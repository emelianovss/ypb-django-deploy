from django.contrib import admin
from files.models import MyModel


@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    pass
