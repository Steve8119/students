from django import forms
from authentication.models import Student

class ParentSignInForm(forms.Form):
    username = forms.CharField(max_length=150)
    admission_number = forms.CharField(max_length=20)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        admission_number = cleaned_data.get("admission_number")

        if not Student.objects.filter(username=username, admission_number=admission_number).exists():
            raise forms.ValidationError("Student with this username and admission number does not exist.")
        return cleaned_data
