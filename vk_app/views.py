import json

from django.shortcuts import render, redirect
from django.urls import reverse

from django.views import View

import vk

from .forms import RegisterForm
from .models import Access
from .scripts.config import scope, VKApiVersion


def get_friends():
    token = Access.objects.latest('token').token
    session = vk.Session(access_token=token)
    api = vk.API(session)
    user = api.users.get(user_ids=Access.objects.values()[0]['user_id'], v=VKApiVersion)[0]['first_name']
    friends = api.friends.get(user_ids=Access.objects.values()[0]['user_id'], v=VKApiVersion)
    json_data = json.dumps(friends)
    data = json.loads(json_data)['items'][:5]
    friends_list = []
    for friend in data:
        friends_list.append(api.users.get(user_ids=friend, v=VKApiVersion)[0]['first_name'])
    return {'user': user, 'friends_list': friends_list}


class Index(View):
    def get(self, request):
        if not Access.objects.all():
            if request.session.get('authorized'):
                del request.session['authorized']
            return redirect('register')
        elif not request.session.get('authorized'):
            return redirect('login')
        friends = get_friends()
        return render(request, 'vk_app/index.html', friends)

    def post(self, request):
        print(request.POST['value'])
        del request.session['authorized']
        if request.POST['value'] == 'exit':
            return redirect('login')
        Access.objects.all().delete()
        return redirect('register')

class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'vk_app/register.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                session = vk.AuthSession(
                    app_id=request.POST['app_id'],
                    user_login=request.POST['username'],
                    user_password=request.POST['password'],
                    scope=scope
                )
            except Exception:
                return redirect('register')
            # print(dir(session))
            print('access_token', session.access_token)
            print('app_id', session.app_id)
            Access(
                token=session.access_token,
                user_id=request.POST['user_id'],
                app_id=request.POST['app_id']
            ).save()
            return redirect('login')


class Login(View):
    def get(self, request):
        if not Access.objects.all():
            if request.session.get('authorized'):
                del request.session['authorized']
            return redirect('register')
        elif not request.session.get('authorized'):
            return render(request, 'vk_app/login.html')
        return redirect('index')

    def post(self, request):
        vk.Session(access_token=Access.objects.latest('token').token)
        request.session['authorized'] = 'authorized'
        return redirect('index')
