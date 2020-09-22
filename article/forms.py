from django import forms

from .models import Article, ArticleDeleteRequest, Comment, Images


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


class ArticleDeleteRequestForm(forms.ModelForm):
    class Meta:
        model = ArticleDeleteRequest
        fields = ["request_author","email","request_content"]
