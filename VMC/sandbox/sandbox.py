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
    is_within_tolerance_variable = False
    auton_enable_final = False
    # NOTE needs logic to handle multiple drops per auto
    def __init__(self):
        super().__init__()

        self.topic_map = {"avr/autonomous/enable" : self.on_autonomous_enable} # On auto enable in GUI, run autonomous
#NOTE this doesn't work because it doesn't send enable disable here        self.topic_map = {"avr/autonomous/disable" : self.on_autonomous_disable} # On auto disable in GUI, run autonomous_disable method
        self.topic_map = {"avr/apriltags/visible" : self.update_visible_tag} # On seeing an april tag, run update_visible_tag


    #Run autonomous when enabled
    def on_autonomous_enable(self, payload: AvrAutonomousEnablePayload) -> None:
        auton_enable = payload["enabled"]
        logger.debug(f"auton_enable: {auton_enable}")
#        if auton_enable == True:
#            global auton_enable_final
#            auton_enable_final = True
#            logger.debug(f"auton_enable_final: {auton_enable_final}")

    # Update class variable visible_tag to the most currently seen tag and log the horizontal distance between the vehicle and april tag
    def update_visible_tag(self, payload: AvrApriltagsVisiblePayload):
        tag_list=payload["tags"] #this is to get the list out of the payload
        april_id = tag_list[0]["id"]
        tag_horiz_dist = tag_list[0]["horizontal_dist"] # Horizontal scalar distance from vehicle to tag in cm
        if april_id == 0:
            global visible_tag
            visible_tag = 0
            logger.debug(f"visible_tag: {visible_tag}")
        if tag_horiz_dist < self.HORIZ_DROP_TOLERANCE:
            global is_within_tolerance_variable
            is_within_tolerance_variable = True
            logger.debug(f"is_within_tolerance_variable: {is_within_tolerance_variable}")
    logger.debug(f"is_within_tolerance_variable outside: {is_within_tolerance_variable}")
    logger.debug(f"visible tag outside: {visible_tag}")
    if visible_tag == 0 and is_within_tolerance_variable:
        code_recieved = True
        logger.debug(f"code_recieved: {code_recieved}")
        def open_servo(self):
                self.send_message(
                    "avr/pcm/set_servo_open_close",
                    {"servo": 0, "action": "open"}
            )
        def blink_leds(self):
                for _ in range(3):
                    self.send_message(
                        "avr/pcm/set_temp_color",
                        {"wrgb": (255, 255, 0, 0), "time": 0.5}
                )
                    time.sleep(1)
        def close_servo(self):
                self.send_message(
                    "avr/pcm/set_servo_open_close",
                    {"servo": 0, "action": "close"}
            )
        code_ran=True
        logger.debug(f"code_ran: {code_ran}")
if __name__ == "__main__":
    box = Sandbox()
    box.run()