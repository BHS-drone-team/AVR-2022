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

bucketServo = int(2)

class Sandbox(MQTTModule):

    # NOTE needs logic to handle multiple drops per auto
    def __init__(self):
        super().__init__()

        self.topic_map = {"avr/apriltags/visible" : self.update_visible_tag, "avr/autonomous/building/drop" : self.extra_uses, "avr/autonomous/enable" : self.enable_auton}
        self.has_dropped_0 = False
        self.has_dropped_1 = False
        self.has_dropped_2 = False
        self.has_dropped_3 = False
        self.has_dropped_4 = False
        self.has_dropped_5 = False
        self.auton_enabled = False


    def update_visible_tag(self, payload: AvrApriltagsVisiblePayload):
        tag_list = payload["tags"] #this is to get the list out of the payload
        x_dist = tag_list[0]["pos_rel"]["x"]
        y_dist = tag_list[0]["pos_rel"]["y"]
        tag_id = tag_list[0]["id"]
        logger.debug(f"tag is being sensed: {tag_id}")
        X_DROP_TOLERANCE = 100000000 # Tolerance for dropping water autonomously in cm NOTE needs to be tuned
        Y_DROP_TOLERANCE = 100000000
    #        logger.debug(f"Horizontal distance: {horiz_dist} cm") # NOTE need to check which logger method to use
        if x_dist < X_DROP_TOLERANCE and y_dist < Y_DROP_TOLERANCE and self.auton_enabled == True:
            if tag_id == 0 and self.has_dropped_0 == False:
                self.drop_building_5()
            if tag_id == 1 and self.has_dropped_1 == False:
                self.drop_building_5()
            if tag_id == 2 and self.has_dropped_2 == False:
                self.drop_building_5()
            if tag_id == 3 and self.has_dropped_3 == False:
                self.drop_building_5()
            if tag_id == 4 and self.has_dropped_4 == False:
                self.drop_building_5()
            if tag_id == 5 and self.has_dropped_5 == False:
                self.drop_building_5()



    def drop_building_1(self):
        self.has_dropped_1 = True
        start = time.time ()
        finish_1 = start + 2
        finish_2 = start + 3
        finish_3 = start + 4
        self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
        while time.time () < finish_2:
            pass
        self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
        while time.time () < finish_3:
            pass
        self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
        self.open_servo(0) # Open servo on channel 0
        while time.time () < finish_1:
            pass
        self.close_servo(0)

    def drop_building_2(self):
        self.has_dropped_2 = True
        start = time.time ()
        finish_1 = start + 2
        finish_2 = start + 3
        finish_3 = start + 4
        while time.time () < finish_1:
            pass
        self.open_servo(0) # Open servo on channel 0
        self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
        while time.time () < finish_2:
            pass
        self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
        while time.time () < finish_3:
            pass
        self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
        self.close_servo(0)

    def drop_building_3(self):
        self.has_dropped_3 = True
        start = time.time ()
        finish_1 = start + 2
        finish_2 = start + 3
        finish_3 = start + 4
        while time.time () < finish_1:
            pass
        self.open_servo(0) # Open servo on channel 0
        self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
        while time.time () < finish_2:
            pass
        self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
        while time.time () < finish_3:
            pass
        self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
        self.close_servo(0)

    def drop_building_4(self):
        self.has_dropped_4 = True
        start = time.time ()
        finish_1 = start + 2
        finish_2 = start + 3
        finish_3 = start + 4
        while time.time () < finish_1:
            pass
        self.open_servo(0) # Open servo on channel 0
        self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
        while time.time () < finish_2:
            pass
        self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
        while time.time () < finish_3:
            pass
        self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
        self.close_servo(0)

    def drop_building_5(self):
        self.has_dropped_5 = True
        start = time.time ()
        finish_1 = start + 2
        finish_2 = start + 3
        finish_3 = start + 4
        self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
        while time.time () < finish_1:
            pass
        self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
        while time.time () < finish_2:
            pass
        self.blink_leds(0.5) # Blink LEDs 1 times at 0.5 second interval
        self.open_servo(0) # Open servo on channel 0
        while time.time () < finish_3:
            pass
        self.close_servo(0)

    def enable_auton(self, paybbhload: AvrAutonomousEnablePayload):
        enable_switch = payload["enabled"]
        self.auton_enabled = enable_switch


    def extra_uses(self, payload: AvrAutonomousBuildingDropPayload):#resets the drop so it can drop more than once per tag
        reset = payload["enabled"]
        reset_button = payload["id"]
        if reset == True and reset_button == 0:
            self.resetting_has_dropped
        if reset == True and reset_button == 1:
            self.open_servo(2)
        if reset == False and reset_button == 1:
            self.open_servo_percent(2, 99)
        if reset == True and reset_button == 4:
            self.open_servo_percent(0, 95)
        if reset == False and reset_button == 4:
            self.close_servo(0)

    def resetting_has_dropped(self):
        self.has_dropped_0 = False
        self.has_dropped_1 = False
        self.has_dropped_2 = False
        self.has_dropped_3 = False
        self.has_dropped_4 = False
        self.has_dropped_5 = False

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