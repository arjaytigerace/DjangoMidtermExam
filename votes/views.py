from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Candidate, Vote, Position

app_name='votes'

# Create your views here.
def index(request):
    context={}

    candidates = Candidate.objects.all().order_by('-position')
    context['candidates'] = candidates
    return render(request,'indext.html', context)
