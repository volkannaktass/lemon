from django import forms
from .models import Article,Comment
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["commoncourses","lessons","title","about","content","article_image"]



#class CommentForm(forms.ModelForm):

 #   class Meta:
  #      model = Comment
   #     fields = ('comment_author', 'comment_content')