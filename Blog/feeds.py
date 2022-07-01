from django.contrib.syndication.views import Feed
from django.urls import reverse_lazy
from Blog.models import Post
from django.template.defaultfilters import truncatewords


class LastedPostsFeed(Feed):
    title = 'Latest Posts Feed'
    link = reverse_lazy('Blog:post_list')
    description = 'This is A feed For My Projects'
    title_template = 'Test'

    def items(self):
        return Post.published.all()[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.body, 30)

    def item_link(self, item):
        return item.get_absolute_url()