from django.contrib import admin

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_display = ["qn_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["qn_text"]
    fieldsets = [
        (None, {"fields": ["qn_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

# Register your models here.
