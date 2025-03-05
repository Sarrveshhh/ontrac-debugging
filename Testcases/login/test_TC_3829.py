import logging
from ElliPageObjects.login_page import ElliLoginPage
import pytest
from Utilities.read_properties import read_json_file
from Utilities.common_util import LOGIN_PATH


class Test_TC_3829:
    login_data = read_json_file(LOGIN_PATH)

    # @pytest.mark.android
    # @pytest.mark.ios
    # @pytest.mark.no_driver_1
    @pytest.mark.xdist_group("train_driver2")
    # no driver required so running on real_driver thread
    def test_Login_TC_3829_Launch_elli_application(self, appium_driver_setup):
        logging.getLogger("root").info("Starting test_login_list_options")
        elli_login_page = ElliLoginPage(appium_driver_setup)
        elli_login_page.perform_initial_actions()
        elli_login_page.fill_and_submit_form(self.login_data["sequence_url"], self.login_data["events_url"])
        logging.getLogger("root").info("Changing to stages Successfully")
        # elli_login_page.assert_driver_id_and_password_field()
        # elli_login_page.assert_and_select_terms_and_conditions()
        # elli_login_page.click_and_print_context_3829()
        logging.getLogger("root").info("Ending test_launch_elli_application")
