from django.shortcuts import render, get_object_or_404
from .models import Question, Choice

def index(request):
    """View for the question index page."""
    latest_questions = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'latest_questions': latest_questions})

def detail(request, question_id):
    """View for the question detail page."""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    """View for displaying results of a particular question."""
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    """View for handling voting."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return render(request, 'polls/results.html', {'question': question})
