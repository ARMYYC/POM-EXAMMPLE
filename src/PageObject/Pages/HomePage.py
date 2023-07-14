import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

base_url = "https://testautomationpractice.blogspot.com/"


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wikipedia_search = "//*[@id='Wikipedia1_wikipedia-search-input']"
        self.date_picker = "datepicker"
        self.speed = "speed"
        self.sunday = "sunday"
        self.monday = "RESULT_CheckBox-8_1"
        self.tuesday = "RESULT_CheckBox-8_2"
        self.field1 = "field1"
        self.field2 = "field2"
        self.iframe_sign_up = "frame-one1434677811"
        self.first_name = "name"
        self.last_name = "RESULT_TextField-2"
        self.phone = "phone"
        self.country = "country"
        self.city = "RESULT_TextField-5"
        self.email = "email"
        self.gender_male = "RESULT_RadioButton-7_0"
        self.gender_female = "RESULT_RadioButton-7_1"
        self.submit_button = "FSsubmit"
        

    def get_wikipedia_search(self):
        return self.driver.find_element(By.XPATH, self.wikipedia_search)

    def get_date_picker(self):
        return self.driver.find_element(By.ID, self.date_picker)

    def get_speed(self):
        return self.driver.find_element(By.ID, self.speed)

    def get_sunday(self):
        return self.driver.find_element(By.ID, self.sunday)

    def get_monday(self):
        return self.driver.find_element(By.ID, self.monday)

    def get_tuesday(self):
        return self.driver.find_element(By.ID, self.tuesday)

    def get_field1(self):
        return self.driver.find_element(By.ID, self.field1)

    def get_field2(self):
        return self.driver.find_element(By.ID, self.field2)

    def get_iframe_sign_up(self):
        return self.driver.find_element(By.ID, self.iframe_sign_up)

    def get_first_name(self):
        return self.driver.find_element(By.ID, self.first_name)

    def get_last_name(self):
        return self.driver.find_element(By.ID, self.last_name)

    def get_phone(self):
        return self.driver.find_element(By.ID, self.phone)

    def get_country(self):
        return self.driver.find_element(By.ID, self.country)

    def get_city(self):
        return self.driver.find_element(By.ID, self.city)

    def get_email(self):
        return self.driver.find_element(By.ID, self.email)

    def get_gender_male(self):
        return self.driver.find_element(By.ID, self.gender_male)

    def get_gender_female(self):
        return self.driver.find_element(By.ID, self.gender_female)

    def get_submit_button(self):
        return self.driver.find_element(By.ID, self.submit_button)



    def wikipedia(self, wikipedia_search):
        self.get_wikipedia_search().send_keys(wikipedia_search)

    def sundaychek(self):
        self.get_sunday().click()


    def sign_up(self, first_name, email):
        #self.switch_to_iframe()
        self.get_first_name().send_keys(first_name)
        #self.get_last_name().send_keys(last_name)
        #self.get_phone().send_keys(phone)
        #self.get_country().send_keys(country)
        #self.get_city().send_keys(city)
        self.get_email().send_keys(email)
        time.sleep(3)

    def click_sing_up(self):
        self.get_submit_button().click()

    def click_country(self):
        select_file = Select(self.find_element(By.ID,'country'))
        select_file.select_by_value('usa')
    
    def click_country_up(self):
        self.get_country().click()
    

    def switch_to_iframe(self):
        iframe = self.get_iframe_sign_up()
        self.driver.switch_to.frame(iframe)

    @staticmethod
    def get_base_url():
        return base_url
