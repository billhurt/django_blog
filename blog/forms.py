from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
from .models import Comment

class ContactForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = "./thanks"
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-secondary'))

    name = forms.CharField(label="Name", widget=forms.TextInput(attrs={'style':'max-width: 20em', 'class': 'text-bg-dark p-1'}), max_length=100)
    email = forms.EmailField(label="Email", widget=forms.EmailInput(attrs={'style':'max-width: 20em', 'class': 'text-bg-dark p-1'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'style':'max-width: 40em', 'class': 'text-bg-dark p-1'}), label="Your message", max_length=400)
    captcha = ReCaptchaField(label="", widget=ReCaptchaV2Checkbox(attrs={'data-theme': 'dark'}))
    

class CommentForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = ""
        self.helper.form_method = 'POST'
    
    class Meta:
        model = Comment
        fields = ['name', 'body']
        widgets = {
         'name': forms.TextInput(attrs={'class': 'text-bg-dark p-1'}),
         'body': forms.Textarea(attrs={'class': 'text-bg-dark p-1'}),
         }


    