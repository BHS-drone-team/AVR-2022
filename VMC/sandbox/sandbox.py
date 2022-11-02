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
)
from loguru import logger
import time

class Sandbox(MQTTModule):

    # NOTE needs logic to handle multiple drops per auto
    def __init__(self):
        super().__init__()

        self.topic_map = {"avr/autonomous/enable": self.on_autonomous_enable, "avr/apriltags/visible" : self.update_visible_tag, "avr/autonomous/building/drop" : self.reset_switch}
#        self.topic_map = {"avr/apriltags/visible": self.on_autonomous_enable}
#        self.visible_map = {"avr/apriltags/visible" : self.update_visible_tag} # On seeing an april tag, run update_visible_tag
        self.visible_tag = None
        self.has_dropped_0 = False
        self.has_dropped_1 = False
        self.has_dropped_2 = False
        self.has_dropped_3 = False
        self.has_dropped_4 = False
        self.has_dropped_5 = False
        self.HORIZ_DROP_TOLERANCE = 20 # Tolerance for dropping water autonomously in cm NOTE needs to be tuned

    # Run autonomous when enabled
    def on_autonomous_enable(self, payload: AvrAutonomousEnablePayload):
        did_message_recieve = payload["enabled"]
        logger.debug(f"visible tag: {self.visible_tag}")
        logger.debug(f"recieved auton enable: {did_message_recieve}")
        # Check if there is a visible april tag, if the vehicle is within specified horizontal tolerance, and if the vehicle has not already dropped the water
        while True:
                start = time.time ()
                finish_1 = start + 2
                while time.time () < finish_1:
                    pass
                if self.visible_tag == 0 and self.has_dropped_0 == False:
                    start = time.time ()
                    finish_1 = start + 1
                    finish_2 = start + 2
                    self.open_servo(0) # Open servo on channel 0
                    self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
                    while time.time () < finish_1:
                        pass
                    self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
                    while time.time () < finish_2:
                        pass
                    self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
                    self.close_servo(0)
                    self.has_dropped_0 = True
                    logger.debug(f"self.has_dropped: {self.has_dropped_0}")
                if self.visible_tag == 1 and self.has_dropped_1 == False:
                    start = time.time ()
                    finish_1 = start + 1
                    finish_2 = start + 2
                    self.close_servo(1) # Open servo on channel 0
                    self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
                    while time.time () < finish_1:
                        pass
                    self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
                    while time.time () < finish_2:
                        pass
                    self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
                    self.open_servo(1)
                    self.has_dropped_1 = True
                    logger.debug(f"self.has_dropped: {self.has_dropped_1}")
                if self.visible_tag == 2 and self.has_dropped_2 == False:
                    start = time.time ()
                    finish_1 = start + 1
                    finish_2 = start + 2
                    self.open_servo(0) # Open servo on channel 0
                    self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
                    while time.time () < finish_1:
                        pass
                    self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
                    while time.time () < finish_2:
                        pass
                    self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
                    self.close_servo(0)
                    self.has_dropped_2 = True
                    logger.debug(f"self.has_dropped: {self.has_dropped_2}")
                if self.visible_tag == 3 and self.has_dropped_3 == False:
                    start = time.time ()
                    finish_1 = start + 1
                    finish_2 = start + 2
                    self.close_servo(1) # Open servo on channel 0
                    self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
                    while time.time () < finish_1:
                        pass
                    self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
                    while time.time () < finish_2:
                        pass
                    self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
                    self.open_servo(1)
                    self.has_dropped_3 = True
                    logger.debug(f"self.has_dropped: {self.has_dropped_3}")
                if self.visible_tag == 4 and self.has_dropped_4 == False:
                    start = time.time ()
                    finish_1 = start + 1
                    finish_2 = start + 2
                    self.open_servo(0) # Open servo on channel 0
                    self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
                    while time.time () < finish_1:
                        pass
                    self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
                    while time.time () < finish_2:
                        pass
                    self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
                    self.close_servo(0)
                    self.has_dropped_4 = True
                    logger.debug(f"self.has_dropped: {self.has_dropped_4}")
                if self.visible_tag == 5 and self.has_dropped_5 == False:
                    start = time.time ()
                    finish_1 = start + 1
                    finish_2 = start + 2
                    self.close_servo(1) # Open servo on channel 0
                    self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
                    while time.time () < finish_1:
                        pass
                    self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
                    while time.time () < finish_2:
                        pass
                    self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
                    self.open_servo(1)
                    self.has_dropped_5 = True
                    logger.debug(f"self.has_dropped: {self.has_dropped_5}")

    def reset_switch(self, payload: AvrAutonomousBuildingDropPayload):#resets the drop so it can drop more than once per tag
        reset = payload["enabled"]
        if reset == True:
            self.has_dropped_0 = False
            self.has_dropped_1 = False
            self.has_dropped_2 = False
            self.has_dropped_3 = False
            self.has_dropped_4 = False
            self.has_dropped_5 = False



    # Update class variable visible_tag to the most currently seen tag and log the horizontal distance between the vehicle and april tag
    def update_visible_tag(self, payload: AvrApriltagsVisiblePayload):
        tag_list = payload["tags"] #this is to get the list out of the payload
        horiz_dist = tag_list[0]["horizontal_dist"]
        tag_id = tag_list[0]["id"]
#        logger.debug(f"Horizontal distance: {horiz_dist} cm") # NOTE need to check which logger method to use
        if horiz_dist < self.HORIZ_DROP_TOLERANCE and tag_id == 0:
            self.visible_tag = 0
        if horiz_dist < self.HORIZ_DROP_TOLERANCE and tag_id == 1:
            self.visible_tag = 1
        if horiz_dist < self.HORIZ_DROP_TOLERANCE and tag_id == 2:
            self.visible_tag = 2
        if horiz_dist < self.HORIZ_DROP_TOLERANCE and tag_id == 3:
            self.visible_tag = 3
        if horiz_dist < self.HORIZ_DROP_TOLERANCE and tag_id == 4:
            self.visible_tag = 4
        if horiz_dist < self.HORIZ_DROP_TOLERANCE and tag_id == 5:
            self.visible_tag = 5

    # Open servo on desired channel
    def open_servo(self, channel):
        self.send_message(
                    "avr/pcm/set_servo_open_close",
                    {"servo": channel, "action": "open"}
            )

    def close_servo(self, channel):
        self.send_message(
                    "avr/pcm/set_servo_open_close",
                    {"servo": channel, "action": "close"}
            )

    # Blink led for desired iterations with desired wrbg value for specified time interval
    def blink_leds(self, time):
        wrgb = (0,0,51,255)
        self.send_message(
                    "avr/pcm/set_temp_color",
                    {"wrgb": wrgb, "time": time}
            )

if __name__ == "__main__":
    box = Sandbox()
    box.run()