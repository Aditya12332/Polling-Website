from django.contrib import admin
from .models import Question, Choice


admin.site.register(Choice)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ("question_text", "publish_date", "was_published_recently")
    search_fields = ["question_text"]  # Adds a search bar for questions

admin.site.register(Question, QuestionAdmin)