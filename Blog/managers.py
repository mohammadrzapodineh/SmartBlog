from django.db.models import Manager


class BlogManager(Manager):
    def get_queryset(self):
        return super(BlogManager, self).get_queryset().filter(status='publish')