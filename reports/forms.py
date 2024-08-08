from django import forms
from .models import Report, Suspect
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["title", "body"]


class ReportCrispyForm(forms.Form):
    title = forms.CharField(
        label="Title",
        max_length=100,
        required=True,
    )

    body = forms.CharField(
        label="Body",
        max_length=100,
        required=False,
    )

    # is_warrant = forms.BooleanField()
    # is_processed = forms.BooleanField()
    # is_plead_guilty = forms.BooleanField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-exampleForm"
        self.helper.form_class = "blueForms"
        self.helper.form_method = "post"
        self.helper.form_action = "submit_survey"
        self.helper.add_input(Submit("submit", "Submit"))
        # self.helper.layout = Layout(Switch("is_warrant"))


class ReportSuspectForm(forms.ModelForm):
    class Meta:
        model = Suspect
        fields = ["profile"]
