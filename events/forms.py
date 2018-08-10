from django import  forms
from  .models import Offer , Planner

class OfferForm(forms.ModelForm) :
    class Meta :
        model = Offer
        fields = ['price' , 'description']


class PlannerForm(forms.ModelForm) :
    class Meta :
        model = Planner
        fields = ['name' ,'email','mobile','website','logo']


