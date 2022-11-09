""" Loads forms from django"""
from django import forms
from .models import Comment
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    """ Sets Meta for form.
    """
    class Meta:
        """ Form fields set to body and years riding.
        """
        model = Comment
        fields = ('body', 'years_riding',)


class CommentDeleteForm(forms.ModelForm):

    class Meta:

        model = Comment
        fields = ('user_removed',)