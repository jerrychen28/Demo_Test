# coding=utf-8

import sys

sys.path.append("d:\\Test\\pythonProject\\new\\BaseOp")

import basepage
from selenium.webdriver.common.by import By


class TargetWeb(basepage.BasePage):
    contact_tab = (By.LINK_TEXT, "Contact")
    shop_tab = (By.LINK_TEXT, "Shop")

    contact_tab_submit_button = (By.LINK_TEXT, "Submit")
    contact_tab_forename_box = (By.ID, "forename")
    contact_tab_email_box = (By.ID, "email")
    contact_tab_message_box = (By.ID, "message")
    contact_success_back_button = (By.LINK_TEXT, "« Back")

    stuffed_frog_buy = (By.CSS_SELECTOR, "#product-2>div>p>a")
    fluffy_bunny_buy = (By.CSS_SELECTOR, "#product-4>div>p>a")
    valentine_bear_buy = (By.CSS_SELECTOR, "#product-7>div>p>a")

    cart_icon = (By.CSS_SELECTOR, "li#nav-cart>a")

    def click_contact_tab(self):
        self.click_on(*self.contact_tab)

    def click_contact_tab_submit_button(self):
        self.click_on(*self.contact_tab_submit_button)
        self.sleep(30)

    def type_contact_tab_forename_box(self, text):
        self.type(text, *self.contact_tab_forename_box)

    def type_contact_tab_email_box(self, text):
        self.type(text, *self.contact_tab_email_box)

    def type_contact_tab_message_box(self, text):
        self.type(text, *self.contact_tab_message_box)

    def click_contact_success_back(self):
        self.click_on(*self.contact_success_back_button)
        self.sleep(5)

    def click_shop_tab(self):
        self.click_on(*self.shop_tab)

    def click_stuffed_frog_buy(self):
        self.click_on(*self.stuffed_frog_buy)

    def click_fluffy_bunny_buy(self):
        self.click_on(*self.fluffy_bunny_buy)

    def click_valentine_bear_buy(self):
        self.click_on(*self.valentine_bear_buy)

    def click_cart_icon(self):
        self.click_on(*self.cart_icon)





