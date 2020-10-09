from django.contrib import admin
from .models import Register,Items,Contact,Cart

# Register your models here.
admin.site.register(Items)
admin.site.register(Register)
admin.site.register(Contact)
admin.site.register(Cart)