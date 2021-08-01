from seleniumwire import webdriver  # Import from seleniumwire
from bs4 import BeautifulSoup

chromedriver_location = input(str('Enter the location to your chromedriver: '))

driver = webdriver.Chrome(chromedriver_location)

URL = 'http://the-internet.herokuapp.com/nested_frames'
driver.get(URL) 

required = ['left' , 'middle' , 'right' , 'bottom']
links = []
for request in driver.requests:
    if request.response:
        if request.url.split('_')[-1] in required:
            links.append(request.url)

ans = []            
for i in range(len(links)):
    driver.get(links[i])
    data = BeautifulSoup(driver.page_source)
    required_text = data.find('body')
    ans.append(required_text.text)
    
for i in ans:
    i = i.strip()
    print(i)
    
