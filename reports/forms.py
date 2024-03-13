from django import forms
from .models import Report


class YourModelForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["title"]
