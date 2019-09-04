import os
import html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

password = 'fisapliciranje'
email = 'andjela.pajic90@gmail.com'

def waitForElement(driver, time, method, elementName):
  try:
    element = WebDriverWait(driver, time).until(
      EC.presence_of_element_located((method, elementName))
    )
  except Exception as e:
    print('element not found' + elementName)
    print(e)
  return element
# scroll page to element
def moveToElementByXpath(actions, elementXpath):
  element = driver.find_element_by_xpath(elementXpath)
  actions.move_to_element(element).perform()

def pressNext():
   #wait for the next page and click next
   waitForElement(driver, 10, By.ID, 'nextButton').click()

try:
  driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get("https://www.fisglobal.com/")
  actions = ActionChains(driver);
  #clicking on careers
  driver.find_element_by_xpath('/html/body/div[2]/header/div/div/div[2]/ul[1]/li[4]').click()

  #hover over menu to select search job
  moveToElementByXpath(actions, '/html/body/div[2]/header/div/div/div[6]/ul/li[6]/a')
  driver.find_element_by_xpath('/html/body/div[2]/header/div/div/div[6]/ul/li[6]/a/h3').click()
  driver.find_element_by_xpath('//*[@id="btnContinue"]').click()

  #clicking on search jobs
  driver.find_element_by_xpath('//*[@id="494d8f54-3675-480f-b32f-25b818d09861"]/div/div[2]/div[1]/a/div/div/span[2]/span[2]').click()
  #wait for the search jobs page
  searchIframe = waitForElement(driver, 10, By.XPATH, '//*[@id="careersframe"]')

  #switch context to the iframe
  driver.switch_to_frame(searchIframe)
  #filling the button search Job by ID
  driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.SEARCHCRITERIA_CLIENTREQID"]').send_keys('JR71455')
  #clicking to Search Button
  driver.find_element_by_id('sp-searchButton').click()

  #waiting for searchApplyButton
  searchApplyButton = waitForElement(driver, 10, By.ID, 'applybutton_149750_en-us')

  #apply for the position
  searchApplyButton.click()
  #filling the input for email
  driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.USER_AUTH_PRIMARYEMAILADDRESS"]').send_keys(email)
  #filling the input for password
  driver.find_element_by_xpath('//*[@id="com.peopleclick.cp.formdata.USER_AUTH_PASSWORD"]').send_keys(password)
  #clicking on signInButton
  driver.find_element_by_xpath('//*[@id="signinButton"]').click()

  #wait for the next page and click next
  pressNext()

  #wait for the next page and click next
  pressNext()

  #wait for the RESUME page
  useSavedResume = waitForElement(driver, 10, By.XPATH, '//*[@id="repositoryRadio"]')
  useSavedResume.click()

  useSavedCoverLetter = driver.find_element_by_xpath('//*[@id="repositoryCLRadio"]')
  useSavedCoverLetter.click()

  #wait for the next page and click next
  pressNext()

  #wait for the next page and click next
  pressNext()

  #wait for the next page and click next
  pressNext()

  luckyButton = waitForElement(driver, 10, By.XPATH, '//*[@id="finishButton"]')
  # submit application
  luckyButton.click()

except Exception as e:
  print('Something goes wrong')
  print(e)
