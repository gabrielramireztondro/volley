from django.urls import path
from login.views import login_view, signup, secret_page, SecretPage

urlpatterns = [
    path('', login_view, name='login'),
    path('signup/', signup, name='signup'),
    path('secret/', secret_page, name='secret'),
    path('secret2/',SecretPage.as_view(), name='secret2'),
]