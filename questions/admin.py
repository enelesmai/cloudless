from django.contrib import admin

# Register your models here.
from .models import Project, Tag, Member, Project_Member, Question, Status, Question_Image, Question_Tag, Comment

class MemberInLine(admin.TabularInline):
	model = Project.members.through
	extra = 0
	
class ProjectAdmin(admin.ModelAdmin):
	inlines = [MemberInLine]
	
class QMemberInLine(admin.TabularInline):
	model = Question.members.through
	extra = 0
	
class ImagesInLine(admin.TabularInline):
	model = Question_Image
	extra = 0
	
class TagsInLine(admin.TabularInline):
	model = Question_Tag
	extra = 0

class CommentsInLine(admin.TabularInline):
	model = Comment
	extra = 0

class QuestionAdmin(admin.ModelAdmin):
	inlines = (
		QMemberInLine,
		ImagesInLine,
		TagsInLine,
		CommentsInLine,
	)
	
admin.site.register(Member)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tag)
admin.site.register(Question, QuestionAdmin)