

from . import models
from django import forms

class EmpLog(forms.Form):
    emp_id = forms.IntegerField()
    pswd = forms.CharField(max_length = 30)




class EmpEntry(forms.ModelForm):

    class Meta:
        model = models.Employee
        exclude = ['sal']
        

class EmpUpFrm(forms.ModelForm):

    id = forms.IntegerField(disabled =True)
    class Meta:
        model = models.Employee
        exclude = ['sal', 'id']
    
