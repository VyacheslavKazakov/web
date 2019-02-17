from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse


def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
def main(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
def question_details(request, *args, **kwargs):
    question = get_object_or_404(Question, id=slug)
    try:
        answers = question.answer.all()[:]
    except Answer.DoesNotExist:
        answers = []
    return render(request, 'question/question_details.html',
                  {'question': question,
                   'answers': answers,
                  })

@require_GET
def popular(request, *args, **kwargs):
    return HttpResponse('OK')
