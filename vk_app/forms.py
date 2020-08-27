from django import forms


class RegisterForm(forms.Form):
    app_id = forms.CharField(label="Введите id приложения в VK", max_length=40)
    user_id = forms.CharField(label="Введите id пользователя в VK", max_length=40)
    username = forms.CharField(label="Введите email или номер телефона", max_length=40)
    password = forms.CharField(label="Введите пароль", widget=forms.PasswordInput)
