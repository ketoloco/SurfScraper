# SurfStatusLED

## Purpose


This project could be used to scrape the current surf conditions (surf status) of a specific surf spot from [Surfline](https://www.surfline.com/) and display the result using a red, yellow and green LED (like a traffic light) that are connected via Raspberry PI 3 B.

![Screenshot](https://user-images.githubusercontent.com/87895941/155831384-48abbec6-0f75-4441-9064-f9ceadfe6eca.jpeg)

The project has been set up as multiple Python class objects called SurfScraper (scrapes the information) and SurfStatusLight (Turns off and on LED's according to scraped surf status).

## Setup

To scrape the surf status and set the lights accordingly, you'll need to do the following

1) set up the environment:

`pip install -r requirements.txt`

2) Install chromedriver for Chromium

`sudo apt-get install chromium-chromedriver`

If not using the chromium browser you will need to download the fitting [chromedriver](https://chromedriver.chromium.org/downloads) and adjust the corresponding arguments in the script accordingly.

3) Wire Raspberry PI and LEDs. Example for Raspberry PI 3 B pin out [here](https://www.etechnophiles.com/wp-content/uploads/2020/12/R-PI-pinout.jpg?ezimgfmt=rs%3Adevice%2Frscb40-1).

## How it works

In the SurfScraper "__init__" function the url of the specific surf spot from Surfline.com that should be scraped  needs to be set.

```
self.url = 'https://www.surfline.com/surf-report/bondi-beach/5842041f4e65fad6a7708bf8?camId=5d4819606fe847165bae11b2' 
```

Once the status was scrapped it will be switched to a numeric number - either 0,1,2 (FLAT - POOR: 0, POOR - POOR TO FAIR = 1, FAIR TO GOOD - EPIC = 2)

```
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
```

In the next step the LED's will be turned on based on the numeric status.

```
        if surf_status == 0: 
            GPIO.output(9, True) # Turns on the Red LED
        if surf_status == 1:
            GPIO.output(10, True) # Turns on the Yellow LED
        if surf_status == 2:
            GPIO.output(11, True) # Turns on the Green LED
```

This python script is then beeing executed in consistent periods via cronjob. The LED's are on as long there is a forecast. 




## Technical components utilized for project

1 * Raspberry Pi 3 B (other RPI versions should work as well)
1 * [Pi Traffic Light LEDs](https://www.amazon.com/Pi-Traffic-Light-Raspberry-pack/dp/B00RIIGD30)
3 * [F-M Dupont wire](https://www.amazon.com/dp/B01EV70C78/ref=cm_sw_em_r_mt_dp_4YDD4VEGT1V00Z8MD2FH?_encoding=UTF8&psc=1)



Hope this is useful!
