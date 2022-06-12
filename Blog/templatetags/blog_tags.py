from Blog.models import Post
from django import template
import markdown
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()

@register.inclusion_tag('include/post_list_component.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.get_last_posts()[:count]
    context = {'latest_posts': latest_posts}
    return context

@register.simple_tag(name='pouplar_posts')
def get_most_posts_by_comment(count=3):
    query = Post.published.get_pouplar_posts()[:count]
    return query 


@register.filter(name='markdown')
def markdown_formater(text):
    return mark_safe(markdown.markdown(text))
