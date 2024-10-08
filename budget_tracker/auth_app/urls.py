from django.urls import path
from . import views
from expenses.urls import *

urlpatterns = [
    path("", sign_in, name="register"),

]
