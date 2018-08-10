from django.contrib import admin
from .models import Event , Offer , Planner

class EventAdmin(admin.ModelAdmin) :
    fields = ['name' , 'type','date_and_time','address','pud_date','duration','details','expcted_cpacity'
              ,'max_price','status','planner','selectPlanners']
    readonly_fields  = ['status','planner',]
    
admin.site.register(Event, EventAdmin)


class OfferAdmin(admin.ModelAdmin) :
    fields = ['price' , 'description','planner','event','status']
    readonly_fields  = ['price','description','planner','event','status']
    
admin.site.register(Offer, OfferAdmin)
    
class PlannerAdmin(admin.ModelAdmin) :
    fields = ['name' ,'user', 'email','mobile','address','category','type','website','logo']
    
admin.site.register(Planner, PlannerAdmin)
