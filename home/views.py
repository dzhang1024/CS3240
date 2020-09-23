from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic


class HomeView(generic.DetailView):
    template_name = 'home/homescreen.html'