from django import forms
#from captcha.fields import ReCaptchaField
#from captcha.widgets import ReCaptchaV2Checkbox

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Your name',
        'class': 'form-control'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Your email',
        'class': 'form-control'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Your message',
        'class': 'form-control',
        'rows': 5
    }))
 #   captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())