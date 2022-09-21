from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):

    def test_coment_body_is_required(self):
        form = CommentForm({'body': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('body', form.errors.keys())
        self.assertEqual(form.errors['body'][0], 'This field is required.')


    def test_years_riding_default_is_working(self):
        form = CommentForm({'body': 'my comment', 'years_riding': 0})
        self.assertTrue(form.is_valid())
    

    def test_form_fields_are_explicit_in_form_metaclass(self):
        form = CommentForm()
        self.assertTrue(form.Meta.fields, ['body', 'years_riding'])