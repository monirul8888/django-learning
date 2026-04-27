from django.contrib import admin
from django.urls import path
from home.views import *
from vege.views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path("recipe/", recipe, name="recipe"),
    path('about/', about, name='about'),
    path("contact/", contact, name="contact"),
    path('admin/', admin.site.urls),
]

# Add this only once, at the end
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)