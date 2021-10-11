from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from user.models import User

@admin.register(User)

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {"fields":('username','password')}), #cada linea es un bloque
        ('Información personal', {"fields":("first_name","last_name","email")}),
        ('Permisos',{"fields": ('is_active','is_staff', 'is_superuser','groups', 'user_permissions')}),
        ('Redes Sociales', {'fields':('web_site', 'twitter')})
    )

#Si se quiere obtener todos los campos dejar a la clase creada con un pass
