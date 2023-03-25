from django.urls import path
from . import views

app_name = "bulletin_board"

urlpatterns = [
    path("inquery/", views.user_inquery_view, name="user_inquery_list"),
    path(
        "inquery/<int:pk>/", views.user_inquery_detail_view, name="user_inquery_detail"
    ),
    path("inquery/reply/", views.post_inquery_reply, name="post_reply"),
]
