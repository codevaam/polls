from django import forms

from polls.models import Question, Choice


ChoiceFormSet = forms.modelformset_factory(Choice, fields=('choice_text',))


class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('question_text',)

#     def __init__(self, *args, **kwargs):
#         # We take out "extra" which tell us how many additional fields have
#         # been added.
#         extra_fields = kwargs.pop('extra', 0)

#         super().__init__(*args, **kwargs)
#         count = int(extra_fields)
#         self.fields['extra_field_count'].initial = count

#         # Add additional fields, as specified via extra_fields
#         for index in range(count):
#             field_name = 'extra_field_{index}'.format(index=index)
#             self.fields[field_name] = ChoiceFormSet()

# class ChoiceForm(forms.ModelForm):

#     class Meta:
#         model = Choice
#         fields = ('choice_text',)
