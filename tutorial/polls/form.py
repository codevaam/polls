from django import forms

class AddPolls(forms.Form):
	question = forms.CharField()
	