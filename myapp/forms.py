from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms
from .models import Class
from .models import Quiz, Question, Option


class RegisterForm(UserCreationForm):
    # Add the 'role' field to the form
    role = forms.ChoiceField(
        choices=CustomUser.ROLE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500'
        }),
        label='Select your role'
    )

    class Meta:
        model = CustomUser  # Use the CustomUser model instead of the default User model
        fields = ['username', 'email', 'password1', 'password2', 'role']  # Include 'role' in the fields
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter your username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter your email'
            }),
            'password1': forms.PasswordInput(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter your password'
            }),
            'password2': forms.PasswordInput(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Confirm your password'
            }),
        }

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name']  # Customize with any fields you want to edit
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter your username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter your email'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter your first name'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'border border-gray-300 rounded-lg p-2 w-full focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Enter your last name'
            }),
        }

#New-------------------------------------------
class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'description', 'max_students']

#Di pako sure kung email
class InviteStudentForm(forms.Form):
    student_username = forms.CharField(label="Student Username", max_length=150)

#Eto bago----------------------------------------------------------------------
class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'description', 'assigned_class', 'schedule', 'timer']


class QuestionForm(forms.ModelForm):
    QUESTION_TYPES = [
        ('MC', 'Multiple Choice'),
        ('TF', 'True or False'),
        ('ID', 'Identification'),
    ]

    question_type = forms.ChoiceField(choices=QUESTION_TYPES, widget=forms.Select)

    class Meta:
        model = Question
        fields = ['text', 'question_type', 'correct_answer']

class OptionForm(forms.ModelForm):
    class Meta:
        model = Option
        fields = ['question', 'text']