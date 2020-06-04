from django.contrib import admin
from testApp.models import blorejobs,chennaijobs,punejobs,hydjobs

# Register your models here.
class hydjobsAdmin(admin.ModelAdmin):
    list_display=['date','company','tittle','eligibility','address','email',]

class blorejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','tittle','eligibility','address','email',]

class chennaijobsAdmin(admin.ModelAdmin):
    list_display=['date','company','tittle','eligibility','address','email',]

class punejobsAdmin(admin.ModelAdmin):
    list_display=['date','company','tittle','eligibility','address','email',]

admin.site.register(hydjobs,hydjobsAdmin)
admin.site.register(blorejobs,blorejobsAdmin)
admin.site.register(chennaijobs,chennaijobsAdmin)
admin.site.register(punejobs,punejobsAdmin)
