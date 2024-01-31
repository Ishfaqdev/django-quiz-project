# quiz/views.py

from django.shortcuts import render
from django.db.models import F, Func
from random import sample
from .models import QuizQuestion

def quiz_view(request):
    # Get 20 random questions
    random_questions = QuizQuestion.objects.order_by('?')[:20]

    return render(request, 'quizs/index.html', {'questions': random_questions})

def quiz_result(request):
    if request.method == 'POST':
        # Handle form submission and evaluate answers
        score = 0
        passing_score = 10  # Adjust as needed

        for question_id in request.POST:
            if question_id.startswith('q'):
                question = QuizQuestion.objects.get(id=int(question_id[1:]))
                selected_option = request.POST[question_id].upper()  # Convert to uppercase

                if selected_option == question.correct_option:
                    score += 1

        result = "Passed" if score >= passing_score else "Failed"

        return render(request, 'quizs/result.html', {'score': score, 'result': result})
    else:
        # Handle non-POST requests, redirect or display an error as needed
        return render(request, 'quizs/error.html')
