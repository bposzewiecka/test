from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your tests here.
class PlayerFormTest(LiveServerTestCase):

  def testform(self):
    selenium = webdriver.Firefox()
    #Choose your url to visit
    selenium.get('http://127.0.0.1:8000/admin/login')

    name = selenium.find_element_by_id('id_username')
    name.send_keys('root')

    password = selenium.find_element_by_id('id_password')
    password.send_keys('root')

    submit = selenium.find_element_by_css_selector(".submit-row > input")

    submit.click()

