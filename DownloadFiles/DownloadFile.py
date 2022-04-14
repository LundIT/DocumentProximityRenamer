import difflib
import re
import zipfile

import pandas as pd
from django.core.files import File

from generic_app.models import *
from generic_app.submodels.DocumentProximityRenamer.UploadFiles.UploadFile import UploadFile


class DownloadFile(CalculatedModelMixin, Model):

    id = AutoField(primary_key=True)
    upload = ForeignKey(to=UploadFile, on_delete=CASCADE)
    zip_file = XLSXField(upload_to="download/zip_file")
    xlsx_report = XLSXField(upload_to="download/xlsx_report")

    defining_fields = ['upload']

    def get_selected_key_list(self, key: str) -> list:
        if key == 'upload':
            return UploadFile.objects.all()

    def clean_names(self, l):
        return [self.clean_name(s) for s in l]

    def clean_name(self, s):
        return re.sub('[^A-Za-z0-9]+', '', s)

    def calculate(self):
        renamingIDs = pd.read_excel(self.upload.renaming_table, sheet_name='IDs')
        renamingIDs['Cleaned Name'] = self.clean_names(renamingIDs['Name'])
        file_name_matching = {'file_name': [], 'Name': [], 'ID': []}
        target_file_name = self.upload.zip_file.file.name.split(os.sep)[-1].split('.')[0]

        source = zipfile.ZipFile(self.upload.zip_file, 'r')
        target = zipfile.ZipFile(f"{target_file_name}_renamed.zip", 'w', zipfile.ZIP_DEFLATED)
        for file in source.filelist:
            file_name = file.filename
            names = difflib.get_close_matches(self.clean_name(file_name), renamingIDs['Cleaned Name'], n=1, cutoff=0.1)
            if len(names) > 0:
                cleaned_name = names[0]
                id = renamingIDs[renamingIDs['Cleaned Name'] == cleaned_name]['ID'].iloc[0]
                name = renamingIDs[renamingIDs['Cleaned Name'] == cleaned_name]['Name'].iloc[0]
                file_name_matching['file_name'].append(file_name)
                file_name_matching['Name'].append(name)
                file_name_matching['ID'].append(id)
                #TODO dont just rename everything to pdf
                target.writestr(f"{id}.pdf", source.read(file.filename))
            else:
                file_name_matching['file_name'].append(file_name)
                file_name_matching['Name'].append('Not Found')
                file_name_matching['ID'].append('Not Found')


        #self.zip_file.save(f"{target_file_name}_renamed.zip", File(target))
        target.close()
        output_overview = pd.DataFrame.from_dict(file_name_matching)
        XLSXField.create_excel_file_from_dfs(self.xlsx_report,
                                             data_frames=[output_overview],
                                             sheet_names=['Output Overview'],
                                             path=f"{self.upload.name}_file_renaming_output_overview.xlsx")
        source.close()
        local_file = open(f"{target_file_name}_renamed.zip", 'rb')
        self.zip_file.save(f"{target_file_name}_renamed.zip", File(local_file))
        local_file.close()
