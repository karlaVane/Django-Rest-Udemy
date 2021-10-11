from rest_framework.views import APIView #GET-POST-DELETE
from rest_framework.response import Response
from rest_framework import serializers, status
from posts.models import Post
from rest_framework.viewsets import ViewSet, ModelViewSet
from posts.api.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly #Tipos de permisos
from posts.api.permissions import IsAdminOrReadOnly

class PostModelViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly] #Se puede agregar varios permisos pero separar con comas dentro de la lista
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    #http_method_names =['get']

#class PostViewSet(ViewSet):
#    def list (self, request):
#        serializer = PostSerializer(Post.objects.all(), many=True)
#        return Response(status=status.HTTP_200_OK, data=serializer.data)
#
#    #Función para obtener solo un elemento que se encuentra en la bd
#    def retrieve (self, request, pk:int):
#        post = PostSerializer(Post.objects.get(pk=pk))
#        return Response(status=status.HTTP_200_OK, data = post.data)
#
#    def create (self, request):
#        serializerP = PostSerializer(data = request.POST)
#        serializerP.is_valid(raise_exception=True)
#        serializerP.save()#Para guardar en la base de datos
#        return Response(status = status.HTTP_200_OK, data= serializerP.data)

#class PostApiView(APIView):
#    def get (self, request):
#        #posts =[post.title for post in Post.objects.all()]
#        serializer = PostSerializer(Post.objects.all(), many=True)
#        return Response(status=status.HTTP_200_OK, data=serializer.data)
#
#    def post (self, request):
#        #Post.objects.create(title=request.POST['title'], description1=request.POST["description1"])
#        #return self.get(request)
#        serializerP = PostSerializer(data = request.POST)
#        serializerP.is_valid(raise_exception=True)
#        serializerP.save()#Para guardar en la base de datos
#        return Response(status = status.HTTP_200_OK, data= serializerP.data)

## Enrutar la view en url principal 