from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'published_date', 'status', 'image', 'caption']  # Add more fields if needed

        def __init__(self, *args, **kwargs):
            user = kwargs.pop('user')  # Remove 'user' from kwargs
            super(PostForm, self).__init__(*args, **kwargs)
            self.fields['author'].initial = user
