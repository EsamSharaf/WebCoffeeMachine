from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MySeleniumTests(StaticLiveServerTestCase):
    fixtures = ["drinks.json"]

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_e2e(self):
        # open the app
        self.selenium.get(f"{self.live_server_url}/coffeemachine/")
        # select a drink from a list of drink
        self.selenium.find_element(
            "xpath", '//a[@href="/coffeemachine/Cappuccino/"]').click()
        # click on + button in drink page to set quantity
        WebDriverWait(self.selenium, 20).until(EC.presence_of_element_located((
            By.ID, "plus-butn"))).click()
        # find the Pay Now buttin
        self.selenium.find_element(By.ID, "pay-btn").click()
        # wait until the order is completed
        WebDriverWait(self.selenium, 20).until(
            EC.text_to_be_present_in_element((By.ID, "overlay-text"),
                                             'Order completed!'))
        overlay_text = self.selenium.find_element(By.ID, "overlay-text")

        assert "Order completed!" in overlay_text.get_attribute("textContent")

        # click on Home Page button to return to the land page
        WebDriverWait(self.selenium, 20).until(
            EC.text_to_be_present_in_element((By.ID, "overlay-homeBtn"),
                                             'Home Page'))

        self.selenium.find_element(By.ID, "overlay-homeBtn").click()
