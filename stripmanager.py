import time
from neopixel import *
from jirawrapper import JIRAWrapper
import settingsmanager

# LED strip configuration:
LED_COUNT      = 60      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
strip.begin()

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

if __name__ == '__main__':
    username, password = settingsmanager.get_jira_credentials()
    project = settingsmanager.get_jira_project()
    jira = JIRAWrapper(username, password, project)

    old_perc = 0.0
    while True:
        progress = jira.current_sprint_progress(force_refresh=True)
        perc = float(progress)/100.0
        if not old_perc == perc:
            old_perc = perc
            fill_strip_percentage(perc)
        time.sleep(600)
