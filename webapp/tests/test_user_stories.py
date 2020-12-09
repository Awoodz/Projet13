from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MySeleniumTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--no-default-browser-check")
        chrome_options.add_argument("--no-first-run")
        chrome_options.add_argument("--disable-default-apps")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--headless")
        super().setUpClass()
        cls.selenium = Chrome(options=chrome_options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_user_can_signup_then_login(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/accounts/signup/"))
        self.selenium.set_window_size(1440, 900)
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys("testuser")
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys("testuser@mail.com")
        password_input = self.selenium.find_element_by_name("password1")
        password_input.send_keys("Testpass1")
        password_input = self.selenium.find_element_by_name("password2")
        password_input.send_keys("Testpass1")
        self.selenium.find_element_by_xpath('//button[@value="signup"]').click()

        WebDriverWait(self.selenium, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "login_body"))
        )
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys("testuser")
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys("Testpass1")
        self.selenium.find_element_by_xpath('//button[@value="login"]').click()
        WebDriverWait(self.selenium, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "block"))
        )
        assert self.selenium.current_url == self.live_server_url + "/"
