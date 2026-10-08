from django.urls import path

from .views import (
    home,
    register_page,
    login_page,
    profile_page,
    logout_page,
    hello_api,
    registration_api,
    registration_detail_api
)


urlpatterns = [

    # ==================================================
    # HOME PAGE
    # ==================================================

    path(
        '',
        home,
        name='home'
    ),


    # ==================================================
    # REGISTRATION PAGE
    # ==================================================

    path(
        'register/',
        register_page,
        name='register'
    ),


    # ==================================================
    # LOGIN PAGE
    # ==================================================

    path(
        'login/',
        login_page,
        name='login'
    ),


    # ==================================================
    # USER PROFILE / DETAILS
    # ==================================================

    path(
        'profile/',
        profile_page,
        name='profile'
    ),


    # ==================================================
    # LOGOUT
    # ==================================================

    path(
        'logout/',
        logout_page,
        name='logout'
    ),


    # ==================================================
    # TEST API
    # ==================================================

    path(
        'hello/',
        hello_api,
        name='hello'
    ),


    # ==================================================
    # REGISTRATION API
    # ==================================================

    path(
        'api/registrations/',
        registration_api,
        name='registrations'
    ),


    # ==================================================
    # SINGLE REGISTRATION API
    # ==================================================

    path(
        'api/registrations/<int:id>/',
        registration_detail_api,
        name='registration_detail'
    ),
]