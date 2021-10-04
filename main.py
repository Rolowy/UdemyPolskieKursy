from selenium import webdriver
import time
import datetime

class PythonOrgSearch():
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--headless')
        
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def test_search(self, url):
        table = []
        url = url

        time.sleep(1)

        for i in range(0, len(url)):
            print("Uruchomienie strony: " + str(url[i]))
            fullurl = 'https://www.udemy.com/courses/' + url[i] + '/?lang=pl&price=price-free&sort=popularity'
            self.driver.get(fullurl)
            time.sleep(1)

            
            pack = self.driver.find_elements_by_tag_name('a')

            licznik = 0
            for value in pack:
                if value.get_attribute('href'):
                    if 'course/' in value.get_attribute('href'):
                        licznik+=1
                        if licznik >= 7:
                            # print(value.get_attribute('href'))
                            table.append(value.get_attribute('href'))
        return table





if __name__ == "__main__":
    url = [
        'development',
        'business',
        'finance-and-accounting',
        'it-and-software',
        'office-productivity',
        'personal-development',
        'design',
        'marketing',
        'lifestyle',
        'photography-and-video',
        'health-and-fitness',
        'music',
        'teaching-and-academics']
    
    main = PythonOrgSearch()
    table = main.test_search(url)

    mydate = datetime.datetime.now()
    mydate = mydate.strftime("%d%m%Y")

    full_url = "Udemy-PolskieKursy " + mydate + ".txt"
    file = open(full_url, "w")

    for value in table:
        print(value)
        file.write(value+"\n")
    
    file.close()

