import dropbox
import json


dbx = dropbox.Dropbox('XXX')


def get_sprint_progress():
    _, res = dbx.files_download('/progress.json')
    data = str(res.content, "utf-8")
    json_data = json.loads(data)
    return json_data['progress']


def set_sprint_progress(progress):
    json_data = dict()
    json_data['progress'] = progress
    mode = dropbox.files.WriteMode('overwrite', None)
    dbx.files_upload(json.dumps(json_data), '/progress.json', mode=mode)
