from django import forms

from .models import Article, ArticleDeleteRequest, Comment, Images,Files
from django.forms.widgets import ClearableFileInput

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["commoncourses","lessons","title","about","content","using_status"]



#class CommentForm(forms.ModelForm):

 #   class Meta:
  #      model = Comment
   #     fields = ('comment_author', 'comment_contentclass ImageForm(forms.ModelForm):


class ImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ["article_image"]
        widgets = {
            'article_image': ClearableFileInput(attrs={'multiple': True}),
        }


class FileForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ["myFile"]
        widgets = {
            'myFile': ClearableFileInput(attrs={'multiple': True}),
        }

class ArticleDeleteRequestForm(forms.ModelForm):
    class Meta:
        model = ArticleDeleteRequest
        fields = ["request_author","email","request_content"]
