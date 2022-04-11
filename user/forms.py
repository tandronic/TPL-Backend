from django import forms

from user.models import User


class RegisterForm(forms.ModelForm):
    password_2 = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('email', 'password', 'password_2')

    def clean(self):
        form_data = self.cleaned_data
        if form_data['password'] != form_data['password_2']:
            self._errors["password"] = ["Password do not match"]
            del form_data['password']
        return form_data
