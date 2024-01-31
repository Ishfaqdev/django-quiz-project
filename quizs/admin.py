from django.contrib import admin
from .models import QuizQuestion

class QuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option')
    search_fields = ('question', 'correct_option')
    list_filter = ('correct_option',)

admin.site.register(QuizQuestion, QuizQuestionAdmin)
