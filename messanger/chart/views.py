from django.shortcuts import render
from django.http import JsonResponse
from django.http import Http404, HttpResponseNotAllowed
from django.utils.datastructures import MultiValueDictKeyError

# Create your views here.

chat = {
    "Ivan": ["Hello", "How are you?"],
    "Rinat": ["Goodbye"],
    "Vaselisa": ["Nice to meet you"],
}


def index(request):
    try:
        chat_name = request.GET.get('name')
        msgs = chat[chat_name]
    except (MultiValueDictKeyError, KeyError):
        raise Http404
    return JsonResponse(msgs, safe=False)
