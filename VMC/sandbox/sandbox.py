# Here we import our own MQTT library which takes care of a lot of boilerplate
# code related to connecting to the MQTT server and sending/receiving messages.
# It also helps us make sure that our code is sending the proper payload on a topic
# and is receiving the proper payload as well.
#from typing_extensions import Self
from pickle import TRUE
from bell.avr.mqtt.client import MQTTModule
from bell.avr.mqtt.payloads import (
    AvrFcmVelocityPayload,
    AvrPcmSetBaseColorPayload,
    AvrApriltagsVisiblePayload,
    AvrPcmSetTempColorPayload,
    AvrApriltagsVisibleTags,
    AvrApriltagsRawPayload,
    AvrAutonomousBuildingDropPayload,
    AvrApriltagsSelectedPayload,
    AvrApriltagsRawTags,
    AvrPcmSetServoOpenClosePayload,
)
from bell.avr.utils import timing
from loguru import logger
import time

class Sandbox(MQTTModule):
    def __init__(self) -> None:
        super().__init__()
        
        self.topic_map = {"avr/autonomous/enable": self.printMessage}
    
    def printMessage(self) -> None:
        logger.debug("Message: Enabled")


if __name__ == "__main__":
    # This is what actually initializes the Sandbox class, and executes it.
    # This is nested under the above condition, as otherwise, if this file
    # were imported by another file, these lines would execute, as the interpreter
    # reads and executes the file top-down. However, whenever a file is called directly
    # with `python file.py`, the magic `__name__` variable is set to "__main__".
    # Thus, this code will only execute if the file is called directly.
    box = Sandbox()
    # The `run` method is defined by the inherited `MQTTModule` class and is a
    # convience function to start processing incoming MQTT messages infinitely.
    box.run()
