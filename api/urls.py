from django.conf.urls import url, include
from api.views import MeasurementListAPIView, UserListCreate

urlpatterns = [
    url(r'measurements/', MeasurementListAPIView.as_view(), name='Measurements'),
    url(r'signup/', UserListCreate.as_view(), name='list_create'),
    url('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # url(r'^token-auth/', views.obtain_auth_token),
    # url(r'^auth/', include('rest_framework.urls')),
]


