from django import forms

class NewEntryForm(forms.Form):
    entryName = forms.CharField(label="New Entry", max_length=100)
    markDown = forms.CharField(label="Mark Down", widget=forms.Textarea)

class EditEntryForm(forms.Form):
    markDown = forms.CharField(label="Mark Down", widget=forms.Textarea)