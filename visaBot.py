from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import ImageChops
from PIL import Image
from playsound import playsound
import time

def equal(im1, im2):
    return ImageChops.difference(im1, im2).getbbox() is None


def runScript():
  options = Options()
  options.add_argument("--start-maximized")
  driver = webdriver.Chrome(options=options)
  driver.get("https://www.berlin.de/einwanderung/en/services/appointments/#appointment")
  href = driver.find_element_by_xpath('//*[@id="layout-grid__area--maincontent"]/div/div/div[3]/div[2]/div/div[3]/div[3]/div[2]/div/div/ul[2]/li/a').get_attribute("href")
  driver.execute_script('''window.open("","_blank");''')
  driver.switch_to.window(driver.window_handles[1])
  driver.get(href)
  driver.find_element_by_id("txtLinkEnglisch").click() # english
  driver.find_element_by_id("btnTerminBuchen").click() # book an appointment
  select = Select(driver.find_element_by_id("cobStaat")) # citizenship
  select.select_by_visible_text("Pakistan")
  select = Select(WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.ID, "cobFamAngInBerlin"))
      ))
  select.select_by_visible_text("No")
  select = Select(WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.ID, "cobAnliegen")) # request
      ))
  select.select_by_value("328188")

  WebDriverWait(driver, 10).until(
          EC.presence_of_element_located((By.ID, "cbZurKenntnis"))
      ).click() # checkbox

  driver.find_element_by_id("labNextpage").click() # next

  driver.find_element_by_id("tfFirstName").send_keys("Fatema")
  driver.find_element_by_id("tfLastName").send_keys("Fatema")
  day = Select(driver.find_element_by_id("cobGebDatumTag"))
  day.select_by_value("25")
  month = Select(driver.find_element_by_id("cobGebDatumMonat"))
  month.select_by_value("2")
  driver.find_element_by_id("tfGebDatumJahr").send_keys("1998")
  select = Select(driver.find_element_by_id("cobVPers"))
  select.select_by_value("1")
  driver.find_element_by_id("tfMail").send_keys("fatema.sultan52@gmail.com")
  select = Select(driver.find_element_by_id("cobGenehmigungBereitsVorhanden"))
  select.select_by_value("No")
  driver.find_element_by_id("txtNextpage").click()
  driver.save_screenshot('calender.png')
  img1 = Image.open('calender_old.png')
  img2 = Image.open('calender.png')
  if(list(img1.getdata()) == list(img2.getdata())):
    driver.quit()
    time.sleep(30)
    runScript()
  else:
    playsound('babyshark.mp3')
    input("")  
  


runScript()  





