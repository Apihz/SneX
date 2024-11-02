from django.urls import path, re_path
from Account import api
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('signup/', api.signup, name='signup'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', api.me, name='me'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
