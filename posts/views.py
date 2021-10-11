from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

class HolaMundo (View):
    def get(self, request):
        data = {
            'name': 'Karla Moyón',
            'age': 24,
            'codes': ['Python', 'Django', 'React']
        }
        return render (request, 'holaMundo.html', context=data)
