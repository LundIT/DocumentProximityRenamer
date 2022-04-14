
def get_model_structure():
    model_structure = {}
    model_structure['UploadFiles'] = {}
    model_structure['DownloadFiles'] = {}
    model_structure['DownloadFiles']['downloadfile'] = None
    model_structure['UploadFiles']['uploadfile'] = None
    return model_structure

def get_model_styling():
    model_styling = {}
    model_styling['DownloadFiles'] = {'name': 'Download Files'}
    model_styling['UploadFiles'] = {'name': 'Upload Files'}
    model_styling['uploadfile'] = {'name': 'Upload File'}
    model_styling['downloadfile'] = {'name': 'Download File'}
    return model_styling