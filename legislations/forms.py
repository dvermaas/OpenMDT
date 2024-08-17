from django import forms


class LegislationSearchForm(forms.Form):
    query = forms.CharField(
        label="Search by title",
        max_length=64,
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Search..."}),
    )
