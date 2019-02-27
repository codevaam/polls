from django.urls import path

from . import views

urlpatterns = [
	path('',views.AddPollsView.as_view(),name='index'),
]