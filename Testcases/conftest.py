import os
import logging
import time
import pytest

from appium import webdriver
from appium.options.common import AppiumOptions
from Utilities.read_properties import  read_config_data
from Utilities.common_util import CURRENT_DIR , CONFIG_PATH
@pytest.fixture(autouse=True, scope='session')
def logger_setup(request):
    logger_name = "root"
    root_logger = logging.getLogger(logger_name)
    root_logger.setLevel(logging.INFO)
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(name)s : %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')
    # Adding console handler for displaying logs in the console
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(formatter)
    root_logger.addHandler(consoleHandler)
    fileHandler = None
    log_folder = os.path.join(CURRENT_DIR, '..')
    try:
        log_file = os.path.join(log_folder, 'test_logs.log')
        fileHandler = logging.FileHandler(log_file, mode='w')
        fileHandler.setFormatter(formatter)
        root_logger.addHandler(fileHandler)
    except Exception as e:
        root_logger.info("Error creating log folder or file")
    urllib3_logger = logging.getLogger('urllib3')
    urllib3_logger.setLevel(logging.ERROR)
    consoleHandler.setLevel(logging.ERROR)
    yield
    root_logger.removeHandler(consoleHandler)
    if fileHandler:
        root_logger.removeHandler(fileHandler)
        fileHandler.close()

DEVICE_CONFIGS = {
        "train_driver1": {
            # "appiumServer": "http://127.0.0.1:4723/wd/hub",
            "appiumServer": "http://127.0.0.1:4723",

            "capabilities":{
                    "platformName": "Android",
                    "appium:platformVersion": "15.0",
                    "deviceName": "emulator-5554", #change your device name
                    "appPackage": "org.wikipedia.alpha",
                    "appActivity": "org.wikipedia.main.MainActivity",
                    "appium:automationName": "UiAutomator2",
                    # "app": App/Android/prod_release_2.0.1_build_53.apk,
                    "newCommandTimeout": 100 * 2,
                    "autoGrantPermissions": "true"
                }
        },
        "train_driver2":
            {
                # "appiumServer": "http://127.0.0.1:4725/wd/hub",
                "appiumServer": "http://127.0.0.1:4725",

                "capabilities":{
                "platformName": "Android",
                "appium:platformVersion": "15.0",
                "deviceName": "emulator-5556",
                "udid": "emulator-5556",
                "appPackage": "org.wikipedia.alpha",
                "appActivity": "org.wikipedia.main.MainActivity",
                "appium:automationName": "UiAutomator2",
                "newCommandTimeout": 100 * 2,
                "autoGrantPermissions": "true"
                }
        }
    }
# Global dictionary to map workers to test groups
WORKER_GROUP_MAPPING = {}

@pytest.fixture(scope="session")
def appium_driver_setup(request,pytestconfig):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    if hasattr(pytestconfig, "workerinput"):  # Check if running with xdist
        worker_id = pytestconfig.workerinput["workerid"]
        if worker_id == "gw0":
            WORKER_GROUP_MAPPING[worker_id] = "train_driver1"
        elif worker_id == "gw1":
            WORKER_GROUP_MAPPING[worker_id] = "train_driver2"
        pytestconfig.workerinput["group_name"] = WORKER_GROUP_MAPPING.get(worker_id, "train_driver1")
    worker_id = os.getenv("PYTEST_XDIST_WORKER", "gw0")  # Default to gw0 if running without xdist
    group_name = request.config.workerinput.get("group_name", "train_driver1")
    # group_name = request.config.getoption("--device-group", default="train_driver1")

    if group_name not in DEVICE_CONFIGS:
        pytest.skip(f"No device configuration found for {group_name}")
    config = DEVICE_CONFIGS[group_name]
    capabilities = config["capabilities"].copy()
    logger.info(capabilities)
    options = AppiumOptions().load_capabilities(caps=capabilities)
    localURL = config["appiumServer"]
    driver = webdriver.Remote(localURL, options=options)

# Local execution - AndroidC
    try:
        yield driver
    finally:
        logger.info("~~~~~~~~~~Finally~~~~~~~~~~~~~")
        driver.quit()
        logger.info("~~~~~~~~~~driver quit ~~~~~~~~~~~~~")

def pytest_addoption(parser):
    parser.addoption(
        "--use-browserstack", action="store_true", help="Run tests on BrowserStack"
    )
    parser.addoption(
        "--platform", action="store", default="android", help="Platform to run tests on: android or ios"
    )
    # parser.addoption(
    #     "--device-group", action="store", default="train_driver1", help="Specify the device group to use"
    # )
