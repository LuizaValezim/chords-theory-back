from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .serializers import UserSerializer
from .models import User

def index(request):
    return HttpResponse("Bem-vindo ao Chords Theory! Venha aprender sobre a teoria musical.")

@api_view(['GET', 'POST'])
def api_user(request, username):
    if request.method == 'POST':
        new_user_data = request.data
        print(new_user_data)
        user = User(username=username, chords=new_user_data['chords'])
        user.save()
    else:
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise Http404()
    
    serialized_user = UserSerializer(user)
    return Response(serialized_user.data)