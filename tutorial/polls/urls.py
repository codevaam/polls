from django.urls import path

from . import views

urlpatterns = [
	path('',views.index, name='index'),
	path('<question_id>',views.choice,name='choice'),
]
