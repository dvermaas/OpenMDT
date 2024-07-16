from django import forms
from .models import Profile


class ProfileInfoForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "surname"]


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["picture"]

    def __init__(self, *args, **kwargs):
        super(ProfilePictureForm, self).__init__(*args, **kwargs)
        self.fields["picture"].label = ""


class ProfileSummaryForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["body"]

    def __init__(self, *args, **kwargs):
        super(ProfileSummaryForm, self).__init__(*args, **kwargs)
        self.fields["body"].label = ""
