class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://example.com')

    def get_title(self):
        return self.driver.title
