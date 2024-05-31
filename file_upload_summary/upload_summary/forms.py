from django import forms
from django.core.exceptions import ValidationError

class UploadFileForm(forms.Form):
    file = forms.FileField(label='Select a CSV or Excel file')

    def clean_file(self):
        file = self.cleaned_data['file']
        if not file.name.endswith(('.csv', '.xlsx', '.xls')):
            raise ValidationError('File must be a CSV or Excel file')
        return file
