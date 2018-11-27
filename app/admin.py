from django.contrib import admin
from app.models import User,Admin,UserFile
# Register your models here.
admin.site.register(User)
admin.site.register(Admin)
admin.site.register(UserFile)