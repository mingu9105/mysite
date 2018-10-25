# from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question, Choice
from django.utils import timezone

def add_question(request):
    text = request.POST['text']

    q = Question(question_text=text,
                 pub_date=timezone.now())
    q.save()
    return HttpResponse('입력완료')

def vote(request):
    choice = request.POST['choice']
    c = Choice.objects.get(pk=choice)
    c.votes = c.votes + 1
    c.save()

    return render(request, 'polls/vote.html', {})

def detail(request, id):
    question = Question.objects.get(id=id)
    return render(request, 'polls/detail.html', {'item' : question})
def index(request):
    list = Question.objects.all()
    return render(request, 'polls/index.html', {'question' : list})

def data(request, email, number):
    value = request.GET['user_name']
    return HttpResponse(value + email + str(number))

def quest(request):
    return render(request, 'polls/quest.html', {})

def result(request, id):
    question = Question.objects.get(pk=id)
    return render(request, 'polls/result.html', {'question' : question})