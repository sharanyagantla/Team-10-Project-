
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm) :
	email = forms.EmailField(required = True, widget=forms.TextInput(attrs={ 'required': 'true' }))
	first_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={ 'required': 'true' }))
	last_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={ 'required': 'true' }))

	class Meta:
		model = User
		fields = ('username','first_name' ,'last_name' , 'email' , 'password1' , 'password2')

	def save(self , commit= True):
		user = super(MyRegistrationForm, self).save(commit= False)	
		user.first_name = self.cleaned_data['first_name']
		self.fields['first_name'].required = True
		user.last_name = self.cleaned_data['last_name']
		if commit:
			user.save()
		return user