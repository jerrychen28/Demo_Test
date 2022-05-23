# coding=utf-8

import sys

sys.path.append("d:\\Test\\pythonProject\\new\\logger")
sys.path.append("d:\\Test\\pythonProject\\new\\BaseOp")
sys.path.append("d:\\Test\\pythonProject\\new\\BrowserEngine")
sys.path.append("d:\\Test\\pythonProject\\new\\pageobjects")
sys.path.append("d:\\Test\\pythonProject\\new\\data_for_test")

import unittest
import browser_engine
import target_web_action
import logger
import basepage
import read_excel
from selenium.webdriver.common.by import By
from ddt import ddt, data, unpack


@ddt
class JupiterToys(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        browse = browser_engine.BrowserEngine()
        self.driver = browse.open_browser()
        self.log = logger.Logger().get_log()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    def test_case_contact1(self):
        tar_act = target_web_action.TargetWeb(self.driver)

        # click contact tab:
        tar_act.click_contact_tab()

        # test going correctly to contact page or not:
        contact_tab_forename_box = (By.ID, "forename")
        att = basepage.BasePage(self.driver).find_element(*contact_tab_forename_box).get_attribute("placeholder")
        try:
            self.assertEqual(str(att), "John")
            self.log.info("Already entered into the contact page")
        except Exception as e:
            self.log.critical("Test fail to enter into the contact page. %s" % format(e))
            basepage.BasePage(self.driver).get_screen_image()
        basepage.BasePage(self.driver).sleep(3)

        # Then test directly clicking the submit button:
        tar_act.click_contact_tab_submit_button()
        alert_box = (By.CSS_SELECTOR, "div.alert-error>strong")
        alert_message = basepage.BasePage(self.driver).find_element(*alert_box).text
        try:
            self.assertIn("We welcome your feedback", alert_message)
            self.log.info("Alert message pass after directly clicking submit button")
        except Exception as e:
            self.log.critical("Alert message isn't correct after directly clicking submit button. %s" % format(e))
            basepage.BasePage(self.driver).get_screen_image()

        # Then test populating the mandatory fields, then clicking the submit button:
        tar_act.type_contact_tab_forename_box("Jerry")
        tar_act.type_contact_tab_email_box("jerry.xin.chen1@gmail.com")
        tar_act.type_contact_tab_message_box("Good product.")
        tar_act.click_contact_tab_submit_button()
        message_box = (By.CSS_SELECTOR, "div.alert-success>strong")
        alert_message = basepage.BasePage(self.driver).find_element(*message_box).text
        try:
            self.assertIn("Thanks", alert_message)
            self.log.info("Success message shown pass after entering mandatory fields and submitting")
        except Exception as e:
            self.log.critical("Success message shown incorrectly after entering mandatory fields and submitting. %s" % format(e))
            basepage.BasePage(self.driver).get_screen_image()
        tar_act.click_contact_success_back()


    @data(*read_excel.get_excel())
    @unpack
    def test_case_contact2(self, forename, email, message):
        tar_act = target_web_action.TargetWeb(self.driver)
        tar_act.type_contact_tab_forename_box(forename)
        tar_act.type_contact_tab_email_box(email)
        tar_act.type_contact_tab_message_box(message)
        tar_act.click_contact_tab_submit_button()
        message_box = (By.CSS_SELECTOR, "div.alert-success>strong")
        alert_message = basepage.BasePage(self.driver).find_element(*message_box).text
        try:
            self.assertIn("Thanks", alert_message)
            self.log.info("Success message shown pass after entering mandatory fields and submitting")
        except Exception as e:
            self.log.critical("Success message shown incorrectly after entering mandatory fields and submitting. %s" % format(e))
            basepage.BasePage(self.driver).get_screen_image()
        tar_act.click_contact_success_back()


    def test_case_cart(self):
        # click shop tab:
        tar_act = target_web_action.TargetWeb(self.driver)
        tar_act.click_shop_tab()

        # test going correctly to product page or not:
        stuffed_frog = (By.CSS_SELECTOR, "#product-2>div>h4")
        att = basepage.BasePage(self.driver).find_element(*stuffed_frog).text
        try:
            self.assertEqual(att, "Stuffed Frog")
            self.log.info("Already entered into the product page")
        except Exception as e:
            self.log.critical("Test fail to enter into the product page. %s" % format(e))

        # Then adding certain quantity products into cart according to the test scenario:
        for i in range(0,2):
            tar_act.click_stuffed_frog_buy()
            basepage.BasePage(self.driver).sleep(1)
        for i in range(0,5):
            tar_act.click_fluffy_bunny_buy()
            basepage.BasePage(self.driver).sleep(1)
        for i in range(0,3):
            tar_act.click_valentine_bear_buy()
            basepage.BasePage(self.driver).sleep(1)

        # Then go to cart page and test:
        tar_act.click_cart_icon()

        # Check total price, each product price and subtotal price:

        expected_perchased_product = ["Stuffed Frog", "Fluffy Bunny", "Valentine Bear"]
        expected_product_price = [10.99, 9.99, 14.99]
        purchased_quantity = [2, 5, 3]

        for i in range(1, 4):
            element = "//tr[%s]/td[1]" % i
            real_cart_product_name = basepage.BasePage(self.driver).find_element(*(By.XPATH, element)).text
            try:
                self.assertEqual(expected_perchased_product[i-1], real_cart_product_name)
                self.log.info("Each product name is correct")
            except Exception as e:
                self.log.critical("Some of the product names are incorrect. %s" % format(e))
                basepage.BasePage(self.driver).get_screen_image()
            element = "//tr[%s]/td[2]" % i
            real_cart_product_price = basepage.BasePage(self.driver).find_element(*(By.XPATH, element)).text
            try:
                self.assertIn(str(expected_product_price[i-1]), real_cart_product_price)
                self.log.info("Each product price is correct")
            except Exception as e:
                self.log.critical("Some of the product prices are incorrect. %s" % format(e))
                basepage.BasePage(self.driver).get_screen_image()
            element = "//tr[%s]/td[4]" % i
            real_cart_product_subtotal_price = basepage.BasePage(self.driver).find_element(*(By.XPATH, element)).text
            try:
                self.assertIn(str(expected_product_price[i-1]*purchased_quantity[i-1]), real_cart_product_subtotal_price)
                self.log.info("Each product subtotal price is correct")
            except Exception as e:
                self.log.critical("Some of the product subtotal prices are incorrect. %s" % format(e))
                basepage.BasePage(self.driver).get_screen_image()

        expected_total = 0
        for i in range(0,3):
            expected_total = expected_total + expected_product_price[i] * purchased_quantity[i]

        total_loc = (By.CSS_SELECTOR, "strong.total")
        real_total = basepage.BasePage(self.driver).find_element(*total_loc).text
        try:
            self.assertIn(str(expected_total), real_total)
            self.log.info("Total price is correct")
        except Exception as e:
            self.log.critical("Total price is incorrect and test fail. %s" % format(e))
            basepage.BasePage(self.driver).get_screen_image()

























