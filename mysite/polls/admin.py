from django.contrib import admin
from .models import Question, Choice

"""
More efficient way to change admin page title.
By using the below line of code you don't have
to copy base_site.html from Django root dir
"""
# admin.site.site_header = "My Polls Administration"

# Stacked view that is not efficient with space
# in this instance:
# class ChoiceInline(admin.StackedInline):

# Tabular view


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": [
         "pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
