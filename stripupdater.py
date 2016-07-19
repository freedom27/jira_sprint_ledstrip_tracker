from jirawrapper import JIRAWrapper
import settingsmanager
import stripmanager


def update_strip():
    username, password = settingsmanager.get_jira_credentials()
    project = settingsmanager.get_jira_project()
    jira = JIRAWrapper(username, password, project)
    progress = jira.current_sprint_progress(force_refresh=True)
    perc = float(progress)/100.0
    stripmanager.fill_strip_percentage(perc)

if __name__ == '__main__':
    update_strip()
