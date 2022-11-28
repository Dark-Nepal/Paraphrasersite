from django.shortcuts import render
from datetime import datetime
from .models import Site
from .forms import ContactForm


def home(request):

    # listing query of paraphraser sites 
    sites = Site.objects.all()

    # form data handling and storing

    if request.method == 'POST':
        filledform = ContactForm(request.POST)
        if filledform.is_valid():
           note = 'Message is sent !!'
           filledform.sent_date = datetime.now()
           filledform.save()
           newform = ContactForm()

           return render(request, 'index.html',{ 'sites':sites, 'form':newform, 'note': note })
    
    else:
        newform = ContactForm()
        return render(request, 'index.html',{ 'sites':sites, 'form':newform })