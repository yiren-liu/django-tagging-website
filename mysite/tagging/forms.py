from django import forms


class TaggingForm(forms.Form):
    data_pk = forms.CharField(label='data primary key', max_length=100)
    data_tag = forms.CharField(label='Tag data here ', max_length=100)

