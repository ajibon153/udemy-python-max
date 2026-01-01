from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

monthly_challenges = {
    "january": "Eat no meat for entire month",
    "february": "work out for at least 20 minutes every day",
    "march": "learn python for at least 20 minutes every day",
    "april": "read at least one book",
    "may": "go for a walk every day",
    "june": "meditate for 10 minutes daily",
    "july": "write in a journal every day",
    "august": "drink 2 liters of water daily",
    "september": "learn a new skill",
    "october": "practice gratitude daily",
    "november": "limit social media usage",
    "december": "reflect on the year and set goals",
}


def index(request):
    list_items = ""
    months = monthly_challenges.keys()

    for month in months:
        # reverse is if the url changes in future, reference to its name
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href='{month_path}'>{month.capitalize()}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if (month > len(months)):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    # if the url changes in future, reference to its name
    redirect_path = reverse("month-challenge", args=[redirect_month])
    # reference to its path
    return HttpResponseRedirect(f"/challenges/{redirect_month}")
    # return HttpResponse(month)


def monthly_challenge(request, month):
    challange_text = None
    if month in monthly_challenges:
        challange_text = monthly_challenges[month]
        return HttpResponse(challange_text)
    else:
        return HttpResponseNotFound("This month is not supported")

    return HttpResponse(challange_text)
