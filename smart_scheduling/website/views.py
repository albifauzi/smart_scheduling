from collections import defaultdict
from datetime import timedelta, time, datetime, date
from pprint import pprint

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils import timezone

from smart_scheduling.apps.instructors.models import Instructor

from .forms import InstructorForm


def index(request: HttpRequest) -> HttpResponse:
    instructors = Instructor.objects.all()

    context = {
        'instructors': instructors
    }
    return render(request, 'index.html', context)


def registration(request: HttpRequest) -> HttpResponse:
    form = InstructorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('website:thanks')

    context = {
        'form': form
    }

    return render(request, 'registration.html', context)


def schedule(request: HttpRequest) -> HttpResponse:

    TIMES = (
        (1, '08.00-09.00'),
        (2, '09.00-10.00'),
        (3, '10.00-11.00'),
        (4, '11.00-12.00'),
        (5, '12.00-13.00'),
        (6, '13.00-14.00'),
        (7, '14.00-15.00'),
        (8, '15.00-16.00')
    )

    schedule = defaultdict(dict)
    exclude_instructor_ids = []
    for day in Instructor.DAYS_CHOICES:
        instructors = Instructor.objects.filter(days__contains=day[0]).exclude(id__in=exclude_instructor_ids).order_by('created')
        schedule[day[1]] = defaultdict(dict)
        for instructor in instructors:
            instructor.time_count = 0
            for time in TIMES:
                if type(schedule[day[1]][time[1]]) != str:
                    if instructor.time_count < instructor.hour:
                        schedule[day[1]][time[1]] = instructor.name
                        instructor.time_count += 1
                    else:
                        exclude_instructor_ids.append(instructor.id)

    for value in schedule:
        schedule[value] = dict(schedule[value])

    context = {
        'times': TIMES,
        'days': Instructor.DAYS_CHOICES,
        'schedule': dict(schedule)
    }

    return render(request, 'schedule.html', context)


def thanks(request: HttpRequest) -> HttpResponse:
    return render(request, 'thanks.html', {})
