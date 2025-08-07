from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import DailyNote

from .forms import DailyNoteForm
import requests

from django_smart_ratelimit import rate_limit
from django.http import JsonResponse

from django_smart_ratelimit import rate_limit

@rate_limit(key='ip', rate='10/m')
def public_api(request):
    return JsonResponse({'message': 'Hello World'})


def home(request):

    if request.method == "POST":

        form = DailyNoteForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("home")

    else:

        form = DailyNoteForm()

    notes = DailyNote.objects.all()

    return render(request, "index.html", {"myForm": form, "myNotes": notes})
