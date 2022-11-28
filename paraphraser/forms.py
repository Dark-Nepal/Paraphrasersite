from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ( 'fullname', 'email', 'phone', 'message')

    def __init__(self,*args,**kwargs):
        super(ContactForm,self).__init__(*args, *kwargs)
        self.fields['fullname'].widget.attrs['placeholder'] = 'DarkNepal'
        self.fields['email'].widget.attrs['placeholder'] = 'darknepal@mail.com'
        self.fields['phone'].widget.attrs['placeholder'] = '9779827189078'
        self.fields['message'].widget.attrs['placeholder'] = 'Leave a message ...'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'