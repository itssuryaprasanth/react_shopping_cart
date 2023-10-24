import logging
import os
from datetime import datetime
from logging import FileHandler
from dotenv import load_dotenv

# Logger object
load_dotenv()

logs_location = rf"{os.getenv('LogsLocation')}"


class CustomLogger:
    """Singleton pattern for logger"""

    __logger_instance = None

    def __new__(cls, name="awcc_automation"):
        if cls.__logger_instance is None:
            cls.__logger_instance = super().__new__(cls)
            cls.__logger_instance.name = name
            cls.__logger_instance.initialize_logger()
        else:
            print("Warning! already object is created!!")

        return cls.__logger_instance.logger

    def initialize_logger(self):
        if not hasattr(self, "initialized"):
            self.initialized = True
            try:
                os.mkdir(logs_location)
                os.mkdir(logs_location + "\\" + "allure-reports")
            except FileExistsError:
                pass
            self.logger = logging.getLogger(self.name)
            self.logger.setLevel(logging.DEBUG)
            now = datetime.now()
            current_time = now.strftime("%m_%d_%Y_%H_%M_%S")
            handler = FileHandler(
                f"{logs_location}" + "BT_Project" + f"_{current_time}" + ".log"
            )
            formatter = logging.Formatter(
                "%(asctime)s  - %(levelname)s: %(message)s",
                datefmt="%m/%d/%Y %I:%M:%S %p",
            )
            handler.setFormatter(formatter)
            self.logger.addHandler(handler)
