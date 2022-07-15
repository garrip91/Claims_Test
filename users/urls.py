from django.urls import path

from users.views import ThanksView, RegistrationView

urlpatterns = [
    path('thanks/', ThanksView.as_view(), name='thanks'),
    path('registration/', RegistrationView.as_view(), name='registration'),
]
