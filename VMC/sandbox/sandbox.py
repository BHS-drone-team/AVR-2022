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

        self.topic_map = {"avr/apriltags/visible" : self.update_visible_tag, "avr/autonomous/building/drop" : self.reset_switch}
        self.has_dropped_0 = False
        self.has_dropped_1 = False
        self.has_dropped_2 = False
        self.has_dropped_3 = False
        self.has_dropped_4 = False
        self.has_dropped_5 = False


    def update_visible_tag(self, payload: AvrApriltagsVisiblePayload):
        tag_list = payload["tags"] #this is to get the list out of the payload
        horiz_dist = tag_list[0]["horizontal_dist"]
        tag_id = tag_list[0]["id"]
        logger.debug(f"tag is being sensed: {tag_id}")
        HORIZ_DROP_TOLERANCE = 10000000 # Tolerance for dropping water autonomously in cm NOTE needs to be tuned
    #        logger.debug(f"Horizontal distance: {horiz_dist} cm") # NOTE need to check which logger method to use
        if horiz_dist < HORIZ_DROP_TOLERANCE:
            visible_tag = tag_id
            if visible_tag == 0 and self.has_dropped_0 == False:
                self.has_dropped_0 = True
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
            if visible_tag == 1 and self.has_dropped_1 == False:
                self.has_dropped_1 = True
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
            if visible_tag == 2 and self.has_dropped_2 == False:
                self.has_dropped_2 = True
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
            if visible_tag == 3 and self.has_dropped_3 == False:
                self.has_dropped_3 = True
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
            if visible_tag == 4 and self.has_dropped_4 == False:
                self.has_dropped_4 = True
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
            if visible_tag == 5 and self.has_dropped_5 == False:
                self.has_dropped_5 = True
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







#    def reset_switch(self, payload: AvrAutonomousBuildingDropPayload):#resets the drop so it can drop more than once per tag
#        reset = payload["enabled"]
#        reset_button = payload["id"]
#        global has_dropped_0
#        global has_dropped_1
#        global has_dropped_2
#        global has_dropped_3
#        global has_dropped_4
#        global has_dropped_5
#        if reset == True and reset_button == 0:
#            has_dropped_0 = False
#            has_dropped_1 = False
#            has_dropped_2 = False
#            has_dropped_3 = False
#            has_dropped_4 = False
#            has_dropped_5 = False
#        if reset == True and reset_button == 1:
#            self.open_servo(5)
#        if reset == False and reset_button == 1:
#            self.close_servo(5)




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