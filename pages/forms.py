# make sure this is at the top if it isn't already
from django import forms

# our new form
class RequestForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    budget = forms.IntegerField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

