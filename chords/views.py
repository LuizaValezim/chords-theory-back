from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .serializers import CombinationsSerializer
from .models import Combinations
import requests

def index(request):
    return HttpResponse("Olá! Bem vind@ ao Chords Theory, onde compor uma música nunca foi tão fácil.")    

@api_view(['GET', 'POST'])
def api_combinations_get(request, combination_id):
    try:
        combination = Combinations.objects.get(id=combination_id)
    except Combinations.DoesNotExist:
        raise Http404()

    serialized_combination = CombinationsSerializer(combination)
    return Response(serialized_combination.data)


@api_view(['GET', 'POST'])
def api_combinations_post(request):
    if request.method == 'POST':
        new_combination_data = request.data
        combination = Combinations()
        combination.content = new_combination_data['content']
        combination.save()
    
    serialized_combination = CombinationsSerializer(combination)
    return Response(serialized_combination.data)


@api_view(['DELETE','GET'])
def api_combinations_delete(request,id):
    if request.method == "DELETE":
        combination = Combinations.objects.get(id=id)
        combination.delete()
        
    combination = Combinations()
    serialized_combination = CombinationsSerializer(combination)
    return Response(serialized_combination.data) 


# Fazendo o POST e o GET da API pelo backend
def api_token():
    URL = 'https://api.hooktheory.com/v1/users/auth'

    headers = {
        'Content-Type': 'application/json', 
        'Accept':'application/json'
    }

    data ={ 'username':'luizavalezim',
            'password':'luizavalezim123'}

    r = requests.post(url=URL, headers=headers, data=data)

    return r.json()['access_token']


def get_songs(sufix):
    access_token = api_token()

    headers = {
        f'Authorization': 'Bearer ' + access_token
    }

    try:
        r = requests.get('https://api.hooktheory.com/v1/trends/' + sufix, headers=headers)
        r.raise_for_status()
    except:
        return 'error'

    return r.json()