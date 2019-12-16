from . import views
from django.urls import path
from . views import models_relationship
urlpatterns = [
              path('', views.models_relationship, 
          	  name = 'models_relationship')
    ]