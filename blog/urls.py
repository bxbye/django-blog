from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path(route='all-posts/', view=views.all_posts, name='all_posts'),
    # Other URL patterns
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
