import time
from jirawrapper import JIRAWrapper
import settingsmanager
import stripmanager


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
            stripmanager.fill_strip_percentage(perc)
        time.sleep(600)
