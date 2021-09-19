from django import forms
from .models import Jasoseol

class JssForm(forms.ModelForm):

    class Meta:
        model = Jasoseol
        fields = ('title', 'content',)

    def __init__(self, *args, **kwargs):
        #super = 부모클래스 있는 거 갖다 쓸 수 있다.
        super().__init__(*args, **kwargs)
        self.fields['title'].label = '제목'
        self.fields['content'].label = '자기소개서 내용'
        self.fields['title'].widget.attrs.update({
            'class':'jss_title',
            'placeholder':'제목',
        })