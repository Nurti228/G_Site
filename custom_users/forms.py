# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models

GENDER_TYPE = (
    ("MALE", "М"),
    ("FEMALE", "Ж")
)


class CustomUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, initial='+996', label="Укажите номер телефона")
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE, required=True)
    source = forms.CharField(required=False, label="Откуда вы узнали про нас")
    country = forms.CharField(required=True, label="Откуда вы?")
    family = forms.CharField(required=False, widget=forms.HiddenInput, label="Семейное положение")
    education = forms.CharField(required=False, label='Уровень образования')
    language = forms.CharField(required=False, label='Количество языков, которыми владеете')

    class Meta:
        model = models.CustomUser  # Fix the attribute name
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'phone_number',
            'date_of_birth',
            'gender',
            'source',
            'country',
            'family',
            'education',
            'language'
        )

    def save(self, commit=True):
        user = super(CustomUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
