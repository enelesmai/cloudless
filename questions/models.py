from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Status(models.Model):
	name = models.CharField(max_length=20)
	def __str__(self):
		return self.name
		
class Member(models.Model):
	name = models.CharField(max_length=50)
	apellido1 = models.CharField(max_length=50)
	apellido2 = models.CharField(max_length=50)
	User = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	foto = models.BinaryField(blank=True)
	def __str__(self):
		return self.name + " " + self.apellido1 + " " + self.apellido2
	
class Tag(models.Model):
	text = models.CharField(max_length=50)
	def __str__(self):
		return self.text
	
class Project(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=500)
	members = models.ManyToManyField(Member, through='Project_Member') 
	def __str__(self):
		return self.name
	
class Project_Member(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	def __str__(self):
		return self.project.name + ' - ' + self.member.name

class Question(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	status = models.ForeignKey(Status, on_delete=models.CASCADE, default='Pendiente')
	question_text = models.CharField(max_length=200)
	pubdate = models.DateTimeField('date published')
	members = models.ManyToManyField(Member, through='Question_Member') 
	def __str__(self):
		return self.question_text
	
class Question_Image(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	image = models.BinaryField(blank=False)
	
class Question_Tag(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

class Question_Member(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	member = models.ForeignKey(Member, on_delete=models.CASCADE)

class Comment(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	member = models.ForeignKey(Member, on_delete=models.CASCADE)
	comment_text = models.CharField(max_length=500)
	pubdate = models.DateTimeField('date published')
	def __str__(self):
		return self.comment_text

class Comment_Image(models.Model):
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
	image = models.BinaryField(blank=False)