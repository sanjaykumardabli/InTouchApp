from django import forms
from todolist_app.models import Details


class TaskForm(forms.ModelForm):
    class Meta :
        model = Details
        widgets = {
            'firstName': forms.TextInput(attrs={'placeholder': 'Enter your First Name'}),
            'lastName': forms.TextInput(attrs={'placeholder': 'Enter your Last Name'}),
            'displayName': forms.TextInput(attrs={'placeholder': 'Enter your Nick Name'}),
            'emailAddress': forms.TextInput(attrs={'placeholder': 'Enter your Email Address'}),
            'homePhone': forms.TextInput(attrs={'placeholder': 'Enter your Phone Number'})}
        fields = ['firstName', 'lastName',  'displayName', 'emailAddress', 'homePhone' ]
        labels = {
            'firstName': 'First Name',
            'lastName': 'Last Name',
            'displayName': 'Display Name',
            'emailAddress' : 'Email Address',
            'homePhone' : 'Home Phone'
        }

    #
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['homePhone'].required = False
        self.fields['emailAddress'].required = False



