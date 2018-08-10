from django.shortcuts import get_object_or_404, render
from .models import Planner, Event, Offer
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from .forms import OfferForm , PlannerForm
from django.contrib.auth.models import User



def index(request):
    str = "Hello world"
    context = {}
    return render(request, 'events/index.html', context)

@login_required(login_url= 'login')
def details(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    user = request.user
    user_events = user.planner.selectedPlanners.all()
    if event in user_events:
        context = {'event': event}
        return render(request, 'events/details.html', context)
    else:
        return render(request, 'events/details.html', {'error_message': "YOU DON'T HAVE ACCESS TO THIS EVENT"})



@login_required(login_url= "login")
def finder(request):
    user = request.user
    p_events = user.planner.selectedPlanners.all()
    context = {'p_evets': p_events}
    return render(request, 'events/finder.html', context)


def login(request):
    str = "Hello world"
    context = {}
    return render(request, 'events/login-page.html', context)

@login_required(login_url= "login")
def offer (request,event_id):
    if request.method == "POST" :
        form = OfferForm(request.POST)
        event = get_object_or_404(Event, pk=event_id)
        user = request.user
        user_events = user.planner.selectedPlanners.all()
        if form.is_valid() and event in user_events :
            offer = form.save(commit=False)
            offer.event_id = event.id
            offer.planner_id = user.planner.id
            offer.save()
            return  redirect('submit_offer',offer_id = offer.id )
        else :
            return render(request,'events/submit-offer.html',{'error_message':"YOU DON'T HAVE ACCESS TO THIS EVENT"})

    else :
        form = OfferForm()
        event = get_object_or_404(Event, pk=event_id)
        user = request.user
        user_events = user.planner.selectedPlanners.all()
        if event in user_events :
            return render(request , 'events/offer.html' , {'form' : form , 'event' : event})
        else :
            return render(request, 'events/offer.html', {'error_message' : "YOU DON'T HAVE ACCESS TO THIS EVENT"})


@login_required(login_url= "login")
def submit_offer(request, offer_id):
    offer = get_object_or_404(Offer, pk=offer_id)
    user = request.user
    offers = user.planner.offer_set.all()
    if offer in offers:
        context = {'offer' :offer}
        return render(request, 'events/submit-offer.html', context)
    else:
        return render(request, 'events/submit-offer.html', {'error_message': "YOU DON'T HAVE ACCESS TO THIS EVENT"})


@login_required(login_url= "login")
def profile(request):
    planner = request.user.planner
    if request.method == "POST":
        form = PlannerForm(request.POST, request.FILES ,instance=planner )
        if form.is_valid():
            form.save(commit=True)
            return redirect('profile')
    else:
        form = PlannerForm(instance=planner)
        offers = planner.offer_set.all()
    return render(request, 'events/profile-page.html', {'form': form , 'planner':planner , 'offers' : offers})


def logout_view(request):
    logout(request)
    return redirect('index')
