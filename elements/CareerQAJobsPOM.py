from selenium.webdriver.common.by import By


class CareerQAJobsPOM:
    URL = 'https://useinsider.com/careers/open-positions/?department=qualityassurance'
    see_all_jobs_button = (By.XPATH, "//a[contains(text(), 'See all QA jobs')]")
    location_filter = (By.CSS_SELECTOR, "#location")
    department_filter = (By.CSS_SELECTOR, "#department")
    job_list = (By.XPATH, "//div[@class='jobs-list']//div[@class='job']")
