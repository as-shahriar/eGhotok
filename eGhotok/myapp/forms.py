from django import forms
from django.contrib.auth.models import User
from myapp.models import UserInfo

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = ('username','email','password')
        help_texts = {
            'username': None,
            'email': None,
        }

        widgets = {'username':forms.TextInput(attrs={'class':'form-control mb-2' , 'placeholder':'Username','id':'username','required':'',}),
                   'email':forms.TextInput(attrs={'class':'form-control mb-2', 'placeholder':'Email','id':'email','required':'','type':'email'}),
                   'password':forms.PasswordInput(attrs={'class':'form-control mb-2', 'placeholder':'Password','id':'password','required':'',})}

class UserInfoForm(forms.ModelForm):
    class Meta():
        model = UserInfo
        fields =("name","fb","insta","cell","age","gender","address","city","education_level" ,"education_field","work_as","work_in" ,"religion",'pic')
        widgets = {"name":forms.TextInput(attrs={'class':'form-control','placeholder': 'Full Name'}),
                   "fb":forms.URLInput(attrs={'class':'form-control','placeholder': 'https://www.facebook.com/yourId'}),
                   "insta":forms.TextInput(attrs={'class':'form-control','placeholder': 'https://www.instagram.com/yourId'}),
                   "cell":forms.TextInput(attrs={'class':'form-control','placeholder': 'Mobile No'}),
                   "age":forms.TextInput(attrs={'class':'form-control','placeholder': 'Age' }),
                   "gender":forms.TextInput(attrs={'class':'form-control','placeholder': 'Gender' }),
                   "address":forms.TextInput(attrs={'class':'form-control','placeholder': 'Address'}),
                   "city":forms.TextInput(attrs={'class':'form-control','placeholder': 'City'}),
                   "education_level":forms.TextInput(attrs={'class':'form-control','placeholder': 'Education Level'}),
                   "education_field":forms.TextInput(attrs={'class':'form-control','placeholder': 'Education Field'}),
                   "work_as":forms.TextInput(attrs={'class':'form-control','placeholder': 'Work As'}),
                   "work_in" :forms.TextInput(attrs={'class':'form-control','placeholder': 'Work In'}),
                   "religion":forms.TextInput(attrs={'class':'form-control','placeholder': 'Religion'}),}
