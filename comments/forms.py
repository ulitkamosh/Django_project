from django import forms

from comments.models import Comment


class CommentForm(forms.Form):
    class Meta:
        model = Comment

    comment_area = forms.CharField(
        label="",
        widget=forms.Textarea
    )
