from django.views.decorators.csrf import csrf_exempt
from .models import Event
from .forms import EventForm, EditEventForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import Http404
from django.http import JsonResponse
from django.core.exceptions import SuspiciousOperation
from django.contrib.auth.decorators import login_required
from user.models import User


@login_required(login_url='login')
def event(request, id):
    try:
        event = Event.objects.prefetch_related('participants').get(pk=id)
    except Event.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = EditEventForm(request.POST, user=request.user, id=event.user_id)
        if form.is_valid():
            Event.objects.update_or_create(pk=id, defaults=form.cleaned_data)
            return redirect('events')
    else:
        form = EditEventForm(initial={
            'date': event.date,
            'title': event.title,
            'description': event.description,
        }
        )

    return render(request, 'event/event.html', {'form': form, 'event': event})


@login_required(login_url='login')
@csrf_exempt
def participation(request, id):
    if request.method != 'POST':
        raise Http404

    if not 'going' in request.POST:
        raise SuspiciousOperation("Invalid request 'going' must be defined")

    try:
        event = Event.objects.prefetch_related('participants').get(pk=id)
    except Event.DoesNotExist:
        raise Http404

    if request.POST['going'] == '0':
        event.participants.remove(request.user)
    else:
        event.participants.add(request.user)

    return JsonResponse({'success': True})


@login_required(login_url='login')
def events(request):
    events_list = Event.objects.select_related('user').prefetch_related('participants').all()
    paginator = Paginator(events_list, 10)
    return render(
        request,
        'event/events.html',
        {
            'events': paginator.get_page(request.GET.get('page')),
        }
    )


@login_required(login_url='login')
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            Event.objects.create(user=request.user, **form.cleaned_data)
            return redirect('events')
    else:
        form = EventForm()

    return render(request, 'event/event-form.html', {'form': form})
