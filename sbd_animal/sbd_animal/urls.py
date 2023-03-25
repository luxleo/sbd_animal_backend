from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("sbd_animal.accounts.urls")),
    path("workout/", include("sbd_animal.work_out.urls")),
    path("bulletin_board/", include("sbd_animal.bulletinBoard.urls")),
    path("beastTamers/", include("sbd_animal.beastTamers.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    import debug_toolbar

    urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
