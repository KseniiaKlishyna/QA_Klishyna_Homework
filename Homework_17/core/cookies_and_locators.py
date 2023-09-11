class Cookies:
    def __init__(self, driver):
        self.driver = driver

    def set_cookie(self, name, value):
        self.driver.add_cookie({'name': name, 'value': value})

    def get_cookie(self, name):
        return self.driver.get_cookie(name)


class LocalStorage:
    def __init__(self, driver):
        self.driver = driver

    def set_item(self, key, value):
        self.driver.execute_script(f'localStorage.setItem("{key}", "{value}");')

    def get_item(self, key):
        return self.driver.execute_script(f'return localStorage.getItem("{key}");')

    def remove_item(self, key):
        self.driver.execute_script(f'localStorage.removeItem("{key}");')