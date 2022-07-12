from django.db.models import Manager
from django.db.models import Count


class BlogManager(Manager):
    def get_queryset(self):
        return super(BlogManager, self).get_queryset().filter(status='publish')
    
    def get_similar_posts_by_tags(self, tags, post_id=None):
        # if This Function has A post id Removed From QuerySet !
        if post_id:
            return self.get_queryset().filter(tags__in=tags).exclude(id=post_id).distinct()
        return self.get_queryset().filter(tags__in=tags).distinct()
    
    def get_last_posts(self):
        return self.get_queryset().order_by('-publish')

    def get_popular_posts(self, count=5):
        return self.get_queryset().annotate(total_comments=Count('comments')).order_by('-total_comments').exclude(total_comments=0).distinct()[:count]