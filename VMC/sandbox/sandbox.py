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
from threading import Thread

class AprilSensor(Thread):

    def __init__(self):
        super().__init__()

        self.topic_map = {"avr/apriltags/visible": self.update_visible_tag}

    def update_visible_tag(self, payload: AvrApriltagsVisiblePayload):
        tag_list = payload["tags"] #this is to get the list out of the payload
        horiz_dist = tag_list[0]["horizontal_dist"]
        tag_id = tag_list[0]["id"]
        logger.debug(f"tag is being sensed: {tag_id}")
        HORIZ_DROP_TOLERANCE = 10000000 # Tolerance for dropping water autonomously in cm NOTE needs to be tuned
    #        logger.debug(f"Horizontal distance: {horiz_dist} cm") # NOTE need to check which logger method to use
        if horiz_dist < HORIZ_DROP_TOLERANCE:
            global visible_tag
            visible_tag = tag_id

class Sandbox(MQTTModule):

    # NOTE needs logic to handle multiple drops per auto
    def __init__(self):
        super().__init__()

        self.topic_map = {"avr/autonomous/enable": self.on_autonomous_enable, "avr/autonomous/building/drop" : self.reset_switch}
#        self.topic_map = {"avr/apriltags/visible": self.on_autonomous_enable}
#        self.visible_map = {"avr/apriltags/visible" : self.update_visible_tag} # On seeing an april tag, run update_visible_tag
        global has_dropped_0
        has_dropped_0 = False
        global has_dropped_1
        has_dropped_1 = False
        global has_dropped_2
        has_dropped_2 = False
        global has_dropped_3
        has_dropped_3 = False
        global has_dropped_4
        has_dropped_4 = False
        global has_dropped_5
        has_dropped_5 = False
        global has_dropped_all
        has_dropped_all = False
        global visible_tag
        visible_tag = None
    # Run autonomous when enabled
    def on_autonomous_enable(self, payload: AvrAutonomousEnablePayload):
        did_message_recieve = payload["enabled"]
        logger.debug(f"visible tag: {visible_tag}")
        logger.debug(f"recieved auton enable: {did_message_recieve}")
        global has_dropped_all
        # Check if there is a visible april tag, if the vehicle is within specified horizontal tolerance, and if the vehicle has not already dropped the water
        while has_dropped_all == False:
            global has_dropped_0
            global has_dropped_1
            global has_dropped_2
            global has_dropped_3
            global has_dropped_4
            global has_dropped_5
            loop_running = True
            logger.debug(f"loop running: {loop_running}")
            logger.debug(f"visible tag in loop: {visible_tag}")
            start = time.time ()
            finish_1 = start + 2
            while time.time () < finish_1:
                pass
            if visible_tag == 0 and has_dropped_0 == False:
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
                has_dropped_0 = True
                logger.debug(f"self.has_dropped: {has_dropped_0}")
            if visible_tag == 1 and has_dropped_1 == False:
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
                has_dropped_1 = True
                logger.debug(f"has_dropped: {has_dropped_1}")
            if visible_tag == 2 and has_dropped_2 == False:
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
                has_dropped_2 = True
                logger.debug(f"has_dropped: {has_dropped_2}")
            if visible_tag == 3 and has_dropped_3 == False:
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
                has_dropped_3 = True
                logger.debug(f"has_dropped: {has_dropped_3}")
            if visible_tag == 4 and has_dropped_4 == False:
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
                has_dropped_4 = True
                logger.debug(f"has_dropped: {has_dropped_4}")
            if visible_tag == 5 and has_dropped_5 == False:
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
                has_dropped_5 = True
                logger.debug(f"has_dropped: {has_dropped_5}")
            if has_dropped_0 == True and has_dropped_1 == True and has_dropped_2 == True and has_dropped_3 == True and has_dropped_4 == True and has_dropped_5 == True:
                logger.debug("ending loop")
                has_dropped_all = True

    def reset_switch(self, payload: AvrAutonomousBuildingDropPayload):#resets the drop so it can drop more than once per tag
        reset = payload["enabled"]
        reset_button = payload["id"]
        global has_dropped_0
        global has_dropped_1
        global has_dropped_2
        global has_dropped_3
        global has_dropped_4
        global has_dropped_5
        if reset == True and reset_button == 0:
            has_dropped_0 = False
            has_dropped_1 = False
            has_dropped_2 = False
            has_dropped_3 = False
            has_dropped_4 = False
            has_dropped_5 = False
        if reset == True and reset_button == 1:
            self.open_servo(5)
        if reset == False and reset_button == 1:
            self.close_servo(5)




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
    x = threading.Thread(target = Sandbox)
    x.start()
    y = Thread(target = AprilSensor, args=(1,))
    y.run()
