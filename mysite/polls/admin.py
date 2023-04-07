from django.contrib import admin
from .models import Question, Choice

for x in [Question, Choice]:
    admin.site.register(x)
