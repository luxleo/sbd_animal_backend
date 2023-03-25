from django.urls import path, re_path
from django.views.generic import TemplateView
from .views import user_view, workout_views, bulletinBoard_views

app_name = "beastTamers"

urlpatterns = [
    # admin users and application users view
    path(
        "",
        TemplateView.as_view(template_name="beastTamers/base.html"),
        name="index_template",
    ),
    re_path(r"^users|FAQ|^workouts/*", user_view.redirect_view),
    path(
        "is_authenticatied/", user_view.CheckAuth.as_view(), name="check_authenticated"
    ),
    path("whoami/", user_view.InitialWhoAmI.as_view(), name="whoami"),
    path("set_csrf/", user_view.set_csrf_token, name="set_csrf"),
    path("login/", user_view.LoginView.as_view(), name="admin_login"),
    path("logout/", user_view.LogoutView.as_view(), name="admin_logout"),
    path("api/users/", user_view.get_all_users, name="user_list"),
    path("api/user/<int:pk>/", user_view.user_detail, name="user_detail"),
    # workout type view
    path("api/workouts/", workout_views.workout_types, name="workout_type_list"),
    path(
        "api/workout/<int:pk>/", workout_views.workout_type, name="workout_type_detail"
    ),
    path("api/inqueries/", bulletinBoard_views.inquery_list, name="inquery_list"),
    path(
        "api/inquery/<int:pk>/",
        bulletinBoard_views.inquery_detail,
        name="inquery_detail",
    ),
    path("api/inquery/reply/", bulletinBoard_views.reply_view, name="reply_views"),
]
