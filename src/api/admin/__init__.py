import inspect
import sys
import os

from django.contrib import admin
from django.db.models.signals import post_migrate
from django.contrib.auth import get_user_model

admin.site.site_header = 'BI-server Admin'
User = get_user_model()

class UserModelAdmin(admin.ModelAdmin):
    exclude = ('password', 'email')

for name, obj in inspect.getmembers(sys.modules['src.api.models']):
    if inspect.isclass(obj):
        admin.site.register(obj, UserModelAdmin)

def add_initial_super_admin(sender, **kwargs):
    if User.objects.count() == 0:
        print('Creating a superAdmin')
        User.objects.create_superuser(
            username=os.getenv('SUPER_NAME'),
            email=os.getenv('SUPER_EMAIL'),
            password=os.getenv('SUPER_PASS')
        )

post_migrate.connect(add_initial_super_admin)
