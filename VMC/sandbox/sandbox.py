# Here we import our own MQTT library which takes care of a lot of boilerplate
# code related to connecting to the MQTT server and sending/receiving messages.
# It also helps us make sure that our code is sending the proper payload on a topic
# and is receiving the proper payload as well.
#from typing_extensions import Self
from ast import Not
from bell.avr.mqtt.client import MQTTModule
from bell.avr.mqtt.payloads import (
    AvrApriltagsVisiblePayload,
    AvrAutonomousEnablePayload,
    AvrAutonomousBuildingDropPayload,
    AvrApriltagsFpsPayload,
)
from bell.avr.utils import timing
from loguru import logger
import time

class Sandbox(MQTTModule):

    HORIZ_DROP_TOLERANCE = 20 # Tolerance for dropping water autonomously in cm NOTE needs to be tuned
    # NOTE needs logic to handle multiple drops per auto
    def __init__(self):
        super().__init__()

        self.topic_map = {"avr/apriltags/fps" : self.on_autonomous_enable} # On auto enable in GUI, run autonomous
#        self.topic_map = {"avr/autonomous/disable" : self.on_autonomous_disable} # On auto disable in GUI, run autonomous_disable method
        self.topic_map = {"avr/apriltags/visible" : self.update_visible_tag} # On seeing an april tag, run update_visible_tag
        self.visible_tag = None
        self.has_dropped = False
        self.HORIZ_DROP_TOLERANCE = 20 # Tolerance for dropping water autonomously in cm NOTE needs to be tuned

    # Run autonomous when enabled
    def on_autonomous_enable(self, payload: AvrApriltagsFpsPayload) -> None:
        recieved_auton_enable = payload["fps"]
        logger.debug(f"recieved auton enable: {recieved_auton_enable}")
        # Check if there is a visible april tag, if the vehicle is within specified horizontal tolerance, and if the vehicle has not already dropped the water
        if self.visible_tag == 0 and self.has_dropped == False:
            self.open_servo(0) # Open servo on channel 0
            self.blink_leds(3, (255, 255, 0, 0), 0.5) # Blink LEDs 3 times at 0.5 second interval
            self.has_dropped = True
            logger.debug(f"self.has_dropped: {self.has_dropped}")


    # Update class variable visible_tag to the most currently seen tag and log the horizontal distance between the vehicle and april tag
    def update_visible_tag(self, payload: AvrApriltagsVisiblePayload):
        tag_list=payload["tags"] #this is to get the list out of the payload
        horiz_dist = tag_list[0]["horizontal_dist"]
        tag_id = tag_list[0]["id"]
        logger.debug(f"Horizontal distance: {horiz_dist} cm") # NOTE need to check which logger method to use
        if horiz_dist < self.HORIZ_DROP_TOLERANCE and tag_id == 0:
            self.visible_tag = 0

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