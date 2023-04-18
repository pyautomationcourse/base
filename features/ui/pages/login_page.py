class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://example.com/login')

    def login(self, username, password):
        username_input = self.driver.find_element_by_name('username')
        password_input = self.driver.find_element_by_name('password')
        submit_button = self.driver.find_element_by_name('submit')

        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.click()
