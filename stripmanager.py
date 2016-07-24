import time
import requests
import settingsmanager
from neopixel import *

# LED strip configuration:
LED_COUNT      = settingsmanager.get_ledstrip_led_count()      # Number of LED pixels.
LED_PIN        = settingsmanager.get_ledstrip_gpio_pin()       # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = settingsmanager.get_ledstrip_led_frequency()  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = settingsmanager.get_ledstrip_dma()            # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = settingsmanager.get_ledstrip_brightness()     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = settingsmanager.is_ledstrip_signal_inverted() # True to invert the signal (when using NPN transistor level shift)

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()


def is_url_reachable(url):
    try:
        if requests.get(url).status_code == 200:
            return True
        else:
            return False
    except:
        return False


def fill_strip_percentage(perc):
    # checking how many leds must be turned on
    limit = int(LED_COUNT*perc)
    # clear the strip otherwise when a new sprint begins the strip will stay full
    for i in range(60):
        strip.setPixelColor(i, 0)
    strip.show()
    # iterating over every let to set the proper color
    for i in range(limit):
        delta = float(255)*(float(i)/60.0)
        strip.setPixelColorRGB(i, int(delta), int(255-delta), 0)
        strip.show()
        time.sleep(0.2)

