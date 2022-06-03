from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from .models import Post


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

