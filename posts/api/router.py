from rest_framework.routers import DefaultRouter
from  posts.api.viewR import PostModelViewSet

router_post = DefaultRouter()
#registramos nuestras rutas
router_post.register(prefix="posts", basename="posts", viewset=PostModelViewSet)