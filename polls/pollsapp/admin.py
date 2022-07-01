from django.contrib import admin
from .models import Question, Vote
# Register your models here.
admin.site.site_header = "Polls Admin"
admin.site.site_title = "Polls admin"
admin.site.index_title = "Polls administration"


class VoteInline(admin.TabularInline):
    model = Vote
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
                 ('Date Information', {'fields': ['pub_time'], 'classes': ['collapse']}), ]
    inlines = [VoteInline]


# admin.site.register(Question)
# admin.site.register(Vote)
admin.site.register(Question, QuestionAdmin)
