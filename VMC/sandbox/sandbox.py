from typing_extensions import Self
from bell.avr.mqtt.client import MQTTModule
from bell.avr.mqtt.payloads import (
    AvrApriltagsVisiblePayload,
    AvrAutonomousEnablePayload,
)
from bell.avr.utils import timing
from loguru import logger
import time

class Sandbox(MQTTModule):
    HORIZ_DROP_TOLERANCE = 20.0 # Tolerance for dropping water autonomously in cm NOTE needs to be tuned
    global visible_tag
    visible_tag = None # Most currently seen april tag
    global has_dropped
    has_dropped = False # Flag to only send drop command once per auto enable
    global is_within_tolerance_variable
    is_within_tolerance_variable = False
    global auton_enable_final
    auton_enable_final = False
    # NOTE needs logic to handle multiple drops per auto
    def __init__(self):
        super().__init__()

        self.topic_map = {"avr/autonomous/enable" : self.on_autonomous_enable} # On auto enable in GUI, run autonomous
#NOTE this doesn't work because it doesn't send enable disable here        self.topic_map = {"avr/autonomous/disable" : self.on_autonomous_disable} # On auto disable in GUI, run autonomous_disable method
        self.topic_map = {"avr/apriltags/visible" : self.update_visible_tag} # On seeing an april tag, run update_visible_tag

        if visible_tag == 0 and is_within_tolerance_variable and has_dropped == False and auton_enable_final:
            self.go_for_auton(True)
            logger.debug(f"has_dropped: {has_dropped}")

    def go_for_auton(self, good_to_go) -> None:
        if good_to_go == True:
            self.open_servo(0) # Open servo on channel 0
            self.blink_leds(3, (255, 255, 0, 0), 0.5) # Blink LEDs 3 times at 0.5 second interval
            global has_dropped
            has_dropped == True

    # Run autonomous when enabled
    def on_autonomous_enable(self, payload: AvrAutonomousEnablePayload):
        auton_enable = payload["enabled"]
        if auton_enable == True:
            global auton_enable_final
            auton_enable_final = True
            logger.debug(f"auton_enable_final: {auton_enable_final}")
        # Check if there is a visible april tag, if the vehicle is within specified horizontal tolerance, and if the vehicle has not already dropped the water




    # Update class variable visible_tag to the most currently seen tag and log the horizontal distance between the vehicle and april tag
    def update_visible_tag(self, payload: AvrApriltagsVisiblePayload):
        tag_list=payload["tags"] #this is to get the list out of the payload
        april_id = tag_list[0]["id"]
        tag_horiz_dist = tag_list[0]["horizontal_dist"] # Horizontal scalar distance from vehicle to tag in cm
        if april_id == 0 and tag_horiz_dist > self.HORIZ_DROP_TOLERANCE:
            global visible_tag
            visible_tag = 0
            logger.debug(f"visible_tag: {visible_tag}")
            global is_within_tolerance_variable
            is_within_tolerance_variable = True
            logger.debug(f"is_within_tolerance_variable: {is_within_tolerance_variable}")



    # Open servo on desired channel
    def open_servo(self, channel):
        self.send_message(
                    "avr/pcm/set_servo_open_close",
                    {"servo": channel, "action": "open"}
            )
    # Close servo on desired channel
    def close_servo(self, channel):
        self.send_message(
                    "avr/pcm/set_servo_open_close",
                    {"servo": channel, "action": "close"}
            )
    # Blink led for desired iterations with desired wrbg value for specified time interval
    def blink_leds(self, iterations, wrgb, time):
        for _ in iterations:
             self.send_message(
                        "avr/pcm/set_temp_color",
                        {"wrgb": wrgb, "time": time}
                )
if __name__ == "__main__":
    box = Sandbox()
    box.run()