from django import forms
from django.core.exceptions import ValidationError
#from django.core.validators import MinValueValidator
from django.contrib.auth.password_validation import password_validators_help_texts, validate_password

from accounts.models import User
from application_events import application_functions as aef




class SignInForm(forms.Form):

    # fields
    email = forms.CharField(
            required=True,
            error_messages={
                'required': 'let\'s have your email address and we\'ll verify how awesome you are.',
                'invalid': 'We appreciate it, but we need you to provide a valid email address.',
                },
            widget=forms.EmailInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'aria-describedby': 'emailHelp',
                    'placeholder': 'email address',
                }), 
            max_length=254,
        )

    password = forms.CharField(
            required=True,
            error_messages={
                'required': 'please provide a password, as our door requires it.',
                },
            widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'aria-describedby': 'password1Help',
                    'placeholder': 'password',
                    }),
        )

    

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)


    def clean(self):
        super(SignInForm, self).clean()
        password = self.cleaned_data.get('password')

        return self.cleaned_data






class SignUpForm(forms.ModelForm):

    # fields
    email = forms.CharField(
            required=True,
            error_messages={
                'required': 'let\'s have your email address and we\'ll take care on everything.',
                'invalid': 'We appreciate it, but we need you to provide a valid email address.',
                },
            widget=forms.EmailInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'aria-describedby': 'emailHelp',
                    'placeholder': 'email address',
                }), 
            max_length=254,
            help_text='we\'ll never share your email with anyone else.'
        )

    password = forms.CharField(
            required=True,
            error_messages={
                'required': 'please provide a password, it will help both of us.',
                },
            widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'aria-describedby': 'password1Help',
                    'placeholder': 'password',
                    }),
            #validators=[validate_password()],
            #help_text=password_validators_help_text_html(),
            help_text='your password must be at least 8 characters long, contain letters and numbers, and must not contain spaces, special characters, or emoji.'
        )

    confirm_password = forms.CharField(
            required=True,
            error_messages={
                'required': 'please provide a password then let\'s make sure with it.',
                },
            widget=forms.PasswordInput(
                attrs={
                    'class': 'form-control form-control-sm',
                    'aria-describedby': 'password2Help',
                    'placeholder': 'confirm password',
                }), 
            #label="Confirm password",
            help_text='let\'s just make sure with your password.'
        )

    

    class Meta:
        model = User
        fields = ['email', 'password', 'confirm_password',]
        #exclude = ['last_login', 'date_joined']


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['email'].validators.append(aef.UniqueEmailSignupValidator)
        self.fields['email'].validators.append(aef.EmailAddressValidator)


    def clean(self):
        super(SignUpForm, self).clean()
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        

        if not not password:
            if validate_password(password) is not None:
                raise forms.ValidationError(_(password_validators_help_texts()), code='password')
            elif password and password != confirm_password:
                self._errors['password'] = self.error_class(['it seems both of your passwords don\'t match.'])

        return self.cleaned_data