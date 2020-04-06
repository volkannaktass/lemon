from django import forms
from .models import Article
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["commoncourses","lessons","title","about","content","article_image"]
