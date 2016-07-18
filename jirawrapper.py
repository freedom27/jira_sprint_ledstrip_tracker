from jira.client import JIRA
from datetime import datetime


class JIRAWrapper(object):

    def __init__(self, user, password, project):
        options = {'server': 'http://rndwww.nce.amadeus.net/agile'}
        self._jira = JIRA(options, basic_auth=(user, password))
        self._project = project
        self._last_update = datetime.fromtimestamp(0)
        self._user_stories = []

    def current_sprint_user_stories(self, force_refresh=False):
        now = datetime.now()
        if (now - self._last_update).seconds > 60 or force_refresh:
            user_stories = self._jira.search_issues('project = {0} AND issuetype = Story AND Sprint in openSprints()'.format(self._project))
            user_stories.sort(key=lambda user_story: user_story.key)
            self._user_stories = user_stories
            self._last_update = now
        return self._user_stories

    def current_sprint_progress(self, force_refresh=False):
        total_sprint_value = 0
        total_sprint_progress = 0
        percent_progress = 0
        try:
            for user_story in self.current_sprint_user_stories(force_refresh):
                total_sprint_value += user_story.fields.aggregateprogress.total
                total_sprint_progress += user_story.fields.aggregateprogress.progress
            percent_progress = (total_sprint_progress/total_sprint_value) * 100
        except Exception:
            print('Issue occurred while accessing info related to the active sprint!')
        return round(percent_progress, 2)
