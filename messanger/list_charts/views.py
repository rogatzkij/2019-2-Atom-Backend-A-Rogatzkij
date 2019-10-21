from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

chats = ["Ivan", "Rinat", "Vaselisa"]


def index(request):
    return JsonResponse(chats, safe=False)
