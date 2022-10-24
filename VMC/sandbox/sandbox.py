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
    visible_tag = None # Most currently seen april tag
    has_dropped = False # Flag to only send drop command once per auto enable
    # NOTE needs logic to handle multiple drops per auto
    def __init__(self):
        super().__init__()

        self.topic_map = {"avr/autonomous/enable" : self.on_autonomous_enable} # On auto enable in GUI, run autonomous
#NOTE this doesn't work because it doesn't send enable disable here        self.topic_map = {"avr/autonomous/disable" : self.on_autonomous_disable} # On auto disable in GUI, run autonomous_disable method
        self.topic_map = {"avr/apriltags/visible" : self.update_visible_tag} # On seeing an april tag, run update_visible_tag

    # Run autonomous when enabled
    def on_autonomous_enable(self, payload: AvrAutonomousEnablePayload):
        # Check if there is a visible april tag, if the vehicle is within specified horizontal tolerance, and if the vehicle has not already dropped the water
        if self.visible_tag != None and self.is_within_tolerance and (not self.has_dropped):
            servo_0 = 0
            self.open_servo(0) # Open servo on channel 0
            self.blink_leds(3, (255, 255, 0, 0), 0.5) # Blink LEDs 3 times at 0.5 second interval
            has_dropped = True

    # Update class variable visible_tag to the most currently seen tag and log the horizontal distance between the vehicle and april tag
    def update_visible_tag(self, payload: AvrApriltagsVisiblePayload):
        tag_list=payload["tags"] #this is to get the list out of the payload
#        self.visible_tag = payload[0] # NOTE if no visible tags are seen, what is payload[0]? If it is None, update visible_tag to None
        horiz_dist = tag_list[1] #pulls the horiz_dist from the tag list
        logger.debug(f"Horizontal distance: {horiz_dist} cm") # NOTE need to check which logger method to use


    # Return whether the vehicle is within the desired horizontal tolerance of the april tag
    def is_within_tolerance(self, payload: AvrApriltagsVisiblePayload):
        tag_list=payload["tags"]
        tag_horiz_dist = tag_list[1]["horizontal_dist"] # Horizontal scalar distance from vehicle to tag in cm
        if tag_horiz_dist > self.HORIZ_DROP_TOLERANCE:
            return True #i did this because it didn't like the variable defining

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