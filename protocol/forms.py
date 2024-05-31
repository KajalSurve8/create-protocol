from django.forms import forms
from .models import ProtocolNew, TestTable2, SampleId
from django.forms import ModelForm
from django import forms

class pageoneform(ModelForm):
    class Meta:
        model=ProtocolNew
        exclude=['serial','protocolid']
        
        widgets = {
            'mfg_date': forms.widgets.DateInput(attrs={'type': 'date'}), 
            'exp_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'study_start_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'effective_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'date_of_release': forms.widgets.DateInput(attrs={'type': 'date'}),
                          
        }
        
class pagetwoform(ModelForm):
    class Meta:
        model=TestTable2
        exclude=['serial','protocolid','test','formulation']
        widgets = {
            'testselect': forms.widgets.CheckboxInput(),    
        }




