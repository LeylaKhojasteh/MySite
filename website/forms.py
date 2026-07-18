from django import forms
from website.models import Contact, Newsletter


class NameForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField( max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'



class NewsletterForm(forms.ModelForm):

    class Meta:
        model = Newsletter
        fields = '__all__'
