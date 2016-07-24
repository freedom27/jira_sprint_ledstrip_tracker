from jirawrapper import JIRAWrapper
import settingsmanager
import stripmanager


def update_strip():
    url = settingsmanager.get_jira_url()
    if stripmanager.is_url_reachable(url):
        username, password = settingsmanager.get_jira_credentials()
        project = settingsmanager.get_jira_project()
        jira = JIRAWrapper(url, username, password, project)
        progress = jira.current_sprint_progress(force_refresh=True)
        perc = float(progress)/100.0
        stripmanager.fill_strip_percentage(perc)
    else:
        print('{0} is unreachable!'.format(url))

if __name__ == '__main__':
    update_strip()
