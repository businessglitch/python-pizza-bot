import pdb
import secrets
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PizzaBot:
    def __init__(self):
        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('https://www.pizzahut.ca/home')

    def enter_delivery_address(self):
        self.wait(
            '//*[@id="zipCode"]').send_keys(secrets.postal_code)

        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div/div[1]/form/button').click()

        self.wait('//*[@id="streetNumber"]').send_keys(secrets.street_number)

        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div[1]/div/div/div[1]/div/div/div/div[2]/form/button').click()

    def add_items_to_cart(self):
        self.wait(
            '/html/body/div[1]/div[2]/div/div[2]/div/div[2]/ul/li[11]/div/div/button').click()
        try:
            self.wait(
                '/html/body/div[1]/div/div/upsell/ng-include/div/div[1]').click()
        except:
            pass

    def navigate_to_checkout(self):
        self.driver.find_element_by_xpath('//*[@id="mini-cart-icon"]').click()
        self.wait(
            '/html/body/div[1]/div[3]/div[2]/div/div[2]/div/button').click()

    def fill_checkout_form(self):
        # Name form
        self.wait(
            '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/input').send_keys(secrets.first_name)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/div[2]/div[2]/div[2]/div/div[2]/input').send_keys(secrets.last_name)

        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/div[2]/div[3]/div/div[2]/input').send_keys(secrets.email)

        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/div[2]/div[4]/div/div/div[2]/input').send_keys(secrets.phone_number)

        # Delivery Instructions
        self.wait('/html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/div[4]/div[3]/div/div/div[2]/input').send_keys(
            'Please give me a call when you are outside. NOTE TO CHEF: Please write "PYTHON" on the pizza :)')

        # Change payment method
        self.driver.find_element_by_xpath(
            '//*[@id="payTypeCategory_label"]/span[2]').click()

        # Click proceeed payment
        time.sleep(3)
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[3]/button').click()

        '''Credit Card information form'''
        # Credit Card Name
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div[2]/input").send_keys(secrets.fullname)

        # Credit Card Number
        self.driver.find_element_by_xpath(
            "/ html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/input").send_keys(secrets.card_number)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[3]/div/div[2]/input").send_keys(secrets.card_cvv)

        # Set Month
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/a').click()
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[2]/div/div/ul/li[{}]'.format(secrets.card_month)).click()

        # Set Year
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/a").click()
        self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/ul/li[{}]'.format(secrets.card_year)).click()

        # Billing same as delivery
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/div[2]/div/div/div/div/div[3]/div[2]/div/div/input").click()

        #  Set tip amount
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/div/div/form/div/div/div[2]/div/div[2]/div/div/div/div/div[4]/div[2]/div/div[4]/div/label/span[2]").click()           

        # click pay button
        self.driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/form/div/div/div[3]/div/button").click()

    def takes_screenshot(self, name):
        self.driver.save_screenshot("{}.png".format(name))


    def place_order(self):
        self.enter_delivery_address()
        self.add_items_to_cart()
        self.navigate_to_checkout()
        self.fill_checkout_form()
        time.sleep(7)
        self.takes_screenshot('confirmation')

    def wait(self, path):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, path)))

p = PizzaBot()

