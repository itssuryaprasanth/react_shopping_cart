from datetime import datetime
from typing import Union, Any
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep
from selenium.webdriver.support import expected_conditions as ec
from features.utilities.custom_logger import CustomLogger
import allure

log = CustomLogger()


class BrowserDriver(webdriver.Chrome):
    def __init__(self):
        log.debug("Initiating Browser driver...")
        super().__init__()
        self.implicitly_wait(time_to_wait=60)

    @staticmethod
    def get_element(locator_type) -> Union[str, bool]:
        if locator_type == "name":
            log.info("Sending back NAME locator as user requested")
            return By.NAME
        if locator_type == "classname":
            log.info("Sending back CLASS_NAME locator as user requested")
            return By.CLASS_NAME
        if locator_type == "xpath":
            log.info("Sending back XPATH locator as user requested")
            return By.XPATH

    def wait_for_element(self, element) -> Union[Any, None]:
        log.debug(f"Waiting for this element ==> {element['value']}")
        value: str = element['value']
        locator_by = BrowserDriver.get_element(locator_type=element['locator'])
        try:
            element_present = ec.presence_of_element_located((locator_by, value))
            return WebDriverWait(self, timeout=30).until(element_present)
        except TimeoutException as e:
            log.error(f"wait_for_element method is failed with an error ==> {e}, returning None to requested method")
            return None

    def click_element(self, element) -> None:
        log.debug(f"Perform click on this element ==> {element['value']}")
        element_status = self.wait_for_element(element)
        if isinstance(element_status, type(None)):
            sleep(2)
            element_status = self.wait_for_element(element)
        element_status.click()
        self.capture_screen_shot()
        log.info(f"Performed click on this element ==> {element['value']}")

    def capture_screen_shot(self) -> None:
        sleep(2)
        log.debug("Capturing screen shot....")
        screenshot_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        try:
            allure.attach(
                self.get_screenshot_as_png(),
                name="BT_" + screenshot_time,
                attachment_type=AttachmentType.PNG,
            )
        except Exception:
            pass

    def launch_url_in_browser(self, url) -> None:
        log.info(f"Launching the browser with these url ===> {url}")
        self.get(url)

    def maximize_browser(self) -> None:
        log.debug("Maximizing the browser..")
        self.maximize_window()

    def element_is_visible(self, element) -> bool:
        log.debug("Check element is visible {}".format(element["value"]))
        try:
            element_status = self.wait_for_element(element=element)
            self.capture_screen_shot()
            log.info(f"Element is visible ==> {(element_visible:=element_status.is_displayed())}")
            return element_visible
        except AttributeError as e:
            self.capture_screen_shot()
            log.error("element is not visible, returning False & error is ==> {}".format(e))
            return False

    def get_text_from_value(self, element) -> Union[str, None]:
        sleep(3)
        log.debug(f"fetching the text from this element {element['value']}")
        element_status = self.wait_for_element(element)
        if element_status is not None:
            log.info(f"Fetching the text in element and text is ==> {element_status.get_attribute('textContent')}")
            if element_status.get_attribute('textContent') != '':
                return str(element_status.get_attribute('textContent'))
            else:
                return None
        else:
            return None

    def quit_browser(self) -> None:
        log.debug("Closing the browser")
        self.quit()

    def wait_and_get_element_list(self, element) -> Union[list, None]:
        log.debug("Wait and get list of elements - {}".format(element["value"]))
        value = element["value"]
        locator_type = BrowserDriver.get_element(element["locator"])
        try:
            self.capture_screen_shot()
            return WebDriverWait(self, timeout=10).until(
                (lambda visible: visible.find_elements(locator_type, value))
            )
        except TimeoutException as e:
            self.capture_screen_shot()
            log.error(
                "Unable to get list of elements data, returning None & error is == > {}".format(
                    e
                )
            )
            return None

    def accept_alert(self) -> None:
        log.debug("Accept the alert")
        alert = self.switch_to.alert
        alert.accept()

    def return_text_from_alert(self) -> str:
        log.debug("bring the text from alert message")
        alert = self.switch_to.alert
        return alert.text

    def do_page_refresh(self) -> None:
        log.debug("Performing page refresh..")
        self.refresh()
