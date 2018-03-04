from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from accounts.forms import SignUpForm, SignInForm
from accounts.models import User
from paperless_mails.models import EmailSubscriber



def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if not form.is_valid():
                #print('invalid')
                #print(form.errors)
                #messages.add_message(request, messages.ERROR, 'There was some problems while creating your account. Please review some fields before submiting again.')
                return render(request, 'accounts/signup.html', { 'forms': form })

            else:
                # check for terms of services
                # if user agree in terms then proceed
                #if request.POST['tosCheckBox']:
                    email = form.cleaned_data.get('email')
                    password = form.cleaned_data.get('password')

                    # create record for this user
                    # auto subscriber for now
                    User.objects.create_user(password=password, email=email)
                    EmailSubscriber.objects.create(email=email)

                    # authenticate then login
                    user = authenticate(email=email, password=password)
                    login(request, user)
                    return redirect('application_events:thanksfor', thanks_for = 'registered')

        else:
            return render(request, 'accounts/signup.html', { 'forms': SignUpForm() })



def signin(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    else:
        if request.method == 'POST':
            form = SignInForm(request.POST)
            if not form.is_valid():
                return render(request, 'accounts/login.html', { 'forms': form, 'unregistereduser': False })

            else:
                # check for terms of services
                email = form.cleaned_data.get('email')
                password = form.cleaned_data.get('password')

                # authenticate then login
                user = authenticate(email=email, password=password)
                if user is not None:
                    #print('authenticated')

                    if user.is_active:
                        login(request, user)
                        return redirect('/') 
                else:
                    #print('who\'s this user')
                    return render(request, 'accounts/login.html', { 'forms': form, 'unregistereduser': True })

                #return redirect('application_events:thanksfor', thanks_for = 'welcome-first')

        else:
            return render(request, 'accounts/login.html', { 'forms': SignInForm(), 'unregistereduser': False })



def signout(request):
    logout(request)
    return redirect('application_events:thanksfor', thanks_for = 'pinningwithus')
