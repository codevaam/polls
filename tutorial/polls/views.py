import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from polls.form import AddPolls


class AddPollsView(TemplateView):

	def get(self, request):
		form = AddPolls()
		return render(request, "polls/addpolls.html", {'form': form})
	
	def post(self, request):
		form = AddPolls(request.POST)
		if not form.is_valid():
			return HttpResponse(str(form.errors))
	
		# Save a Question with current time
		question = form.save(commit=False)
		question.pub_date = datetime.datetime.now()
		question.save()

		# Send a response about successful submission
		text = form.cleaned_data['question_text']
		args = {'form': form, 'text': text}
		return render(request, "polls/addpolls.html", args)
