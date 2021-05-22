import uuid
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Url


def index(request):
    return render(request, "index.html")


def short(request):
    if request.method == "POST":
        url_link = request.POST["link"]
        uid = str(uuid.uuid4())[:5]
        new_url = Url(link=url_link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)


def go(request, pk):
    url_details = Url.objects.get(uuid=pk)
    return redirect(url_details.link)
