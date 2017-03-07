from django.conf.urls import url
from experiments import views
from drf_chunked_upload.views import ChunkedUploadView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^experiments/$', views.ExperimentList.as_view()),
    url(r'^experiments/(?P<pk>[0-9]+)/$', views.ExperimentDetail.as_view()),
    # url(r'^experiments/(?P<pk>[0-9]+)/uploads/$', views.FileUpload.as_view()),
    url(r'^uploads/$', views.FileUploadList.as_view()),
    url(r'^uploadchunks/$', ChunkedUploadView.as_view()),
    url(r'^uploadchuncks/(?P<pk>.*)/$', views.UploadChunksDetail,
        name='chunkedupload-detail'),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
