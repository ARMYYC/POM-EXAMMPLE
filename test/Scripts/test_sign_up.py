import time

from src.PageObject.Pages import HomePage
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import HomePage


class Test_course_pack(WebDriverSetup):

    def test_add_item_to_course_pack(self):
        driver = self.driver
        self.driver.get(HomePage.get_base_url())
        home_page = HomePage(driver)
        time.sleep(3)
        home_page.wikipedia("hola")
        home_page.sign_up("Armando", "Cardenas")
        home_page.sundaychek()
        home_page.click_country_up()
        time.sleep(3)





