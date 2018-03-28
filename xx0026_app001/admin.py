from django.contrib import admin

# Register your models here.
from xx0026_app001.models import Topic, Webpage, AccessRecord

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)