from django.shortcuts import render, redirect
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .serializers import UserSerializer
from .models import User
from .models import Combinations

def index(request):
    all_combinations = Combinations.objects.all()
    return render(request, 'chords/index.html', {'combinations': all_combinations})       


def add(request):
    title = request.POST.get('titulo')
    chords = request.POST.get('acordes')
    
    combination = Combinations(title=title, chords=chords)
    combination.save()

    serialized_combination = UserSerializer(combination)
    return Response(serialized_combination.data)