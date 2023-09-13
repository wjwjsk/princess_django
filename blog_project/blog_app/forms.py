from django import forms
from ckeditor.widgets import CKEditorWidget

class CKForm(forms.Form):
    content = forms.CharField(widget=CKEditorWidget())
    image = forms.ImageField()