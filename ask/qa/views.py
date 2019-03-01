from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from qa.models import Question, Answer
from qa.forms import AnswerForm, AskForm


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if not 0 < limit <=100:
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
    return paginator, page


@require_GET
def home(request):
    questions = Question.objects.new()
    paginator, page = paginate(request, questions)
    paginator.baseurl = "{}?page=".format(reverse('home'))
    return render(request, 'base.html', {'questions': page.object_list,
                                         'paginator': paginator,
                                         'page': page,})

@require_GET
def popular(request):
    questions = Question.objects.popular()
    paginator, page = paginate(request, questions)
    paginator.baseurl = "{}?page=".format(reverse('popular'))
    return render(request, 'base.html', {'questions': page.object_list,
                                         'paginator': paginator,
                                         'page': page,})

@require_GET
def test(request, *args, **kwargs):
    return HttpResponse('OK')


def question_details(request, slug, *args, **kwargs):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = answer.get_url()
            return HttpResponseRedirect(url)
    else:
        question = get_object_or_404(Question, id=slug)
        form = AnswerForm()
        try:
            answers = question.answer_set.all()
        except Answer.DoesNotExist:
            answers = []
        return render(request, 'question/question_details.html',
                                      {'question': question,
                                       'answers': answers,
                                       'form': form})


def ask_question(request, *args, **kwargs):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
        return render(request, 'ask.html', {'form': form})
