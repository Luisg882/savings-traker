from django import forms
from django.contrib.auth.models import User
from .models import Profile, SavingPot
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field

# Form to create new user
class CustomSignupForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('nominated_bank_account', 'main_balance')
    
    
    def signup(self, request, user):
        user.email = self.cleaned_data['email']
        user.save()

        profile = Profile(
            user=user,
            slug=user.username,
            age=0,  
            email=user.email,
            nominated_bank_account=self.cleaned_data['nominated_bank_account'],
            main_balance=self.cleaned_data['main_balance']
        )
        profile.save()
        return user

# Form to add Money in the user Main Balance    
class AddMoney(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('main_balance',)

    def __init__(self, *args, **kwargs):
        super(AddMoney, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_show_labels = False
        
# Form to open new Saving Pot
class OpenNewPot(forms.ModelForm):
    class Meta:
        model = SavingPot
        fields = ('name',)

# Form to move money to saving pot
class AddMoneySavingPot(forms.ModelForm):
    class Meta:
        model = SavingPot
        fields = ('balance',)