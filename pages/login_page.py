from playwright.sync_api import Page

class LoginPage:
    def __init__(self,browsertab:Page):
        #self.page = browsertab stores the Playwright browser tab in LoginPage object,
        # so its methods can access and interact with the elements on that tab.
        #self is the LoginPage object; self.page refers to the Playwright browser tab stored inside it.
        self.page = browsertab
        
        #Locators
        self.username = browsertab.get_by_placeholder("Username")
        self.password = browsertab.get_by_placeholder("Password")
        self.login_btn = browsertab.locator('//input[@name="login-button"]')
        self.validation_message = browsertab.locator('//h3[@data-test="error"]')
    
    #Actions
    def enter_username(self, username):
        self.username.fill(username)
     
    def enter_password(self,password):
        self.password.fill(password)    
        
    def login(self):
        self.login_btn.click()