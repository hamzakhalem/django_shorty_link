from django.urls import path, include
from .views import ShortyCBView, shorty_redirect

urlpatterns = [
    path('<slug:slug>/', shorty_redirect),
    path('view-2/<slug:slug>/', ShortyCBView.as_view()),
]