from django.contrib import admin
from posts.models import Post #Importando la clase

@admin.register(Post) #Se está mandando al panel del Administrado
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','create_at'] #para indicar que campos se indiquen en la tabla donde se muestra la info dentro de la pestaña admin
    
    
