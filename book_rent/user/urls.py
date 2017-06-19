from django.conf.urls import url, include
from user.views import RentUserList, RentUserDetail
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^users/$', RentUserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', RentUserDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^get-auth-token/', obtain_auth_token),
]