from django import forms
from datetime import datetime


from .models import Todo

class RawTodoForm(forms.Form):
    year = forms.IntegerField(initial=2020,max_value=2030,min_value=2000)
    month = forms.IntegerField(initial=datetime.now().month,max_value=12,min_value=1)
    day = forms.IntegerField(initial=datetime.now().day,max_value=31,min_value=1)

    # class Meta:
    #     model = Todo
    #     fields = [
    #         'year',
    #         'month',
    #         'day'
    #     ]
