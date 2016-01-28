from django.conf.urls import patterns, include, url

from views import (
    user_list_view,
    user_detail_view,

    photo_detail_view,
    photo_upload_view,
)

urlpatterns = patterns(
    '',
    # index page
    url(r'^$', user_list_view, name='user-list'),

    # user viewn
    url(r'users/(?P<pk>\d+)$', user_detail_view, name='user-detail'),

    #individual photo view
    url(r'photos/(?P<pk>\d+)$', photo_detail_view, name='photo-detail'),

    # todo: a view to upload photos
    url(r'^photos/upload$', photo_upload_view, name='photo-upload-view'),
)
