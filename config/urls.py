"""
URL configuration for config project.
"""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    # ==================================================
    # DJANGO ADMIN
    # ==================================================

    path(
        'admin/',
        admin.site.urls
    ),


    # ==================================================
    # REGISTRATION APPLICATION
    # ==================================================

    path(
        '',
        include('registration.urls')
    ),

]