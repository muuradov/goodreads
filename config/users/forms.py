
from .models import CustomUser
from django import forms


class UserCreateForm(forms.Form):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'gender', 'password')



    def save(self, commit=True):
        user = super().save(commit)
        user.set.password(self.cleaned_data['password'])
        user.save()
        gender = user.gender
        if gender == 'male':
            user.profile_picture = 'profile_pictures/download.png'
        else:
            user.profile_picture = 'profile_pictures/download.png'
        user.save()

        return user



