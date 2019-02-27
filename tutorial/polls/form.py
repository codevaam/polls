from django import forms
from polls.models import Question

class AddPolls(forms.ModelForm):
	class Meta:
		model = Question
		fields = ('question_text',)
