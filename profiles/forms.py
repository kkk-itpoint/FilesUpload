from django import forms
from .models import *

class ProfileForm(forms.ModelForm):
    fn = forms.CharField(label = 'First Name')
    ln = forms.CharField(label = 'Last Name')
    # tech = forms.CharField(label = 'Technologies')
    skills = [('python','Python'), ('django', 'Django'), ('mysql', 'MySql'), ('java', 'Java'), ('oracle', 'Oracle'), ('sales force', 'Sales Force'), ('react', 'React'), ('angular', 'Angular'), ('javascript', 'Javascript')]
    tech = forms.ChoiceField(label = 'Skills', choices = skills)
    email = forms.EmailField(label = 'Email ID')
    photo = forms.FileField(label = 'Select Photo')
    
    class Meta:
        model = Info
        fields = '__all__'

    class SearchProfile(forms.Form):
        profile_id = forms.IntegerField()

        