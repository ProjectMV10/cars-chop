from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views


urlpatterns = [
    path('categoria_productos/<int:id>', views.VerCategoriasProducto, name='categoria_productos')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)