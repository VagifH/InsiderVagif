from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from elements.CareerQAJobsPOM import CareerQAJobsPOM


class Career:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_careers_page(self):
        self.driver.get(CareerQAJobsPOM.URL)

    def filter_jobs(self, location, department):
        see_all_jobs_button = self.wait.until(EC.element_to_be_clickable(CareerQAJobsPOM.see_all_jobs_button))
        see_all_jobs_button.click()

        location_filter = self.driver.find_element(CareerQAJobsPOM.location_filter)
        location_filter.send_keys(location)

        department_filter = self.driver.find_element(CareerQAJobsPOM.department_filter)
        department_filter.send_keys(department)

    def check_jobs_list(self):
        job_list = self.driver.find_elements(CareerQAJobsPOM.job_list)
        return job_list

    def check_job_details(self, job):
        position = job.find_element(By.CLASS_NAME, "position").text
        department = job.find_element(By.CLASS_NAME, "department").text
        location = job.find_element(By.CLASS_NAME, "location").text

        return "Quality Assurance" in position and "Quality Assurance" in department and "Istanbul, Turkey" in location

    def click_view_role(self,job,):
        view_role_button = job.find_element(By.XPATH, ".//a[contains(text(), 'View Role')]")
        view_role_button.click()

        # Add code to check that the action redirects to the Lever Application form page


# Initialize the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Test Case
career_page = Career(driver)
career_page.open_careers_page()
career_page.filter_jobs("Istanbul, Turkey", "Quality Assurance")

job_list = career_page.check_jobs_list()

for job in job_list:
    assert career_page.check_job_details(job)
    career_page.click_view_role(job)

# Close the browser
driver.quit()
