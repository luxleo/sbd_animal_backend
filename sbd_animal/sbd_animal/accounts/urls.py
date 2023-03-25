from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="sign_up"),
    path(
        "verification_code/",
        views.send_signup_verification_code,
        name="signup_verification_code",
    ),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.logout, name="logout"),
    path("test_access_code/", views.test_access_code, name="test_access_code"),
    path("profile/", views.user_profile, name="profile"),
]
