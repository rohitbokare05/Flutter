from rest_framework import generics
from .models import Todo
from .serialiser import TodoSerilizer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def my_view(request):
    if request.method == 'GET':
        data = {"message": "Hello, world!"}
        return JsonResponse(data)
class TodoGetCreate(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerilizer

class TodoUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerilizer

