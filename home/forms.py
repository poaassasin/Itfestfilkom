from django import forms
from . import models


class UsersForm(forms.Form):
    nama = forms.CharField(max_length=65)
    utusan = forms.CharField(max_length=65)
    email = forms.CharField(max_length=65, widget=forms.EmailInput)
    wa_number = forms.CharField(max_length=65)
    password1 = forms.CharField(max_length=65, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=65, widget=forms.PasswordInput)
        
    def clean(self):
        cleaned_data = super(UsersForm, self).clean()
        password = cleaned_data.get("password1")
        confirm_password = cleaned_data.get("password2")

        if password != confirm_password:
            raise forms.ValidationError(
                "Password tidak sama"
            )
        email_input = cleaned_data.get('email')
        if models.UserItfess.objects.filter(email=email_input).exists():
            raise forms.ValidationError("Email sudah terdaftar.")

        

class LoginForm(forms.Form):
    email = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class userItFessForm(forms.ModelForm):
    class Meta:
        model = models.UserItfess
        fields = [
            "email",
            "utusan",
            "nama",
            "wa_number"
        ]

    def __init__(self, *args, **kwargs):
        super(userItFessForm, self).__init__(*args, **kwargs)


class memberForm(forms.ModelForm):
    class Meta:
        model = models.Member
        fields = [
            "user",
            "nama",
            "email"
        ]
        widgets = {
            "user": forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(memberForm, self).__init__(*args, **kwargs)
        self.fields["user"].queryset = models.UserItfess.objects.all()
