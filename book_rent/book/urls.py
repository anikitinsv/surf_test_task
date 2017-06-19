from django.conf.urls import url
from book.views import BookListView, BookViewDetail

urlpatterns = [
    url(r'^books/$', BookListView.as_view()),
    url(r'^books/(?P<pk>[0-9]+)/$', BookViewDetail.as_view()),
]