import configparser
config = configparser.ConfigParser()
config.read('jira_tracker.ini')


def get_jira_credentials():
    return config['jira_settings']['username'], config['jira_settings']['password']


def get_jira_project():
    return config['jira_settings']['project']
