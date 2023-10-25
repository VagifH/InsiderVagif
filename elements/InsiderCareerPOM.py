from selenium.webdriver.common.by import By


class InsiderCareerPOM :

    URL = 'https://useinsider.com'
    careers_menu = (By.XPATH, "//a[contains(text(), 'Careers')")
    careers_submenu = (By.CSS_SELECTOR, 'a[href="/careers"]')
    locations_block = (By.CSS_SELECTOR, "div[class='elementor-element elementor-element-38b8000 elementor-widget elementor-widget-wp-widget-insider-locations']")
    teams_block = (By.CSS_SELECTOR, "div[class='col-12 d-flex flex-wrap p-0 career-load-more']")
    life_block = (By.CSS_SELECTOR, "div[class='elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-87842ec']")
