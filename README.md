
# rpi-weather
![thumbnail](http://caternuson.github.io/rpi-weather/static/rpi-weather-thumb.jpg)<br/>
Python 3.9 application to get local weather forecast and display results
via icons on LED 8x8 matrices.

# Hardware

## Overview
Here's a general overview about the hardware setup to give you some orientation: https://caternuson.github.io/rpi-weather/. The wodden case has roughly these dimensions: 19cm (length) x 13cm (width) x 8cm (height). The jumper cables should have a length of 16-18 cm.

This program should work with any Raspberry Pi although I have only tested it with an original Model A (yes, an A). Also, any 4 Adafruit 8x8 LED Matrices with I2C Backpacks should work.

## Soldering the address jumpers
Be sure to [solder the address jumpers](https://learn.adafruit.com/adafruit-led-backpack/changing-i2c-address#changing-addresses-706265) to set unique addresses for each. Expected range is 0x70-0x73. Make sure you solder the pins of the matrices in the right direction for this project (in other words, **do not** follow the soldering instructions as presented in [this tutorial](https://learn.adafruit.com/adafruit-led-backpack/0-8-8x8-matrix-assembly), the pins have to be the other way around )
# Software
A brief description of the various software components.
* ```weather.py``` - gets and displays forecast from [NOAA](http://graphical.weather.gov/xml/rest.php) (**US ONLY**)
* ```weather_metoffice.py``` - gets and displays forecast from [metoffice.gov.uk](http://metoffice.gov.uk) (**UK ONLY**)
* ```weather_forecastio.py``` - gets and displays forecast from [forecast.io](http://forecast.io)
* ```weather_openweather.py``` - gets and displays forecast from [openweathermap.org](http://openweathermap.org)
* ```rpi_weather.py``` - defines a class for interfacing with the hardware
* ```led8x8icons.py``` - contains a dictionary of icons
* ```clock.py``` - displays the time, for use as a clock
# Dependencies

Optional: Before installing any software, it is convenient to set up  your raspberry pi using [the rpi imager](https://learn.adafruit.com/raspberry-pi-zero-creation/using-rpi-imager) (so you can ssh into it, or even use a remote desktop client to get a graphical user interface). If you are using Windows on your hostmachine and you want to use the Remote Desktop Client make sure that `xrdp` is installed on the pi by running `sudo apt install xrdp`.

You need to then install Python & the [Adafruit_CircuitPython_HT16K33 Library](https://github.com/adafruit/Adafruit_CircuitPython_HT16K33#installing-from-pypi) so that your Rasperry Pi can communicate with the Adafruit LED matrices. For that you can follow [this tutorial](https://learn.adafruit.com/adafruit-led-backpack/0-8-8x8-matrix-python-wiring-and-setup). 


# Install
Simply clone this repo and run:
```
$ git clone https://github.com/caternuson/rpi-weather.git
$ cd rpi-weather
$ sudo python weather.py
```

# Configure (NOAA)
The forecast location is specified with a zipcode. A default zipcode can be
set in the code:
```python
ZIPCODE = 98109
```
A zipcode can also be passed in from the command line, which will override the
default:
```
$ sudo python weather.py 98109
```

# Configure (metoffice.gov.uk)
You will need an API key to use these services, available [here](http://www.metoffice.gov.uk/datapoint/API).
You will also need to determine your location ID. To get that you need to hit this url:
```
http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/json/sitelist?key=[YOUR_API_KEY_HERE]
```
and search for your nearest location. If you can't find the location you are after you can hit the [main site](http://www.metoffice.gov.uk) and use their front-end search to find the closest location they have,
then get the code for that from the api response above.

Once you have this info, create a file called ```weather.cfg```
with the following contents:
```
[config]
API_KEY: your_api_key
LOCATION_ID: your_location_id
```
replacing the ```your_*``` info as needed.

# Configure (forecast.io and openweathermap.org)
You will need an API key to use these services. Each website has instructions
for how to do this. You will also need the latitude and longitude for your
location. Once you have this info, create a file called ```weather.cfg```
with the following contents:
```
[config]
APIKEY: your_api_key
LAT: your_latitude
LON: your_longitude
```
replacing the ```your_*``` info as needed. **NOTE:** west longitudes are negative,
use decimal values for both.

# Automation
The easiest way to have the program run on a daily basis is to use ```cron```.
Use ```crontab -e``` to add the following entry, which will run the program
every morning at 4AM:
```
0 4 * * * sudo -E PYTHONPATH=$PYTHONPATH python /home/pi/rpi-weather/weather.py
```
**NOTE:** If you installed the program in a different location, change the path
accordingly.

# NOAA REST
The forecast is determined using the [NOAA REST](http://graphical.weather.gov/xml/rest.php)
web service. Specifically, the **Summarized Data for One or More Zipcodes**. A
typical request looks like:
```
http://graphical.weather.gov/xml/sample_products/browser_interface/ndfdBrowserClientByDay.php?zipCodeList=98109&format=12+hourly&numDays=4
```
The key bits being:
* ```zipCodeList``` - zipcode(s) for forecast
* ```format``` - choose either 12 or 24 hour period
* ```numDays``` - number of days in forecast

The request returns XML data. The icons are set by a simple text search in the
```weather-summary``` attribute of the ```weather-conditions``` tag.

# forecast.io and openweathermap.org
An ```ICON_MAP``` is defined to map forecast results to a specific LED 8x8 icon.

# Icons
| Icon | Weather  |
| :---: | :---: |
| ![SUNNY](http://caternuson.github.io/rpi-weather/static/SUNNY.jpg) | SUNNY |
| ![RAIN](http://caternuson.github.io/rpi-weather/static/RAIN.jpg) | RAIN |
| ![CLOUD](http://caternuson.github.io/rpi-weather/static/CLOUD.jpg) | CLOUD |
| ![SHOWERS](http://caternuson.github.io/rpi-weather/static/SHOWERS.jpg) | SHOWERS |
| ![STORM](http://caternuson.github.io/rpi-weather/static/STORM.jpg) | STORM |
| ![SNOW](http://caternuson.github.io/rpi-weather/static/SNOW.jpg) | SNOW |
| ![UNKNOWN](http://caternuson.github.io/rpi-weather/static/UNKNOWN.jpg) | none of the above |
