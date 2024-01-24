from django.shortcuts import render
from django.http import HttpResponse
from .utils import get_weather, context_data


def forecast(request):
    return HttpResponse("done")


def index(request):
    data = context_data
    if request.method == "POST":
        query = request.POST.get("query")
        # context_data = get_weather(query)
        return render(request, "main.html",  data)
    # return render(request, "index.html")
    return render(request, "main.html",  data)
