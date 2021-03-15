from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


yaz = open('html.txt', 'w')
time.sleep(0.2)

lines = []
while True:
    line = input("Metini boş satır olmadan yapıştırınız!!!")
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)

yaz.write(str(text))
yaz.close()

oku=open("html.txt","r+")
time.sleep(0.2)

driver = webdriver.Chrome('chromedriver')
driver.get("https://www.hiqpdf.com/demo/ConvertHtmlToPdf.aspx")
elem2 = driver.find_element_by_id("ctl00_ContentPlaceHolder1_radioButtonConvertHtmlCode")
elem2.click()
time.sleep(0.5)

elem = driver.find_element_by_id("ctl00_ContentPlaceHolder1_textBoxHtmlCode")
elem.clear()
elem.send_keys(oku.read())
oku.close()

elem.send_keys(Keys.RETURN)
pdf = driver.find_element_by_id("ctl00_ContentPlaceHolder1_buttonConvertToPdf")
pdf.click()

time.sleep(1)
driver.close()