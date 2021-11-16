from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .serializers import CombinationsSerializer
from .models import Combinations

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