
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import Index, Contacto, Institucional
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index, name='index'),
    path('contacto/', Contacto, name='contacto'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('noticia/', include('apps.noticia.urls')),
    path('usuario/', include('apps.usuario.urls')),
    path('comentario/', include('apps.comentario.urls')),
   path('institucional/', Institucional, name='inst'),
    path('carrousel/', include('apps.carrousel.urls')),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)