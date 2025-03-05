import subprocess
import logging


def set_mock_location_android(latitude="42.0987", longitude="-75.9180"):
    # command = f"adb shell appops set io.appium.settings android:mock_location allow"
    # subprocess.run(command, shell=True)
    # command = f"adb shell am start-foreground-service --user 0 -n io.appium.settings/.LocationService --es longitude {longitude} --es latitude {latitude} "
    # subprocess.run(command, shell=True)
    import requests
    from requests.auth import HTTPBasicAuth
    # session = self.driver.session_id
    logging.info(f"Mocking Location to lat {latitude} and long {longitude}")
    api_endpoint_geo = f"https://api-cloud.browserstack.com/app-automate/xcuitest/v2/build"
    payload = {
            "gpsLocation": "42.0987, -75.9180",
            "devices": ["iPhone 12-15"],
            "app": "bs://ada346d7adfabcfc5db77af358e593f83832b7ed",
            "testSuite": "bs://ada346d7adfabcfc5db77af358e593f83832b7ed"
        }
    my_username = "anjanikumar_4El02x"
    my_password = "1eoGzmuph1dimfFRWP4k"
    try:
        response = requests.put(api_endpoint_geo, json=payload,
                                headers={'Content-Type': 'application/json', 'Accept': 'application/json'}
                                , auth=HTTPBasicAuth(my_username, my_password))
        if response.status_code == 200 or response.status_code == 204:
            logging.getLogger("root").info(f"response status code : {response.status_code}")
        else:
            logging.getLogger("root").info(f"Failed to retrieve data: {response.status_code}")
    except requests.exceptions.RequestException as e:
        logging.getLogger("root").error(f"API call failed: {e}")

def set_mock_location_ios(driver, latitude, longitude):
    device_name = driver.capabilities['deviceName']
    command = f"xcrun simctl list devices booted | grep '{device_name}' | awk -F '[()]' '{{print $2}}'"
    result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
    device_udid = result.stdout.strip()
    command = [
        'xcrun', 'simctl', 'location', device_udid, 'set', f'{latitude},{longitude}'
    ]
    subprocess.run(command, check=True, text=True, capture_output=True)
