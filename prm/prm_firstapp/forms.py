from django import forms
from django.forms import fields
from django.forms.fields import EmailField
from django.forms.widgets import HiddenInput
from django.core import validators
from prm_firstapp.models import Salary

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("NAME NEEDS TO START WITH Z")
class employeeForm(forms.Form):
    # creating fields
    #name = forms.CharField(validators = [check_for_z]) # one way of adding validations
    name = forms.CharField()
    belt_A = forms.IntegerField()
    belt_B = forms.IntegerField()
    belt_C = forms.IntegerField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again')
    # hidden fields
    # botcatcher not actually required

    #botcatcher = forms.CharField(required=False, widget=HiddenInput, validators =[validators.MaxLengthValidator(0)] ) #multiple validators can be passed in the list

    # create a custom validator - this is basically not used a lot
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']
        if len(botcatcher)>0:
            # means that a robot tried to scrap our page - so raise an error
            raise forms.ValidationError("GOTCHA BOT")
        return botcatcher
    # using Django's core built in validator - just add another parameter - validators as above

    # single clean method for all
    def clean(self):
        all_clean = super().clean()
        email = all_clean['email']
        vmail = all_clean['verify_email']
        if email != vmail:
            raise forms.ValidationError('EMAILS SHOULD MATCH')

    # creating custom validators using Django's built in validators
    # let's say we have to ensure that the name starts with z - we use the methos created outside the class to validate this
"""""
Connecting models and forms
"""""
class NewUserForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = '__all__'