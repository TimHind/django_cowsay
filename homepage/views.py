from django.shortcuts import render, HttpResponseRedirect, reverse
from homepage.models import Cow
from homepage.forms import CowSay
import subprocess

def cow_view(request):
    """ Help from Detrich """
    if request.method == "POST":
        form = CowSay(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cowsay = Cow.objects.create(
                cow = subprocess.check_output(["cowsay", str(data.get("text"))]).decode(),
                text = data.get("text"),       
            )
            return render(request, "cow.html", {"form": form, "phrases": cowsay})
    form = CowSay()
    return render(request, "cow.html", {"form": form})

def history_view(request):
   cow = Cow.objects.order_by('-id')[0:10]
   return render(request, "history.html", {"cow": cow})

