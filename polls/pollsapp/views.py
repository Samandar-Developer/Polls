from django.shortcuts import render, get_object_or_404
from .models import Question, Vote
from django.template import loader
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

# Create your views here.

# To send a question to the index.html


def index(request):
    latest_question_list = Question.objects.order_by("-pub_time")[:5]
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context=context)


# Show the results page

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Page does not exist 😭")

    return render(request, "polls/details.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.vote_set.get(pk=request.POST['choice'])
    except (KeyError, Vote.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('pollsapp:results', args=(question.id,)))
