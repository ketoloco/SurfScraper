import logging
import time
import RPi.GPIO as GPIO
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class SurfScraper:
    """
    The Surf Scraper is scraping the surf forecast from surfline.com.
    """
    def __init__(self, delay=5):
        """Initialize class set logger

        Parameters
        ----------
        url : str
        """

        # set logger
        log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        logging.basicConfig(level=logging.INFO, format=log_fmt)
        self.delay=delay
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless") #to run chrome in headless mode
        logging.info("Starting driver")
        
        self.driver = webdriver.Chrome('/usr/bin/chromedriver', options=self.chrome_options)
        self.surf_status = None

        #Surfline url of spot whose surf status should be scraped (change to spot that should be scraped)
        self.url = 'https://www.surfline.com/surf-report/bondi-beach/5842041f4e65fad6a7708bf8?camId=5d4819606fe847165bae11b2' 

    def scrape_status(self):
        """Opens surfline url and scrapes information about surf status.
        """
        self.driver.get(self.url)
        time.sleep(self.delay)
        report = self.driver.find_elements_by_class_name("quiver-spot-report")
        for status in report:
            status_details = status.text.split('\n')[:3]
            status_spot = status_details[0]
            time.sleep(self.delay)
        self.surf_status = status_spot

    def close_session(self):
        """Closes session
        """
        logging.info("Closing session")
        self.driver.close()


class SurfStatusLight:
    """
    The SurfStatusLight can turn on/off 3 external LEDs (green, yellow and red) conencted to a Raspberry PI 3 Model B via GPIO depending on the surf status scraped of a 
    """
    def __init__(self):
        """Initialize class
        """
        GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
     
    def set_light(self,surf_status):
        """Turn on LED depending on numeric surf status
        """
        # Pin setup
        GPIO.setup(9, GPIO.OUT) # Red LED pin set as output
        GPIO.setup(10, GPIO.OUT) # Yellow LED pin set as output
        GPIO.setup(11, GPIO.OUT) # Green LED pin set as output

        # Set the pin HIGH - turn on LED
        if surf_status == 0: 
            GPIO.output(9, True) # Turns on the Red LED
        if surf_status == 1:
            GPIO.output(10, True) # Turns on the Yellow LED
        if surf_status == 2:
            GPIO.output(11, True) # Turns on the Green LED


def switch_string_to_numeric(argument):
    """
    Switch status string to numeric status (FLAT - POOR: 0, POOR - POOR TO FAIR = 1, FAIR TO GOOD - EPIC = 2)
    """

    switcher = {
        "FLAT": 0,
        "VERY POOR": 0,
        "POOR": 0,
        "POOR TO FAIR":1,
        "FAIR":1,
        "FAIR TO GOOD":2,
        "GOOD":2,
        "VERY GOOD":2,
        "GOOD TO EPIC":2,
        "EPIC":2
    }

    # get() method of dictionary data type returns
    # value of passed argument if it is present
    # in dictionary otherwise second argument will
    # be assigned as default value of passed argument
    return switcher.get(argument, "nothing")


if __name__ == "__main__":

    scraper = SurfScraper() #Create instance
    scraper.scrape_status() #Scrape surf status
    scraper.close_session() #Close scraping session
    print(scraper.surf_status) 
    surf_status_number = switch_string_to_numeric(scraper.surf_status) #Switch scraped surf status string against numeric status 1-3 
    light = SurfStatusLight()
    light.set_light(surf_status_number)  
