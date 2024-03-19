from django import forms
from .models import Student


class submitdata(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
