from django.shortcuts import render
from polls.form import AddPolls
from django.views.generic import TemplateView

class addpolls(TemplateView):

	def get(self,request):
		form = AddPolls()
		return render(request,"polls/addpolls.html",{'form': form})

# Create your views here.
