
from django.test import TestCase
from unittest import TestCase

from generic_app.submodels.DocumentProximityRenamer.UploadFiles.UploadFile import UploadFile


class q4_basic_test(TestCase):

    def setUp(self) -> None:
        path = 'submodels/DocumentProximityRenamer/Tests/'
        quarter = UploadFile(name='Simple Test', zip_file=path+'simple_zip.zip', renaming_table=path+"simple_renaming_table.xlsx")
        quarter.calculate = True
        quarter.save()

    def test(self):
        pass