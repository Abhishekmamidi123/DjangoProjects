# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import (View, TemplateView,
                                ListView, DetailView,
                                CreateView, UpdateView,
                                DeleteView)
from django.core.urlresolvers import reverse_lazy
from .import models
# from django.http import HttpResponse

# Create your views here.
# def index(request):
#     return render(request, 'index.html')

# class CBView(View):
#     def get(self, request):
#         return HttpResponse("Class based views are really COOL")


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School
    template_name = 'basic_app/school_list.html'
    # returns school_list

class SchoolDetailView(DetailView):
    # returns school
    context_object_name = 'school_details'
    model = models.School
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    #template --> school_form.html
    fields = ('name', 'principal', 'location')
    model = models.School

class SchoolUpdateView(UpdateView):
    #template --> school_form.html
    fields = ('name', 'principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    #template --> school_conform_delete.html
    model = models.School
    success_url = reverse_lazy("basic_app:list")
