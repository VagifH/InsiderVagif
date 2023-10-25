from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from elements.InsiderCareerPOM import import InsiderCareerPOM

class Insider:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # Initialize WebDriverWait

    def open_home_page(self):
        self.driver.get(InsiderCareerPOM .URL)

    def is_home_page_opened(self):
        return "#1 Leader in Individualized, Cross-Channel CX — Insider" in self.driver.title

    def navigate_to_careers(self):
        careers_link = self.wait.until(EC.element_to_be_clickable(InsiderCareerPOM .careers_submenu))
        careers_link.click()

    def open_careers_page(self):
        careers_submenu = self.driver.find_element(InsiderCareerPOM .careers_submenu)
        careers_submenu.click()

    def is_careers_page_opened(self):
        return "Careers at Insider | Insider" in self.driver.title

    def check_locations_teams_life_blocks(self):
        locations_block = self.driver.find_element(InsiderCareerPOM .locations_block)
        teams_block = self.driver.find_element(InsiderCareerPOM .teams_block)
        life_block = self.driver.find_element(InsiderCareerPOM .life_block)

        return locations_block.is_displayed() and teams_block.is_displayed() and life_block.is_displayed()

    def dismiss_cookie_banner(self):
        try:
            cookie_banner = self.driver.find_element(By.ID, "wt-cli-cookie-banner-title")
            if cookie_banner.is_displayed():
                actions = ActionChains(self.driver)
                actions.move_to_element(cookie_banner)
                actions.click().perform()
        except Exception as e:
            print("Cookie banner not found or not clickable:", str(e))

# Initialize the WebDriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.set_window_size(1024, 600)
driver.maximize_window()

# Test Case
insider_career_page = Insider(driver)
insider_career_page.open_home_page()
assert insider_career_page.is_home_page_opened()

insider_career_page.navigate_to_careers()
insider_career_page.dismiss_cookie_banner()
driver.implicitly_wait(10)
insider_career_page.open_careers_page()
driver.implicitly_wait(10)
assert insider_career_page.is_careers_page_opened()

assert insider_career_page.check_locations_teams_life_blocks()

# Close the browser
driver.quit()

