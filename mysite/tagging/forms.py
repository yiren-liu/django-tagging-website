from django import forms


class TaggingForm(forms.Form):
    data_tag = forms.CharField(label='Tag data here', max_length=100)

