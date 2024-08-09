# from django import forms
# class PostForm(forms.Form):
#     title = forms.CharField(label='제목', max_length=10)
#     content = forms.CharField(label='내용', widget=forms.Textarea)

from django.forms import ModelForm
from second.models import Post
from django.utils.translation import gettext_lazy as _

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': _('제목'),
            'content': _('내용'),
        }
        help_texts = {
            'title': _('제목을 입력해 주세요'),
            'content': _('내용을 입력해 주세요')
        }
        error_messages = {
            'name': {
                'max_length': _("10까지 입력가능합니다")
            }
        }