from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),
    path('category/',category,name='category'),
    path('contact/',Contact.as_view(),name='contact'),
    path('listing/',Listing.as_view(),name='listing'),
    path('misol/',misol,name='misol')
]
