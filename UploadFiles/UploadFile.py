from ProcessAdminRestApi.models.upload_model import ConditionalUpdateMixin
from generic_app.models import *

class UploadFile(UploadModelMixin, ConditionalUpdateMixin, Model):
    id = AutoField(primary_key=True)
    name = TextField()
    zip_file = FileField(upload_to='upload_files/zip_file', max_length=300, null=True, blank=True)
    renaming_table = FileField(upload_to='upload_files/renaming_table', max_length=300, null=True, blank=True)



    @ConditionalUpdateMixin.conditional_calculation
    def update(self):
        from generic_app.submodels.DocumentProximityRenamer.DownloadFiles.DownloadFile import DownloadFile
        DownloadFile.objects.filter(upload=self).delete()
        DownloadFile.create(upload=[self])

    def __str__(self):
        return f"{self.name}"
