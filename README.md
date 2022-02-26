# SurfScraperLED
<hr>
This project could be used to scrape the surf status of a specific surf spot from Surfline.com and display the result using a red, yellow and green LED (like a traffic light) that are connected via Raspberry PI 3 B. <br><br>

The project has been set up as multiple Python class objects called SurfScraper (scrapes the information) and SurfStatusLight (Turns off and on LED's according to scraped surf status).

To scrape the surf status and set the lights accordingly, you'll need to set up the environment:

`pip install -r requirements.txt`

In the SurfScraper "__init__" function the url of the specific surf spot on Surfline.com can be set.

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




Prerequisites to create the SurfScraperLED:

Technical components utilized:
Raspberry Pi 3 B
1 TrafficLight LEDs ("Amazon.com: Pi Traffic Light for the Raspberry Pi (2 pack) : Electronics" https://www.amazon.com/Pi-Traffic-Light-Raspberry-pack/dp/B00RIIGD30)
3 Male-to-Female connectors (
"Amazon.com: ELEGOO 120pcs Multicolored Dupont Wire 40pin Male to Female, 40pin Male to Male, 40pin Female to Female Breadboard Jumper Wires Ribbon Cables Kit Compatible with Arduino Projects : Electronics" https://www.amazon.com/Elegoo-EL-CP-004-Multicolored-Breadboard-arduino/dp/B01EV70C78/ref=mp_s_a_1_3?crid=PW0DMJ2QAA35&keywords=female-to+male+dupont+breadboard&qid=1645836784&sprefix=female-to+male+dupont+breadb%2Caps%2C311&sr=8-3)
Picture of wirr


Hope this is useful!
