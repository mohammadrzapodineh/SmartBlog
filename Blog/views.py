from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import SharePostForm
from django.core.mail import send_mail


class PostList(ListView):
    queryset = Post.published.all()
    paginate_by = 1
    context_object_name = 'posts'
    template_name = 'Blog/post_list.html'


def post_detail(request, year, month, day, post_slug):
    post = get_object_or_404(Post,
                             slug=post_slug,
                             status='publish',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day
                             )

    context = {'post': post}
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