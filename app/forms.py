from django import forms
from .models import booking

class bookingform(forms.ModelForm):
    class Meta:
        model=booking
        fields=['name','fromto','destination','phno','email']
