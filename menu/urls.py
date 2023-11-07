from django.urls import path
from . import views

app_name = 'menu'
urlpatterns = [
    path(route='all-items/', view=views.all_items, name='all_items'),
    # Other URL patterns
]