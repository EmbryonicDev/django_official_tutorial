from django.contrib import admin
from .models import Question, Choice


class QuestionAdmin(admin.ModelAdmin):
    # Fields without using fieldset format
    # fields = ["pub_date", "question_text"]

    # Using fieldset format.
    # 1st field in tuple is title
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
