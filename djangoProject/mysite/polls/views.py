from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import subject

def index(request: HttpRequest):
    return render(request, "index.html", {"test": "this is my template"})

def index1(request):
    # this is like doing a select * from subject
    subjectlist = subject.objects.all()
    print(subjectlist)

    # printing out all the subjects
    for x in subjectlist:
        print(f"Subject: {x.subject} Freq: {x.frequency_s}")
    return render(request, "page 1.html", {"test": "this is my p1", "subjects": subjectlist})

def index2(request):
    return render(request, "page 2.html", {"test": "this is my p2"})

def index3(request):
    return render(request, "page 3.html", {"test": "this is my p3"})

def index4(request):
    return render(request, "page 4.html", {"test": "this is my p4"})


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "mamma mia %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)