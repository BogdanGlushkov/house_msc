from django.shortcuts import render

from .models import Docs
from .models import Event
from .models import Jobs
from .models import Partner
from .models import lendingLinks


def index(request):
    event_1 = Event.objects.get(id=1)
    event_1_oldprice = round(event_1.price * 100 / (100 - event_1.procents))
    event_2 = Event.objects.get(id=2)
    event_2_oldprice = round(event_2.price * 100 / (100 - event_2.procents))
    event_3 = Event.objects.get(id=3)
    event_3_oldprice = round(event_3.price * 100 / (100 - event_3.procents))
    links = lendingLinks.objects.get(id=1)

    event_1_about = [event_1.link1, event_1.link2, event_1.link3, event_1.link4, event_1.link5, event_1.link6,
                     event_1.link7, event_1.link8]
    event_2_about = [event_2.link1, event_2.link2, event_2.link3, event_2.link4, event_2.link5, event_2.link6,
                     event_2.link7, event_2.link8]
    event_3_about = [event_3.link1, event_3.link2, event_3.link3, event_3.link4, event_3.link5, event_3.link6,
                     event_3.link7, event_3.link8]
    return render(request, 'main/index.html',
                  {'event_1': event_1, 'event_1_oldprice': event_1_oldprice, 'event_2': event_2,
                   'event_2_oldprice': event_2_oldprice, 'event_3': event_3, 'event_3_oldprice': event_3_oldprice,
                   'event_1_about': event_1_about, 'event_2_about': event_2_about,
                   'event_3_about': event_3_about, 'links': links})


def rules(request):
    return render(request, 'main/rules.html')


def documents(request):
    doc = Docs.objects.all()
    return render(request, 'main/docs.html', {'doc': doc})


def contacts(request):
    return render(request, 'main/contacts.html')


def buy(request):
    return render(request, 'main/buy.html')


def coop(request):
    jobs = Jobs.objects.all()
    return render(request, 'main/coop.html', {'jobs': jobs})


def partner(request):
    partner = Partner.objects.all()
    return render(request, 'main/partner.html', {'partner': partner})
