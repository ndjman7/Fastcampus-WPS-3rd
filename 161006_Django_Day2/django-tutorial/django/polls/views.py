from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question


def index(request):
    # 가장 최근의 Question 5개를 가져온다
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # 장고 템플릿 폴더에서 index.html파일을 가져온다
    template = loader.get_template('index.html')
    # 템플릿을 렌더링 할 때 사용할 변수 dictionary
    context = {
        'latest_question_list': latest_question_list
    }
    # Http형식으로 응답을 돌려준다. 내용은 template을 context와 request를 사용해서 렌더링한 결과
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)