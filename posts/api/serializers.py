from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from posts.models import Post

class PostSerializer (ModelSerializer):
    class Meta:
        model = Post
        #especificamos los datos que queremos utilizar
        fields = ["title", "description1", "create_at"]
        #fields = '__all__' #para escoger todos los elementos
        