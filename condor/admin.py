from django.contrib import admin
from .models import User, Agent, Condor, UserProfile,Category

# Register your models here.
admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Condor)
admin.site.register(UserProfile)
admin.site.register(Category)
