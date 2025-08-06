from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import DailyNote

from .forms import DailyNoteForm

from django_ratelimit.decorators import ratelimit
@ratelimit(key='ip', rate='10/m', block=True)
def my_view(request):
    return render(request, 'crm/templates/index.html')




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
