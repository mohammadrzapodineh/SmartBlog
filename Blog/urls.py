from django.urls import path
from . views import PostList, post_detail

app_name = 'Blog'
urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post_slug>/', post_detail, name='post_detail')
]