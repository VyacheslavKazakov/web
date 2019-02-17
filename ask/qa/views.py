from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page


@require_GET
def home(request):
    questions = Question.objects.new()
    page = paginate(request, questions)
    baseurl = '/?page='
    return render(request, 'base.html', {'questions': page.object_list,
                                         'baseurl': baseurl,
                                         'page': page,})

@require_GET
def popular(request):
    questions = Question.objects.popular()
    page = paginate(request, questions)
    baseurl = '/popular/?page='
    return render(request, 'base.html', {'questions': page.object_list,
                                         'baseurl': baseurl,
                                         'page': page,})

@require_GET
def test(request, *args, **kwargs):
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
                   'answers': answers,})
