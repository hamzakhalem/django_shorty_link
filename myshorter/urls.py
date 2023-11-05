from django.urls import path, include
from .views import ShortyCBView, shorty_redirect

urlpatterns = [
    path('view-1', shorty_redirect),
    path('view-2', ShortyCBView.as_view()),
]