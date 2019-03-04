import datetime

from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView
from django.forms import inlineformset_factory
from django.urls import reverse

from polls.form import QuestionForm
from polls.models import Question,Choice

def choice(request, question_id):
	question = Question.objects.get(pk=question_id)
	ChoiceFormset = inlineformset_factory(Question, Choice, fields=('choice_text',))

	if request.method == 'POST':
		formset = ChoiceFormset(request.POST, instance=question)
		if formset.is_valid():
			formset.save()

		return redirect(choice, question_id = question.id)
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

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except(KeyError,Choice.DoesNotExist):
		return render(request,'polls/detail.html',{'question': question, 'error_message': "You didn't select a choice",})
	else:
		selected_choice.votes +=1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question':question})

def home(request):
	latest_question_list=Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/home.html', context)
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
