from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Question,Response,StudentBuffer

class CreateUserForm(forms.ModelForm):
    class Meta:
        model=StudentBuffer
        fields=['name','age','standard','username','password','school']
class NewQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title','body']
        widgets = {'title':forms.TextInput(attrs={'autofocus':True,'placeholder':'Enter a title for your question'})}
 

class NewResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['body']
        widgets={
            'body':forms.Textarea(attrs={'rows':7,'placeHolder':'What are your thoughts?'})
        }
       

class NewReplyForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['body']
        widgets={
            'body':forms.Textarea(attrs={'rows':2,'placeHolder':'What are your thoughts?'})
        }