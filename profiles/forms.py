from django import forms
from .models import Profile


class ProfileInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "surname"]


class ProfileSummaryForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["body"]
