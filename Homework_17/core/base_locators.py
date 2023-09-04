class BaseLocators:
    def __init__(self):
        self.overlay_locator = ('css selector', '.onetrust-pc-dark-filter')
        self.close_button_locator = ('xpath', "//button[@id='onetrust-accept-btn-handler']")