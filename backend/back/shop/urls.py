from django.urls import path, include

from .views import *

urlpatterns = [
    path('', ProductCardView.as_view()),
    path('lol/<str:slug>', ProductCartWithEmpty.as_view()),
    path('user/', ProfileViews.as_view()),
    path('user/<int:pk>', ProfileKorzinaViews.as_view())
]