from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

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
    "december": None,
    # "december": "reflect on the year and set goals",
}


def index(request):
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })
    # for month in months:
    #     # reverse is if the url changes in future, reference to its name
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f"<li><a href='{month_path}'>{month.capitalize()}</a></li>"

    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if (month > len(months)):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    # if the url changes in future, reference to its name
    redirect_path = reverse("month-challenge", args=[redirect_month])
    # reference to its path
    return HttpResponseRedirect(f"/challenges/{redirect_path}")
    # return HttpResponse(month)


def monthly_challenge(request, month):
    challange_text = None
    if month in monthly_challenges:
        challange_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html",  {
            "text": challange_text,
            "month_name": month
        })
        # response_data = render_to_string(
        #     "challenge.html", {"month": month, "text": challange_text})
        # return HttpResponse(response_data)
    else:
        # raise Http404()
        response_data = render_to_string("404.html")
        return HttpResponseNotFound(response_data)
