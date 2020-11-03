from django import forms 
#created form that has subject recipient and message
class ContactForm(forms.Form):
    recipient = forms.EmailField(required = True)
    subject = forms.CharField(required = True)
    message = forms.CharField(widget=forms.Textarea, required = True)
