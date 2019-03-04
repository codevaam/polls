import datetime

from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.forms import inlineformset_factory

from polls.form import QuestionForm
from polls.models import Question,Choice

def choice(request, question_id):
	question = Question.objects.get(pk=question_id)
	ChoiceFormset = inlineformset_factory(Question, Choice, fields=('choice_text',))

	if request.method == 'POST':
		formset = ChoiceFormset(request.POST, instance=question)
		if formset.is_valid():
			formset.save()

		return redirect('choice', question_id = question.id)
	formset = ChoiceFormset(instance=question)

	return render(request, 'polls/index.html', {'formset': formset, 'question_text': question.question_text})

def index(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		if not form.is_valid():
			return HttpResponse(str(form.errors))

			# Save a Question with current time
		question = form.save(commit = False)
		question.pub_date = datetime.datetime.now()
		question.save()
		return redirect(choice, question_id=question.id)
	if request.method=='GET':
		form = QuestionForm()
		return render(request, "polls/create.html", {'form': form})
# class AddPollsView(TemplateView):

# 	def get(self, request):
# 		form = QuestionForm()
# 		form1 = ChoiceForm()
# 		return render(request, "polls/create.html", {'form': form,'form1': form1})

# 	def post(self, request):
# 		form = QuestionForm(request.POST, extra=request.POST.get('extra_field_count'))
# 		if not form.is_valid():
# 			return HttpResponse(str(form.errors))

# 		# Save a Question with current time
# 		question = form.save(commit = False)
# 		question.pub_date = datetime.datetime.now()
# 		question.save()

# 		# Send a response about successful submission
# 		text = form.cleaned_data['question_text']
# 		args = {'form': form}
# 		return render(request, "polls/create.html", args)
