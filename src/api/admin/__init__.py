import inspect
import sys
from django.contrib import admin

for name, obj in inspect.getmembers(sys.modules['src.api.models']):
    if inspect.isclass(obj):
        admin.site.register(obj)
