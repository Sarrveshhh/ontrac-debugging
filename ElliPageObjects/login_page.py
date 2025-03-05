import os
import time
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait
from Base.custom_code import Custom_code
import logging
import subprocess
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.custom_code import Custom_code
from selenium.webdriver import Keys, ActionChains


class ElliLoginPage(Custom_code):
    locators = {
        'android': {
            'Skip_btn': (AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.ontrac.onroute:id/tvSkip']"),
            'elli_Bata_logo': (AppiumBy.XPATH, "//*[@resource-id='com.ontrac.onroute:id/icLogo']"),
            'text_488': (AppiumBy.XPATH, "//android.widget.LinearLayout[@resource-id='com.ontrac.onroute:id/llLang']/preceding-sibling::android.widget.TextView"),
            'base_sequence_url_input': (AppiumBy.XPATH,"//android.widget.EditText[@resource-id='com.ontrac.onroute:id/dialogTwoInputsFirstInput']"),
            'base_events_url_input_field': (AppiumBy.XPATH,"//android.widget.EditText[@resource-id='com.ontrac.onroute:id/dialogTwoInputsSecondInput']"),
            'submit_button': (AppiumBy.XPATH,"//android.widget.Button[@resource-id='com.ontrac.onroute:id/dialogTwoInputsButtonFirst']"),
            'driver_id_text_bar': (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='com.ontrac.onroute:id/etDriverId']"),
            'password_text_bar': (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='com.ontrac.onroute:id/etPassword']"),
            'check_box_termAndConditions': (AppiumBy.XPATH, "//android.widget.CheckBox[@resource-id='com.ontrac.onroute:id/cbTerms']"),
            'login_btn': (AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.ontrac.onroute:id/btnSubmit']"),
            'skip_permission_btn': (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.ontrac.onroute:id/btnSkip']"),
            'close_map_btn': (AppiumBy.XPATH, "(//android.widget.ImageView)[1]"),
            'package_text': (AppiumBy.XPATH, "//android.widget.TextSwitcher"),
            'ontrac_driver_id': (AppiumBy.XPATH,"//android.widget.LinearLayout[@resource-id='com.ontrac.onroute:id/crlOptionList']/android.widget.FrameLayout[1]/android.view.ViewGroup"),
            'next_btn': (AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.ontrac.onroute:id/btnNext']"),
            'icon_Settings': (AppiumBy.XPATH,"//android.widget.TextView[@resource-id='com.ontrac.onroute:id/tvOptionSettings']"),
            'logout_btn': (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='com.ontrac.onroute:id/tvLogout']"),
            'language_settings': (AppiumBy.XPATH, "//*[@resource-id='com.ontrac.onroute:id/llSettings']"),
            'language_lable': (AppiumBy.XPATH, "//*[@resource-id='com.ontrac.onroute:id/tvLanguage']"),
            'engilsh_language': (AppiumBy.XPATH, "//*[@resource-id='com.ontrac.onroute:id/tvEnglish']"),
            'Español_language': (AppiumBy.XPATH, "//*[@resource-id='com.ontrac.onroute:id/tvSpanish']"),
            'French_comingSoon_language': (AppiumBy.XPATH, "(//android.widget.CheckedTextView)[3]"),
            'idioma_label': (AppiumBy.XPATH, "//android.widget.LinearLayout/android.widget.TextView"),
            'Id_del_conductor': (AppiumBy.XPATH, "(//android.view.ViewGroup/android.widget.TextView)[2]"),
            'contraseria': (AppiumBy.XPATH, "(//android.view.ViewGroup/android.widget.TextView)[3]"),

            'code_text_bar': (AppiumBy.XPATH, "//android.widget.EditText[@resource-id='com.ontrac.onroute:id/etVerificationCode']"),
            'use_mylocation': (AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.ontrac.onroute:id/btnAction']"),
            'allow_for_location': (AppiumBy.XPATH,"//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']"),
            'open_settings': (AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.ontrac.onroute:id/btnAction']"),
            'allow1': (AppiumBy.XPATH,"//android.widget.RadioButton[@resource-id='com.android.permissioncontroller:id/allow_foreground_only_radio_button']"),
            'back_arrow': (AppiumBy.XPATH, "//android.view.ViewGroup/android.widget.ImageButton"),
            'navigate_up': (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']"),
            'camera': (AppiumBy.XPATH, "//android.widget.Button[@resource-id='com.ontrac.onroute:id/btnAction']"),
            'allow_for_camera': (AppiumBy.XPATH,"//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_foreground_only_button']"),
            'skip': (AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='com.ontrac.onroute:id/ivClose']"),
            'allow_notifications' : (AppiumBy.XPATH,"//android.widget.Button[@resource-id='com.ontrac.onroute:id/btnAction']"),
            'pop_allow': (AppiumBy.XPATH,"//android.widget.Button[@resource-id='com.android.permissioncontroller:id/permission_allow_button']"),
            'close': (AppiumBy.XPATH, "//android.widget.ImageView[@resource-id='com.ontrac.onroute:id/ivClose']"),
            'by_using_our_app_TermsAndConditions_Lable': (AppiumBy.XPATH, "//*[@resource-id='com.ontrac.onroute:id/tvTerms']"),
            'terms_and_conditions_text': (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'terms & conditions')]"),
            'ontrac_logo': (AppiumBy.XPATH, "//android.view.View/android.widget.Image"),
            'no_connection_text': (AppiumBy.XPATH, '//android.widget.TextView[@text="No Connection"]'),
            'refresh_btn': (AppiumBy.XPATH, '//android.widget.ImageButton[@resource-id="com.ontrac.onroute:id/btnRefresh"]'),
            'accept_btn_1':(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.ontrac.onroute:id/btnAccept"]'),
            'accept_btn_2':(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.ontrac.onroute:id/btnAccept"]'),
            'accept_1_text_1':(AppiumBy.XPATH,'(//android.widget.FrameLayout[@resource-id="com.ontrac.onroute:id/custom"]/android.widget.LinearLayout//android.widget.TextView)[1]'),
            'accept_1_text_2': (AppiumBy.XPATH, '(//android.widget.FrameLayout[@resource-id="com.ontrac.onroute:id/custom"]/android.widget.LinearLayout//android.widget.TextView)[2]'),
            'accept_2_text_1': (AppiumBy.XPATH, '(//android.widget.ScrollView[@resource-id="com.ontrac.onroute:id/scrollableContent"]/android.widget.LinearLayout//android.widget.TextView)[1]'),
            'accept_2_text_2': (AppiumBy.XPATH, '(//android.widget.ScrollView[@resource-id="com.ontrac.onroute:id/scrollableContent"]/android.widget.LinearLayout//android.widget.TextView)[2]'),
            'screen_after_close_and_re_launch_app':(AppiumBy.XPATH,'//android.view.ViewGroup[@resource-id="com.ontrac.onroute:id/clContainer"]'),
            'landing_page':(AppiumBy.XPATH,'//android.view.ViewGroup[@resource-id="com.ontrac.onroute:id/viewNavigation"]'),
            'wrong_email_sent_code_message':(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.ontrac.onroute:id/snackbar_text"]'),
            'great_news_ok_btn':(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.ontrac.onroute:id/dialogAlertBtnPositive"]'),
            'relogin_pop_validation_code_field':(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="com.ontrac.onroute:id/dialogTwoInputsSecondInput"]'),
            'relogin_pop_up_submit_button':(AppiumBy.XPATH,'//android.widget.Button[@resource-id="com.ontrac.onroute:id/dialogTwoInputsButtonFirst"]'),
            'Facility_choose_screen':(AppiumBy.XPATH,'//android.widget.TextView[@text="Select Facility"]'),
            'main_login_screem':(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.ontrac.onroute:id/tvTitle"]'),
            'select_RSP_heading':(AppiumBy.XPATH,'//android.widget.TextView[@text="Select RSP"]'),
            'select_facility_heading':(AppiumBy.XPATH,'//android.widget.TextView[@text="Select Facility"]'),
            'user_is_already_logged_out':(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.ontrac.onroute:id/snackbar_text"]'),
            'version_number_section': (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.ontrac.onroute:id/tvVer"]'),

            'back_button': (AppiumBy.XPATH, "//*[@resource-id='com.ontrac.onroute:id/btnBack']"),

            'login_page_settings':(AppiumBy.XPATH,'//android.widget.LinearLayout[@resource-id="com.ontrac.onroute:id/llSettings"]'),
            'login_page_language_option':(AppiumBy.XPATH,'//android.widget.TextView[@resource-id="com.ontrac.onroute:id/tvLanguage"]'),
            'spanish_language':(AppiumBy.XPATH,'//android.widget.CheckedTextView[@resource-id="com.ontrac.onroute:id/tvSpanish"]'),
            'english_language':(AppiumBy.XPATH,'//android.widget.CheckedTextView[@resource-id="com.ontrac.onroute:id/tvEnglish"]'),
            'language_back_button':(AppiumBy.XPATH,'//android.widget.ImageButton[@resource-id="com.ontrac.onroute:id/btnBack"]')
            },
        'ios': {
            # Add iOS locators here if needed
            'read_now_btn': (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Read now"]'),
            'ok_btn': (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="okButton"]'),
            'Skip_btn': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Skip"]'),
            'elli_Bata_logo': (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="eliLogo"]'),
            'text_488': (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Language"]/following-sibling::XCUIElementTypeButton'),
            'base_sequence_url_input': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Base Sequence URL"]/following::XCUIElementTypeTextField[1]'),
            'base_events_url_input_field': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Base Sequence URL"]/following::XCUIElementTypeTextField[2]'),
            'submit_button': (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Submit"]'),
            'driver_id_text_bar': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Driver ID"]/following::*[@type="XCUIElementTypeTextField"][1]'),
            'password_text_bar': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Password"]/following::*[@type="XCUIElementTypeSecureTextField"][1]'),
            'check_box_termAndConditions': (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="acceptCheckbox"]'),
            'login_btn': (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="loginButton"]'),
            # 'proceed_location_btn' (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Proceed"]'),
            'code_text_bar': (AppiumBy.XPATH, '//XCUIElementTypeTextField[@name="enterCodeTextField"]'),
            'send_code_btn': (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="sendCodeButton"]'),
            'ontrac_driver_id': (AppiumBy.XPATH, '//XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeOther[1]'),
            'next_btn': (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="selectRspButton"]'),
            'select_facility': (AppiumBy.XPATH, '(//XCUIElementTypeCell[@name="pickersItemCell"])[1]'),
            'icon_Settings': (AppiumBy.XPATH, '//XCUIElementTypeImage[@name="ic_setting_bottom_bar"]'),
            'logout_btn': (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="logoutButton"]'),
            'language_lable': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Language"]'),
            'engilsh_language': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="English"]'),
            'Español_language': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Español"]'),
            'French_comingSoon_language': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="French (coming soon)"]'),
            'idioma_label': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="Idioma"]'),
            'Id_del_conductor': (AppiumBy.XPATH, '//XCUIElementTypeTextField[@name="loginTextField"]'),
            # 'contraseria': (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Passwords"]'),
            'use_mylocation': (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="proceedButton"]'),
            'camera': (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="proceedButton"]'),
            'allow_notifications': (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="proceedButton"]'),
            'pop_allow': (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Allow"]'),
            'close': (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="closeButton"]'),
            'by_using_our_app_TermsAndConditions_Lable': (AppiumBy.XPATH, '//XCUIElementTypeLink[@name="terms & conditions"]'),
            'terms_and_conditions_text': (AppiumBy.XPATH, '//XCUIElementTypeLink[@name="terms & conditions"]'),
            'ontrac_logo': (AppiumBy.XPATH, '//XCUIElementTypeOther[@name="banner"]'),
            'download_now_btn': (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="proceedButton"]'),
            'no_connection_text': (AppiumBy.XPATH, '//XCUIElementTypeStaticText[@name="No Connection"]'),
            'package_text': (AppiumBy.XPATH, '(//XCUIElementTypeButton[@name="scanButton"]/parent::XCUIElementTypeOther/preceding-sibling::XCUIElementTypeStaticText)[3]'),
            'refresh_btn': (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="ic refresh"]'),
            'allow_once': (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Allow Once"]'),
            'allow_for_camera': (AppiumBy.XPATH, '//XCUIElementTypeButton[@name="Allow"]')

        }
    }






    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_ok_btn_ios(self):
        try:
            if self.get_element(self.locators[self.platform]['ok_btn']):
                self.ElementPresent_and_click(self.locators[self.platform]['ok_btn'])
        except Exception as e:
            logging.getLogger("root").info(f"Exception in get_element: {str(e)}")

    def click_on_skip_element(self):
        assert self.get_element_present_status(self.locators[self.platform]['Skip_btn']), "Failed to find Skip button after App launched"
        self.ElementPresent_and_click(self.locators[self.platform]['Skip_btn'])

    def accept_prominent_disclosure(self):
        if self.driver.capabilities['platformName'].lower() == 'android':

            self.ElementPresent_and_click(self.locators[self.platform]['accept_btn_1'])
            time.sleep(2)
            self.ElementPresent_and_click(self.locators[self.platform]['accept_btn_2'])

    def click_on_version_multiple_times(self, times,wait_after_taps=10):
        if self.driver.capabilities['platformName'].lower() == 'ios':
            #commented for BrowserStack
            version = self.get_element(self.locators[self.platform]['text_488'])
            # center_x = version.location['x'] + version.size['width'] / 2
            # center_y = version.location['y'] + version.size['height'] / 2
            # params = {"x": center_x, "y": center_y}
            # for _ in range(times + 1):
            #     self.driver.execute_script("mobile: doubleTap", params)
        else:
            time.sleep(3)
            for _ in range(times):
                self.ElementPresent_and_click(self.locators[self.platform]['version_number_section'])

    def change_sequence_url(self, sequence_url):
        if self.driver.capabilities['platformName'].lower() == 'ios':
            logging.getLogger("root").info("Escape this for ios")
            #commented for browserstack
            #     try:
            #         version = self.get_element(self.locators[self.platform]['text_488'])
            #         for _ in range(10):
            #             version.click()
            #     except Exception as e:
            #       logging.getLogger("root").info(f"Exception in get_element: {str(e)}")

        else:
            locator = self.locators[self.platform]['base_sequence_url_input']
            self.clear_field(locator)
            self.send_keys_to(locator, sequence_url)

    def change_events_url(self, events_url):
        if self.driver.capabilities['platformName'].lower() == 'android':
            locator = self.locators[self.platform]['base_events_url_input_field']
            self.clear_field(locator)
            self.send_keys_to(locator, events_url)

    def submit_form(self):
        self.ElementPresent_and_click(self.locators[self.platform]['submit_button'])

    def perform_initial_actions(self):
        # if self.driver.capabilities['platformName'].lower() == 'ios':
            # self.click_on_ok_btn_ios()

        self.click_on_skip_element()
        if self.driver.capabilities['platformName'].lower() == 'android':
             self.accept_prominent_disclosure()

        self.click_on_version_multiple_times(10)

    def fill_and_submit_form(self, sequence_url, events_url):
        if self.driver.capabilities['platformName'].lower() == 'android':
            self.change_sequence_url(sequence_url)
            self.change_events_url(events_url)
            self.submit_form()
            self.isElementPresent(self.locators[self.platform]['elli_Bata_logo'])

    def verify_app_logged_out(self):
        try:
            return self.isElementPresent(self.locators[self.platform]['driver_id_text_bar'])
        except:
            return False

    def verify_app_logged_out(self):
        try:
            return self.isElementPresent(self.locators[self.platform]['driver_id_text_bar'])
        except:
            return False

    def login_driver(self, driver_id, password):
        time.sleep(5)
        driver_id_locator = self.locators[self.platform]['driver_id_text_bar']
        self.clear_field(driver_id_locator)
        self.send_keys_to(driver_id_locator, driver_id)
        time.sleep(2)
        try:
            self.driver.find_element(AppiumBy.XPATH, '(//*)[1]').send_keys(Keys.RETURN)
        except NoSuchElementException:
            logging.info("The keyboard screen didn't appear.")
        time.sleep(2)
        self.scroll_fixed_steps(steps=2)
        check_box_term_and_conditions_locator = self.locators[self.platform]['check_box_termAndConditions']
        self.ElementPresent_and_click(check_box_term_and_conditions_locator)
        condition = True
        while condition:
            self.scroll_fixed_steps(steps=2)
            submit_btn_locator = self.locators[self.platform]['login_btn']
            condition =  not self.ElementPresent_and_click(submit_btn_locator)
            if not condition:
                break
        email_code_locator = self.locators[self.platform]['code_text_bar']
        time.sleep(5)
        self.clear_field(email_code_locator)
        # Handle the driver logged-in issue
        try:
            assert self.get_element(email_code_locator)
        except Exception:
            i = 1
            if driver_id.upper() not in ['ORLAQADRV02','ORLAQADRV01', 'NASHQADRV02','NASHQADRV01',
                                         'ASHDQADRV02','ASHDQADRV01', 'CLVDQADRV02', 'CLVDQADRV01']:
                while i <= 10:
                    driver_id = driver_id + str(i)
                    self.clear_field(driver_id_locator)
                    self.send_keys_to(driver_id_locator, driver_id)
                    self.ElementPresent_and_click(submit_btn_locator)
                    try:
                        assert self.get_element(email_code_locator)
                        break
                    except Exception as e:
                        i = i + 1
        #Handle the driver logged-in issue
        self.send_keys_to(email_code_locator, password)
        if self.driver.capabilities['platformName'].lower() == 'android':
            self.ElementPresent_and_click(submit_btn_locator)
        if self.driver.capabilities['platformName'].lower() == 'ios':
            self.ElementPresent_and_click(self.locators[self.platform]['send_code_btn'])
        time.sleep(5)
        self.ElementPresent_and_click(self.locators[self.platform]['ontrac_driver_id'])
        self.ElementPresent_and_click(self.locators[self.platform]['next_btn'])
        if self.driver.capabilities['platformName'].lower() == 'ios':
            self.ElementPresent_and_click(self.locators[self.platform]['select_facility'])
        login_result = self.ElementPresent_and_click(self.locators[self.platform]['next_btn'])
        time.sleep(5)
        assert login_result, 'Failed to login to OnRoute'

    def skip_permissions(self):
        skip_permission_btn_locator = self.locators[self.platform]['skip_permission_btn']
        self.ElementPresent_and_click(skip_permission_btn_locator)
        # self.imp_wait_20()
        self.ElementPresent_and_click(skip_permission_btn_locator)
        # self.imp_wait_20()
        self.ElementPresent_and_click(skip_permission_btn_locator)
        # self.imp_wait_20()
        close_map_btn_locator = self.locators[self.platform]['close_map_btn']
        self.imp_wait_20()
        logging.getLogger("root").info(close_map_btn_locator)
        self.ElementPresent_and_click(close_map_btn_locator)
        # self.ElementPresent_and_click(close_map_btn_locator)

    def get_package_data(self):
        package_text_locator = self.locators[self.platform]['package_text']
        return self.get_element(package_text_locator).text

    def logout_driver(self):
        icon_settings_btn_locator = self.locators[self.platform]['icon_Settings']
        time.sleep(5)
        logout_btn_btn_locator = self.locators[self.platform]['logout_btn']
        self.ElementPresent_and_click(icon_settings_btn_locator)
        assert self.isElementPresent(logout_btn_btn_locator), "Failed to find Logout button"
        self.ElementPresent_and_click(logout_btn_btn_locator)
        time.sleep(3)

    def logout_driver_from_finally(self):
        icon_settings_btn_locator = self.locators[self.platform]['icon_Settings']
        time.sleep(5)
        logout_btn_btn_locator = self.locators[self.platform]['logout_btn']
        self.ElementPresent_and_click(icon_settings_btn_locator)
        self.ElementPresent_and_click(logout_btn_btn_locator)
        time.sleep(3)

    def click_on_language_button(self):
        self.isElementPresent(self.locators[self.platform]['language_settings'])
        self.ElementPresent_and_click(self.locators[self.platform]['language_settings'])
        self.isElementPresent(self.locators[self.platform]['language_lable'])
        self.ElementPresent_and_click(self.locators[self.platform]['language_lable'])

    def click_on_english_language(self):
        self.ElementPresent_and_click(self.locators[self.platform]['engilsh_language'])
        self.ElementPresent_and_click(self.locators[self.platform]['back_button'])
        self.wait_for_element_not_clickable(self.locators[self.platform]['back_button'])
        self.ElementPresent_and_click(self.locators[self.platform]['back_button'])
        self.isElementPresent(self.locators[self.platform]['elli_Bata_logo'])

    def click_on_espanol_language(self):
        self.ElementPresent_and_click(self.locators[self.platform]['Español_language'])
        self.ElementPresent_and_click(self.locators[self.platform]['back_button'])
        self.wait_for_element_not_clickable(self.locators[self.platform]['back_button'])
        self.ElementPresent_and_click(self.locators[self.platform]['back_button'])

    def assert_language_options_visible(self):
        # self.isElementPresent(self.locators[self.platform]['language_lable'])
        self.isElementPresent(self.locators[self.platform]['engilsh_language'])
        self.isElementPresent(self.locators[self.platform]['Español_language'])
        # self.isElementPresent(self.locators[self.platform]['French_comingSoon_language'])

    def assert_spanish_language_elements_visible(self):
        self.isElementPresent(self.locators[self.platform]['elli_Bata_logo'])
        # self.isElementPresent(self.locators[self.platform]['contraseria'])
        self.isElementPresent(self.locators[self.platform]['Id_del_conductor'])
        self.isElementPresent(self.locators[self.platform]['idioma_label'])

    def location_permission(self):
        return
        self.ElementPresent_and_click(self.locators[self.platform]['use_mylocation'])
        if self.driver.capabilities['platformName'].lower() == 'android':
            self.ElementPresent_and_click(self.locators[self.platform]['allow_for_location'])
            self.ElementPresent_and_click(self.locators[self.platform]['open_settings'])
            self.ElementPresent_and_click(self.locators[self.platform]['allow1'])
            self.ElementPresent_and_click(self.locators[self.platform]['back_arrow'])
        else:
            self.ElementPresent_and_click(self.locators[self.platform]['allow_once'])
    def camera_permission(self):
        return
        time.sleep(2)
        self.ElementPresent_and_click(self.locators[self.platform]['camera'])
        # if self.driver.capabilities['platformName'].lower() == 'android':
        self.ElementPresent_and_click(self.locators[self.platform]['allow_for_camera'])

    def skip_notification(self):
        return
        time.sleep(2)
        self.ElementPresent_and_click(self.locators[self.platform]['allow_notifications'])
        if self.driver.capabilities['platformName'].lower() == 'android':
            self.ElementPresent_and_click(self.locators[self.platform]['pop_allow'])
        else:
            self.ElementPresent_and_click(self.locators[self.platform]['pop_allow'])
    def download_map(self):
         return
        # if self.driver.capabilities['platformName'].lower() == 'ios':
        #     WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located(self.locators[self.platform]['download_now_btn']))
        # elif self.driver.capabilities['platformName'].lower() == 'android':
        #     pass
         self.ElementPresent_and_click(self.locators[self.platform]['close'])



    def is_internet_connected(self):
        # Check if the device is connected to WiFi
        result = self.driver.execute_script('mobile: shell', {
            'command': 'dumpsys',
            'args': ['wifi'],
            'includeStderr': True,
            'timeout': 5000
        })
        return 'Wi-Fi is enabled' in result.get('stdout', '') and 'connected' in result.get('stdout', '')

    def toggle_network_modes(self, wifi_mode: bool, mobile_data_mode: bool):
        # if self.driver.capabilities['platformName'].lower() == 'android':
        #     try:
        #         # Determine the Wi-Fi command based on wifi_mode
        #         wifi_command = 'enable' if wifi_mode else 'disable'
        #         # Determine the mobile data command based on mobile_data_mode
        #         mobile_data_command = 'enable' if mobile_data_mode else 'disable'
        #
        #         # Construct the adb commands
        #         wifi_cmd = ['adb', 'shell', 'svc', 'wifi', wifi_command]
        #         mobile_data_cmd = ['adb', 'shell', 'svc', 'data', mobile_data_command]
        #
        #         # Run the Wi-Fi command
        #         wifi_result = subprocess.run(wifi_cmd, check=True, text=True, capture_output=True)
        #         logging.info(f"Wi-Fi Command output: {wifi_result.stdout}")
        #
        #         # Run the mobile data command
        #         mobile_data_result = subprocess.run(mobile_data_cmd, check=True, text=True, capture_output=True)
        #         logging.info(f"Mobile Data Command output: {mobile_data_result.stdout}")
        #
        #     except subprocess.CalledProcessError as e:
        #         # Log any errors from the adb command
        #         logging.error(f"Error executing adb command: {e.stderr}")
        #
        #     except Exception as e:
        #         # Log any other unexpected errors
        #         logging.error(f"Unexpected error: {e}")
        # if self.driver.capabilities['platformName'].lower() == 'ios':
        #     if wifi_mode:
        #         subprocess.run(["networksetup", "-setairportpower", "en0", "on"])
        #     else:
        #         subprocess.run(["networksetup", "-setairportpower", "en0", "off"])

        import requests
        from requests.auth import HTTPBasicAuth
        session = self.driver.session_id
        logging.info(session)
        api_endpoint_wifi = f"https://api-cloud.browserstack.com/app-automate/sessions/{session}/update_network.json"
        payload = {
            "networkProfile": "no-network"
        }
        if wifi_mode:
            payload = {
                "networkProfile": "reset"
            }
        my_username = "anjanikumar_4El02x"
        my_password = "1eoGzmuph1dimfFRWP4k"
        try:
            response = requests.put(api_endpoint_wifi, json=payload, headers={'Content-Type': 'application/json', 'Accept': 'application/json'}
                                    , auth=HTTPBasicAuth(my_username, my_password))
            if response.status_code == 200 or response.status_code == 204:
                logging.getLogger("root").info(f"response status code : {response.status_code}")
            else:
                logging.getLogger("root").info(f"Failed to retrieve data: {response.status_code}")
        except requests.exceptions.RequestException as e:
            logging.getLogger("root").error(f"API call failed: {e}")

    def verify_no_connection_message(self):
        element = self.get_element(self.locators[self.platform]['no_connection_text'])
        if element:
            return element.text
        else:
            logging.getLogger("root").error("No connection message is not appear")
            return None

    def verify_packages_displayed_after_internet_connection(self):
        self.ElementPresent_and_click(self.locators[self.platform]['refresh_btn'])
        time.sleep(7)
        # self.isElementPresent(self.locators[self.platform]['package_text'])

    def assert_driver_id_and_password_field(self):
        self.isElementPresent(self.locators[self.platform]['driver_id_text_bar'])

    def assert_and_select_terms_and_conditions(self):
        self.scroll_fixed_steps(steps=2)
        time.sleep(5)
        self.scroll_fixed_steps(steps=2)
        self.isElementPresent(self.locators[self.platform]['by_using_our_app_TermsAndConditions_Lable'])
        self.ElementPresent_and_click(self.locators[self.platform]['check_box_termAndConditions'])

    def click_and_print_context(self):
        self.scroll_fixed_steps(steps=2)
        # self.ElementPresent_and_click(self.locators[self.platform]['by_using_our_app_TermsAndConditions_Lable'])
        element = self.get_element(self.locators[self.platform]['by_using_our_app_TermsAndConditions_Lable'])
        self.isElementPresent(self.locators[self.platform]["terms_and_conditions_text"])
        location = element.location
        size = element.size
        x_center = location['x'] + (size['width']-1)
        y_center = location['y'] + size['height']-1
        #os.system(f"adb shell input tap {int((location['x'] + size['width'] ))-1} {int(y_center)}")
        actions = ActionChains(self.driver)
        time.sleep(5)
        actions = ActionChains(self.driver)
        time.sleep(5)
        touch_input = PointerInput(interaction.POINTER_TOUCH, "touch")
        actions.w3c_actions.devices.append(touch_input)
        actions.w3c_actions.pointer_action.move_to_location(x_center,y_center).click()
        actions.perform()
        time.sleep(7)
        self.isElementPresent(self.locators[self.platform]["ontrac_logo"])
        logging.getLogger("root").info("Navigated successfully to terms and conditions page")


    def click_and_print_context_3829(self):
        # self.ElementPresent_and_click(self.locators[self.platform]['by_using_our_app_TermsAndConditions_Lable'])
        # self.isElementPresent(self.locators[self.platform]["ontrac_logo"])
        # logging.getLogger("root").info("Navigated successfully to privacy policy page")
        self.scroll_fixed_steps(steps=2)
        time.sleep(5)
        self.scroll_fixed_steps(steps=2)
        element = self.get_element(self.locators[self.platform]['by_using_our_app_TermsAndConditions_Lable'])
        self.isElementPresent(self.locators[self.platform]["terms_and_conditions_text"])
        location = element.location
        size = element.size
        x_center = location['x'] + (size['width'] - 1)
        y_center = location['y'] + size['height'] - 1
        #os.system(f"adb shell input tap {int((location['x'] + size['width'])) - 1} {int(y_center)}")
        actions = ActionChains(self.driver)
        time.sleep(5)
        actions = ActionChains(self.driver)
        time.sleep(5)
        touch_input = PointerInput(interaction.POINTER_TOUCH, "touch")
        actions.w3c_actions.devices.append(touch_input)
        actions.w3c_actions.pointer_action.move_to_location(x_center, y_center).click()
        actions.perform()
        time.sleep(7)
        self.isElementPresent(self.locators[self.platform]["ontrac_logo"])
        logging.getLogger("root").info("Navigated successfully to terms and conditions page")

    def toggle_network_modes_10125(self, wifi_mode: bool, mobile_data_mode: bool):

        try:
            # Toggle Wi-Fi
            wifi_command = 'enable' if wifi_mode else 'disable'
            wifi_result = subprocess.run(['adb', 'shell', 'svc', 'wifi', wifi_command], check=True, text=True,
                                         capture_output=True)


            # Toggle Mobile Data
            mobile_data_command = 'enable' if mobile_data_mode else 'disable'
            mobile_data_result = subprocess.run(['adb', 'shell', 'svc', 'data', mobile_data_command], check=True,
                                                text=True, capture_output=True)


        except subprocess.CalledProcessError as e:
            logging.error(f"Error executing adb command: {e.stderr}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")



    def android_only(self,text_1,text_2,text_3,text_4):
        self.click_on_skip_element()
        time.sleep(1)
        element_1 = self.get_element(self.locators[self.platform]['accept_1_text_1']).text
        assert element_1 == text_1
        element_2 = self.get_element(self.locators[self.platform]['accept_1_text_2']).text
        assert element_2 == text_2
        self.ElementPresent_and_click(self.locators[self.platform]['accept_btn_1'])
        time.sleep(2)
        element_3 = self.get_element(self.locators[self.platform]['accept_2_text_1']).text
        assert element_3 == text_3
        element_4 = self.get_element(self.locators[self.platform]['accept_2_text_2']).text
        assert element_4 == text_4
        self.ElementPresent_and_click(self.locators[self.platform]['accept_btn_2'])

    def checking_screen_after_relaunch(self):

        assert self.isElementPresent(self.locators[self.platform]['screen_after_close_and_re_launch_app'])

    def verify_login(self):
        WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(self.locators[self.platform]['landing_page']))
        assert self.isElementPresent(self.locators[self.platform]['landing_page']) , 'unable to login successfully'


    def fill_login_form_and_submit(self, driver_id, password):
        time.sleep(5)
        driver_id_locator = self.locators[self.platform]['driver_id_text_bar']
        self.clear_field(driver_id_locator)
        self.send_keys_to(driver_id_locator, driver_id)
        check_box_term_and_conditions_locator = self.locators[self.platform]['check_box_termAndConditions']
        self.ElementPresent_and_click(check_box_term_and_conditions_locator)
        submit_btn_locator = self.locators[self.platform]['login_btn']
        self.ElementPresent_and_click(submit_btn_locator)
        email_code_locator = self.locators[self.platform]['code_text_bar']
        time.sleep(5)
        self.clear_field(email_code_locator)
        # Handle the driver logged-in issue
        try:
            assert self.get_element(email_code_locator)
        except Exception:
            i = 1
            if driver_id.upper() not in ['ORLAQADRV02', 'NASHQADRV02', 'ASHDQADRV02', 'CLVDQADRV02']:
                while i <= 10:
                    driver_id = driver_id + str(i)
                    self.clear_field(driver_id_locator)
                    self.send_keys_to(driver_id_locator, driver_id)
                    self.ElementPresent_and_click(submit_btn_locator)
                    try:
                        assert self.get_element(email_code_locator)
                        break
                    except Exception as e:
                        i = i + 1
        # Handle the driver logged-in issue
        self.send_keys_to(email_code_locator, password)
        self.ElementPresent_and_click(submit_btn_locator)

    def verify_wrong_email_code(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators[self.platform]['wrong_email_sent_code_message']))
        assert self.isElementPresent(self.locators[self.platform]['wrong_email_sent_code_message']), 'unable to login successfully'

    def verify_test_login_in_offline_mode(self,driver_id):
        driver_id_locator = self.locators[self.platform]['driver_id_text_bar']
        self.clear_field(driver_id_locator)
        self.send_keys_to(driver_id_locator, driver_id)
        time.sleep(2)
        try:
            self.driver.find_element(AppiumBy.XPATH, '(//*)[1]').send_keys(Keys.RETURN)
        except NoSuchElementException:
            logging.info("The keyboard screen didn't appear.")
        time.sleep(2)
        self.scroll_fixed_steps(steps=2)
        self.ElementPresent_and_click(self.locators[self.platform]['check_box_termAndConditions'])
        self.scroll_fixed_steps(steps=2)
        self.ElementPresent_and_click(self.locators[self.platform]['login_btn'])
        time.sleep(5)
        self.verify_login()

    def verify_RSP_and_Facility_choosers_are_not_appeared(self,verification_code):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.locators[self.platform]['relogin_pop_validation_code_field']))
        assert self.isElementPresent(
            self.locators[self.platform]['relogin_pop_validation_code_field']), 'Re-Login popup message was not appeared'
        self.clear_field(self.locators[self.platform]['relogin_pop_validation_code_field'])
        self.send_keys_to(self.locators[self.platform]['relogin_pop_validation_code_field'], verification_code)
        self.ElementPresent_and_click(self.locators[self.platform]['relogin_pop_up_submit_button'])
        time.sleep(5)
        try:
            RSP_locator=self.locators[self.platform]['ontrac_driver_id']
            locator_type = RSP_locator[0]
            locator_value = RSP_locator[1]
            by_type = self.get_by_type(locator_type)
            self.driver.find_element(by_type,locator_value).click()
            assert False , 'RSP Screen is present'
        except Exception as e:
            pass
        try:
            Facility_chooser_locator=self.locators[self.platform]['Facility_choose_screen']
            locator_type = Facility_chooser_locator[0]
            locator_value = Facility_chooser_locator[1]
            by_type = self.get_by_type(locator_type)
            self.driver.find_element(by_type,locator_value).click()
            assert False , 'Facility choosing Screen is present'
        except Exception as e:
            pass

    def verify_RSP_screen_Facility_screen(self,driver_id,password):
        time.sleep(5)
        assert self.isElementPresent(self.locators[self.platform]['main_login_screem'])
        driver_id_locator = self.locators[self.platform]['driver_id_text_bar']
        self.clear_field(driver_id_locator)
        self.send_keys_to(driver_id_locator, driver_id)
        time.sleep(2)
        try:
            self.driver.find_element(AppiumBy.XPATH, '(//*)[1]').send_keys(Keys.RETURN)
        except NoSuchElementException:
            logging.info("The keyboard screen didn't appear.")
        time.sleep(2)
        self.scroll_fixed_steps(steps=2)
        check_box_term_and_conditions_locator = self.locators[self.platform]['check_box_termAndConditions']
        self.ElementPresent_and_click(check_box_term_and_conditions_locator)
        self.scroll_fixed_steps(steps=2)
        submit_btn_locator = self.locators[self.platform]['login_btn']
        self.ElementPresent_and_click(submit_btn_locator)
        assert self.isElementPresent(self.locators[self.platform]['code_text_bar'])
        email_code_locator = self.locators[self.platform]['code_text_bar']
        time.sleep(5)
        self.clear_field(email_code_locator)
        # Handle the driver logged-in issue
        try:
            assert self.get_element(email_code_locator)
        except Exception:
            i = 1
            if driver_id.upper() not in ['ORLAQADRV02', 'NASHQADRV02', 'ASHDQADRV02', 'CLVDQADRV02']:
                while i <= 10:
                    driver_id = driver_id + str(i)
                    self.clear_field(driver_id_locator)
                    self.send_keys_to(driver_id_locator, driver_id)
                    self.ElementPresent_and_click(submit_btn_locator)
                    try:
                        assert self.get_element(email_code_locator)
                        break
                    except Exception as e:
                        i = i + 1
        #Handle the driver logged-in issue
        self.send_keys_to(email_code_locator, password)
        if self.driver.capabilities['platformName'].lower() == 'android':
            self.ElementPresent_and_click(submit_btn_locator)
        if self.driver.capabilities['platformName'].lower() == 'ios':
            self.ElementPresent_and_click(self.locators[self.platform]['send_code_btn'])
        time.sleep(5)
        self.ElementPresent_and_click(self.locators[self.platform]['ontrac_driver_id'])
        self.isElementPresent(self.locators[self.platform]['select_RSP_heading'])
        self.ElementPresent_and_click(self.locators[self.platform]['next_btn'])
        if self.driver.capabilities['platformName'].lower() == 'ios':
            self.ElementPresent_and_click(self.locators[self.platform]['select_facility'])
        self.isElementPresent(self.locators[self.platform]['select_facility_heading'])
        login_result = self.ElementPresent_and_click(self.locators[self.platform]['next_btn'])
        time.sleep(5)
        assert login_result, 'Failed to login to OnRoute'

    def scroll_fixed_steps(self, steps=1):
        try:
            scrollable_ui = f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollForward({steps})'
            self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scrollable_ui)
            logging.getLogger("root").info(f"Scrolled {steps} steps.")
        except NoSuchElementException:
            logging.getLogger("root").info(f"Not scrolled {steps} steps.")

    def verify_user_should_not_be_able_to_login(self,driver_id,message_to_validate_user,spanish_message_to_validate_user,logging):
        time.sleep(5)
        driver_id_locator = self.locators[self.platform]['driver_id_text_bar']
        self.clear_field(driver_id_locator)
        self.send_keys_to(driver_id_locator, driver_id)
        check_box_term_and_conditions_locator = self.locators[self.platform]['check_box_termAndConditions']
        self.ElementPresent_and_click(check_box_term_and_conditions_locator)
        submit_btn_locator = self.locators[self.platform]['login_btn']
        self.ElementPresent_and_click(submit_btn_locator)
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(self.locators[self.platform]["user_is_already_logged_out"]))
        text0=self.get_element(self.locators[self.platform]["user_is_already_logged_out"]).text
        assert text0 == message_to_validate_user
        time.sleep(5)
        self.click_on_element(self.locators[self.platform]['language_lable'])
        self.click_on_element(self.locators[self.platform]["Español_language"])
        time.sleep(3)
        self.clear_field(driver_id_locator)
        self.send_keys_to(driver_id_locator, driver_id)
        submit_btn_locator = self.locators[self.platform]['login_btn']
        self.ElementPresent_and_click(submit_btn_locator)
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(self.locators[self.platform]["user_is_already_logged_out"]))
        text1=self.get_element(self.locators[self.platform]["user_is_already_logged_out"]).text
        assert text1 == spanish_message_to_validate_user

    def change_language(self, language='spanish'):
        self.ElementPresent_and_click(self.locators[self.platform]['login_page_settings'])
        self.ElementPresent_and_click(self.locators[self.platform]['login_page_language_option'])
        if language == 'spanish':
            self.ElementPresent_and_click(self.locators[self.platform]['spanish_language'])
        else:
            self.ElementPresent_and_click(self.locators[self.platform]['english_language'])
        self.ElementPresent_and_click(self.locators[self.platform]['language_back_button'])
        time.sleep(5)
        self.ElementPresent_and_click(self.locators[self.platform]['language_back_button'])


