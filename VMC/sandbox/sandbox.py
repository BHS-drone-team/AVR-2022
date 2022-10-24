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
)
from bell.avr.utils import timing
from loguru import logger
import time

class Sandbox(MQTTModule):

    def __init__(self):
        super().__init__()

        self.topic_map = {"avr/autonomous/enable" : self.on_autonomous_enable} # On auto enable in GUI, run autonomous
#NOTE this doesn't work because it doesn't send enable disable here        self.topic_map = {"avr/autonomous/disable" : self.on_autonomous_disable} # On auto disable in GUI, run autonomous_disable method
        self.topic_map = {"avr/apriltags/visible" : self.update_visible_tag} # On seeing an april tag, run update_visible_tag

    # Run autonomous when enabled
    def on_autonomous_enable(self, payload: AvrAutonomousEnablePayload):
        run_auton = payload["enabled"]
        if run_auton == True:
            self.has_dropped(False)
        # Check if there is a visible april tag, if the vehicle is within specified horizontal tolerance, and if the vehicle has not already dropped the water
        if self.visible_tag != None and self.is_within_tolerance and self.has_dropped == False:
            self.open_servo(0) # Open servo on channel 0
            self.blink_leds(3, (255, 255, 0, 0), 0.5) # Blink LEDs 3 times at 0.5 second interval
            has_dropped = True

    def has_dropped(self, boolean):
        has_dropped = boolean
        if has_dropped == False:
            return False
        if has_dropped == True:
            return True
    # Run when autonomous is disabled
#    def on_autonomous_disable(self):
#        global has_dropped
#        has_dropped = False # Reset the has_dropped flag for next auto run

    # Update class variable visible_tag to the most currently seen tag and log the horizontal distance between the vehicle and april tag
    def update_visible_tag(self, payload: AvrApriltagsVisiblePayload):
        tag_list=payload["tags"] #this is to get the list out of the payload
#        self.visible_tag = payload[0] # NOTE if no visible tags are seen, what is payload[0]? If it is None, update visible_tag to None
        horiz_dist = tag_list[0]["horizontal_dist"] #pulls the horiz_dist from the tag list
        april_tag_id = tag_list[0]["id"]
#        logger.debug(f"Horizontal distance: {horiz_dist} cm") # NOTE need to check which logger method to use
        if april_tag_id == 0:
            self.visible_tag(0)


    def visible_tag(self, tag_id_message):
        tag_id = tag_id_message
        if tag_id == 0:
            return 0
    # Return whether the vehicle is within the desired horizontal tolerance of the april tag
    def is_within_tolerance(self, payload: AvrApriltagsVisiblePayload):
        tag_list=payload["tags"]
        tag_horiz_dist = tag_list[0]["horizontal_dist"] # Horizontal scalar distance from vehicle to tag in cm
        HORIZ_DROP_TOLERANCE = 20.0
        if tag_horiz_dist < HORIZ_DROP_TOLERANCE:
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