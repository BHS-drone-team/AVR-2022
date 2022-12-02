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
        x_dist = tag_list[0]["pos_rel"]["x"]
        y_dist = tag_list[0]["pos_rel"]["y"]
        tag_id = tag_list[0]["id"]
        logger.debug(f"tag is being sensed: {tag_id}")
        X_DROP_TOLERANCE = -3 # Tolerance for dropping water autonomously in cm NOTE needs to be tuned
        Y_DROP_TOLERANCE = -10
    #        logger.debug(f"Horizontal distance: {horiz_dist} cm") # NOTE need to check which logger method to use
        if x_dist < X_DROP_TOLERANCE and y_dist < Y_DROP_TOLERANCE:
            if tag_id == 0 and self.has_dropped_0 == False:
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
            if tag_id == 1 and self.has_dropped_1 == False:
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
                self.open_servo(0)
            if tag_id == 2 and self.has_dropped_2 == False:
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
            if tag_id == 3 and self.has_dropped_3 == False:
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
                self.open_servo(0)
            if tag_id == 4 and self.has_dropped_4 == False:
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
            if tag_id == 5 and self.has_dropped_5 == False:
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
                self.open_servo(0)







    def reset_switch(self, payload: AvrAutonomousBuildingDropPayload):#resets the drop so it can drop more than once per tag
        reset = payload["enabled"]
        reset_button = payload["id"]
        if reset == True and reset_button == 0:
            self.has_dropped_0 = False
            self.has_dropped_1 = False
            self.has_dropped_2 = False
            self.has_dropped_3 = False
            self.has_dropped_4 = False
            self.has_dropped_5 = False
        if reset == True and reset_button == 1:
            self.open_servo(4)
            self.open_servo(5)
        if reset == False and reset_button == 1:
            self.open_servo_percent(4, 99)
            self.close_servo_percent(5, 99)
        if reset == True and reset_button == 4:
            self.open_servo(4)
            self.open_servo(5)
        if reset == False and reset_button == 4:
            self.close_servo(4)
            self.close_servo(5)



    # Open servo on desired channel
    def open_servo(self, channel):
        self.send_message(
                    "avr/pcm/set_servo_open_close",
                    {"servo": channel, "action": "open"}
            )

    def open_servo_percent(self, channel, percent):
        self.send_message(
                    "avr/pcm/set_servo_pct",
                    {"servo": channel, "percent": percent}
            )


    def close_servo(self, channel):
        self.send_message(
                    "avr/pcm/set_servo_open_close",
                    {"servo": channel, "action": "close"}
            )

    def close_servo_percent(self, channel, percent):
        self.send_message(
                    "avr/pcm/set_servo_pct",
                    {"servo": channel, "percent": percent}
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