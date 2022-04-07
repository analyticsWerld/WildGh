from django import forms
from accounts.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'fullname': forms.TextInput(attrs={'type': 'text','name':"name","placeholder": "Full Name"}),
            'email': forms.EmailInput(attrs={'name':'email','placeholder':"Email"}),
            'subject': forms.TextInput(attrs={'type': 'text','name':'subject','placeholder':"Subject"}),
            'message' : forms.Textarea(attrs={'name':"subject",'placeholder':"Message",'cols':"30",'rows':'10'})
        }

    
