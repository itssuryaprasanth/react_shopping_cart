from features.wrappers.browser_driver import BrowserDriver
from features.utilities.custom_logger import CustomLogger

log = CustomLogger()


class Environment:
    def __init__(self):
        self.driver = ""

    def get_driver(self):
        return self.driver

    def set_driver(self, driver):
        self.driver = driver


def create_environment():
    driver = BrowserDriver()
    env = Environment()
    env.set_driver(driver=driver)
    return env
