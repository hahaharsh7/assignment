from seleniumwire import webdriver  # Import from seleniumwire
from bs4 import BeautifulSoup

chromedriver_location = input(str('Enter the location to your chromedriver: '))

driver = webdriver.Chrome(chromedriver_location)

URL = 'http://the-internet.herokuapp.com/nested_frames'
driver.get(URL)

links = []
for request in driver.requests:
    if request.response:
        links.append(request.url)

ans = []            
for i in range(len(links)):
    driver.get(links[i])
    data = BeautifulSoup(driver.page_source)
    try:
        required_text = data.find('body')
        required_text = (required_text.text).strip().split()
        if len(required_text)==1:
            ans.append(required_text)
    except:
        pass

for i in ans:
    for j in i:
        print(j)
        
driver.quit()    
