from django.contrib import admin

from .models import Child, Family, Parent, ResetPassword

# Register your models here.
admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(Family)
admin.site.register(ResetPassword)
