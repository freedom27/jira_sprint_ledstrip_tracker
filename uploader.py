import datamanager
from jirawrapper import JIRAWrapper
import time
import sys
import getopt


def upload_sprint_progress(prog):
    datamanager.set_sprint_progress(prog)
    print('Uploaded: ' + str(prog))


if __name__ == "__main__":
    argv = sys.argv[1:]
    print_help = lambda: print('uploader.py [-p project] -c <username:password>')
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

    jira = JIRAWrapper(username, password, project)

    old_progress = 0
    while True:
        progress = jira.current_sprint_progress(force_refresh=True)
        if not old_progress == progress:
            upload_sprint_progress(progress)
            old_progress = progress
            time.sleep(600)
