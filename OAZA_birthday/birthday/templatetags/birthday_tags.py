from django.template import Library
from datetime import datetime
from birthday.models import Person
from django.db.models import Q

register = Library()

@register.inclusion_tag('tags/show_birthdays_people.html')
def show_birthdays_people():
    today = datetime.now()
    oaza_ending_date = datetime(year=2023, month=6, day=16)

    if today.month > oaza_ending_date.month:
        people = Person.objects.filter(
            Q(birthday__month__gt=oaza_ending_date.month) |
            (Q(birthday__month=oaza_ending_date.month) & Q(birthday__day__gte=oaza_ending_date.day)),
            Q(birthday__month__lt=today.month) |
            Q(birthday__month=today.month) & Q(birthday__day__lte=today.day),
            chocolate_received=False
        )
    else:
        people = Person.objects.filter(
            (Q(birthday__month__gte=oaza_ending_date.month) & Q(birthday__day__gt=oaza_ending_date.day)) |
            (Q(birthday__month__lt=today.month) | Q(birthday__month=today.month) & Q(birthday__day__lte=today.day)),
            chocolate_received=False
        )

    return {'people': people}