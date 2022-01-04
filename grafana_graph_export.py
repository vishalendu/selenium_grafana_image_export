from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def is_visible(driver,locator, timeout = 20):
    try:
        WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False

def getPanelImage(url):
    xpath='//*[@id="reactRoot"]/div/main/div[3]/div[1]/section/div[2]/div/div[1]/div/div[1]/div/div/div[4]'
    driver.implicitly_wait(0.5)
    driver.maximize_window()
    driver.get(url)
    try:
        is_visible(driver,xpath)
    except:
        driver.quit()

    driver.get_screenshot_as_file(f'out{panel}.png')
    driver.quit()
    
def dologin(baseurl):
    driver.get(f'{baseurl}/login')
    driver.maximize_window()
    driver.find_element(By.NAME, "user").send_keys("admin")
    driver.find_element(By.ID, "current-password").send_keys("admin")
    driver.find_element(By.CSS_SELECTOR, ".css-3coq9d-button > .css-1mhnkuh").click()


if __name__ == "__main__":
    baseurl = "http://localhost:3100"
    driver = webdriver.Chrome(executable_path="<PATH_TO_CHROMEDRIVER>/chromedriver")
    dologin(baseurl)
    panel=4
    getPanelImage(f'{baseurl}/d-solo/TSq5TL07z/processor?orgId=1&from=1641323169397&to=1641324069397&panelId={panel}')

