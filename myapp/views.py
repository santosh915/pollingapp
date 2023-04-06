from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from.models import Question,Choice

# Create your views here.
def index(request):
    question_text = Question.objects.all()
    return render(request,'index.html',{'questions':question_text})

def vote(request,pk):
    question_text = Question.objects.get(id=pk)
    options = question_text.choices.all()
    if request.method == 'POST':
         inputvalue = request.POST['choice']
         selection_option = options.get(id=inputvalue)
         selection_option.vote += 1
         selection_option.save()

    return render(request, 'vote.html', {'question':question_text, 'options': options })

def result(request,pk):
    question_text = Question.objects.get(id=pk)
    options = question_text.choices.all()
    if request.method == 'POST':
        inputvalue = request.POST['choice']
        selection_option = options.get(id=inputvalue)
        selection_option.vote += 1
        selection_option.save()
    return render(request, 'result.html', {'question': question_text, 'options': options})





