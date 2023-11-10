from django.urls import path, include
from .views import ShortyCBView, shorty_redirect, HomeView

urlpatterns = [
    path('index/', HomeView.as_view(), name='home' ),
    path('<slug:slug>/', shorty_redirect, name="shorty"),
    path('view-2/<slug:slug>/', ShortyCBView.as_view()),
]