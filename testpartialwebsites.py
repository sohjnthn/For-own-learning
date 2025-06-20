from selenium import webdriver
from selenium.webdriver.common.by import By

from datetime import datetime

from selenium.webdriver.common.utils import Keys

from hellocucumber.hellocucumberpython.testpartialapps import test_if_websites_can_call_apps

import os

from hellocucumber.hellocucumberpython.testfirstgroupofwebsites import test_first_group_of_websites
from hellocucumber.hellocucumberpython.testsecondgroupofwebsites import test_second_group_of_websites
from hellocucumber.hellocucumberpython.testthirdgroupofwebsites import test_third_group_of_websites


def test_if_websites_can_be_split():
    driver1 = webdriver.Chrome()
    test_first_group_of_websites(driver1)
    test_second_group_of_websites(driver1)
    test_third_group_of_websites(driver1)
    # Only for executing testpartialapps.py
    test_if_websites_can_call_apps()
