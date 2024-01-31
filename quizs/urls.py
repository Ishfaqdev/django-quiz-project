# quiz/urls.py

from django.urls import path
from .views import quiz_view, quiz_result

urlpatterns = [
    path('', quiz_view, name='quiz_view'),
    path('result/', quiz_result, name='quiz_result'),
    # Add other URLs as needed
]
