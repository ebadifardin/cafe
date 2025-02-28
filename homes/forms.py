from django import forms

class PollCreateForm(forms.Form):
    name=forms.CharField(label="name")
    email=forms.EmailField( label="email")
    message=forms.CharField(label="message")