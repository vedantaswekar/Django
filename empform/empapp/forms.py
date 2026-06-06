from django import forms

class EmployeeForm(forms.Form):
    ename=forms.CharField(initial="softmusk",disabled=True)
    eno=forms.IntegerField()
    cadd=forms.CharField(widget=forms.Textarea,help_text="only 150 characters")
    gender=forms.CharField(widget=forms.CheckboxInput)
    email=forms.EmailField()
    mobile=forms.IntegerField()
    photo=forms.CharField(widget=forms.FileInput)
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)