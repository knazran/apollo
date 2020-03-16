from django import forms
from django.forms import ModelForm, widgets
from django.forms.widgets import Select
from base.models import ShuttleCheckIn

class ShuttleCheckInForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ShuttleCheckInForm, self).__init__(*args, **kwargs)
        self.fields['staff_id'].required = True
    
    def clean(self):
        print("CLEAN")
        cleaned_data = super().clean()
        staff_id = cleaned_data.get('staff_id')
        if len(staff_id) < 7:
            raise forms.ValidationError("Invalid Staff ID")
        print("CLEAN1")
        # return staff_id

    class Meta:
        model = ShuttleCheckIn
        fields = ['staff_id']
        labels = {'staff_id': 'Staff ID'}
