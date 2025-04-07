from django import forms
from .models import Register
from .models import Login
from .models import Review
class RegisterForm(forms.ModelForm):  # Corrected to use ModelForm
    class Meta:
        model = Register
        fields = ['name', 'email', 'password']  # Changed 'username' to 'name'

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['email','password']



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review']
