import logging
from ElliPageObjects.login_page import ElliLoginPage
from Utilities.common_util import LOGIN_PATH
from Utilities.read_properties import read_json_file
import pytest


class Test_TC_3831:
    login_data = read_json_file(LOGIN_PATH)


    @pytest.mark.android
    @pytest.mark.ios
    @pytest.mark.no_driver_1
    @pytest.mark.skip(reason="Needs blocked road")
    # @pytest.mark.xdist_group("train_driver2")
    def test_Login_TC_3831_Checking_language_change_functionality(self, appium_driver_setup):
        logging.getLogger("root").info("Starting test_login_with_spanish_language")
        elli_login_page = ElliLoginPage(appium_driver_setup)
        elli_login_page.perform_initial_actions()
        elli_login_page.fill_and_submit_form(self.login_data['sequence_url'], self.login_data['events_url'])
        logging.getLogger("root").info("Changing to stages Successfully")
        elli_login_page.click_on_language_button()
        logging.getLogger("root").info("Language pop-up open Successfully")
        elli_login_page.click_on_english_language()
        logging.getLogger("root").info("Language changed to English Successfully")
        elli_login_page.click_on_language_button()
        elli_login_page.click_on_espanol_language()
        logging.getLogger("root").info("Language changed to Espanol Successfully")
        elli_login_page.assert_spanish_language_elements_visible()
        logging.getLogger("root").info("Ending test_login_with_spanish_language")



