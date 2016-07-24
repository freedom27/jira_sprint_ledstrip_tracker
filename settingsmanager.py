import configparser
config = configparser.ConfigParser()
config.read('jira_tracker.ini')


def get_jira_credentials():
    return config['jira_settings']['username'], config['jira_settings']['password']


def get_jira_project():
    return config['jira_settings']['project']
    

def get_jira_url():
    return config['jira_settings']['url']


def get_ledstrip_gpio_pin():
    return int(config['ledstrip_settings']['gpio_pin'])


def get_ledstrip_led_count():
    return int(config['ledstrip_settings']['led_count'])
    
        
def get_ledstrip_led_frequency():
    return int(config['ledstrip_settings']['led_frequency_hz'])
    

def get_ledstrip_dma():
    return int(config['ledstrip_settings']['dma'])
    

def get_ledstrip_brightness():
    return int(config['ledstrip_settings']['brightness'])


def is_ledstrip_signal_inverted():
    return config['ledstrip_settings'].getboolean('invert_signal')