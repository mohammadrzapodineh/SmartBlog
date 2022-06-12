from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404, redirect, get_list_or_404
from .models import Post
from .forms import SharePostForm, CommentForm
from taggit.models import Tag
from django.core.mail import send_mail
from django.db.models import Count

class PostList(ListView):
    paginate_by = 6
    context_object_name = 'posts'
    template_name = 'Blog/post_list.html'
    def get_queryset(self):
        object_list = Post.published.all()
        tag_slug = self.kwargs.get('tag')
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            object_list = object_list.filter(tags__in=[tag])
            tags = self.request.GET.get('tags')
            if tags:
                tag_list = get_list_or_404(Tag, slug__in=[tags])
                object_list = object_list.filter(tags__in=tag_list)
            
        return object_list
    def get_context_data(self):
        context = super(PostList, self).get_context_data()
        tag_slug = self.kwargs.get('tag')
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            context['tag'] = tag
        return context
        
def post_detail(request, year, month, day, post_slug):
    post = get_object_or_404(Post,
                             slug=post_slug,
                             status='publish',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day
                             )
    comment_form = CommentForm(data=request.POST or None)
    comments = post.comments.filter(active=True)
    tags = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.get_similar_posts_by_tags(tags=tags, post_id=post.id).annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]
    new_comment = None
    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.post = post
        new_comment.save()
        new_comment = True

    context = {'post': post, 'comments': comments, 'comment_form': comment_form, "similar_posts": similar_posts}
    return render(request, 'Blog/post_detail.html', context)


def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='publish')
    share_form = SharePostForm(data=request.POST or None)
    sent = False
    if share_form.is_valid():
        comment = share_form.cleaned_data.get('comment')
        to = share_form.cleaned_data.get('to')
        subject = f'You Get A  Share Post {post.title}'
        post_url = request.build_absolute_uri(post.get_absolute_url())
        message = f'please See This Post {post_url} your Comments {comment}'
        send_mail(subject, message, 'admin@Smartblog.com', [to])
        sent = True
    context = {'post': post, 'form': share_form, 'sent': sent}
    return render(request, 'Blog/post_share.html', context)