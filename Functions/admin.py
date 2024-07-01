from django.contrib import admin

# Register your models here.

from Functions.models import *

admin.site.register(Services)
admin.site.register(TeamMember)
admin.site.register(Portflolio_Projecrs)
admin.site.register(Pricing)
admin.site.register(PublicMessage)