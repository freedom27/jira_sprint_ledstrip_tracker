from jirawrapper import JIRAWrapper
import sys
import getopt

if __name__ == "__main__":
    argv = sys.argv[1:]
    print_help = lambda: print('sprintreport.py [-p project] -c <username:password>')
    try:
        opts, args = getopt.getopt(argv, "p:c:", ["project=", "credentials="])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    project = 'HSD'
    username = None
    password = None
    for opt, arg in opts:
        if opt in ('-p', '--project'):
            project = arg
        elif opt in ('-c', '--credentials'):
            if ':' in arg:
                username = arg.split(':')[0]
                password = arg.split(':')[1]

    if username is None or password is None:
        print_help()
        sys.exit(2)

    try:
        jira_wrapper = JIRAWrapper(username, password, project)
        print('Stories in current sprint:')
        for issue in jira_wrapper.current_sprint_user_stories():
            if issue.fields.status.name == 'Completed':
                percent = 100
            else:
                percent = issue.fields.aggregateprogress.percent
            print('{0} - {1}% - {2}'.format(issue.key, str(percent), issue.fields.summary))
        print('Sprint completed at {0}%'.format(str(jira_wrapper.current_sprint_progress())))
    except:
        print('ERROR: An error occurred while contacting JIRA!')
