from django import forms
from .models import Report, Suspect


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["title", "body"]


class ReportSuspectForm(forms.ModelForm):
    class Meta:
        model = Suspect
        fields = ["profile", "charges"]
