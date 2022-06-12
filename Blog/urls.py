from django.urls import path
from . views import PostList, post_detail, post_share

app_name = 'Blog'
urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('tag/<slug:tag>/', PostList.as_view(), name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post_slug>/', post_detail, name='post_detail'),
    path('<int:post_id>/share/', post_share, name='post_share'),
]