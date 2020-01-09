from urllib.parse import quote_plus
from django.views import generic
from .models import Post,PostPicture
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404

from .utils import get_read_time , count_words


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


    # def post_list(request):

    #     query = request.GET.get("q")
    #     if query:
    #         queryset = queryset.filter(title_icontains=query)

    



# class PostDetail(generic.DetailView):
#     model = Post
#     template_name = 'post_detail.html'

def post_detail(request, slug):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    share_string = quote_plus(post.content)
    comments = post.comments.filter(active=True)
    new_comment = None

    
    
    print(count_words(post.content))
    print(get_read_time(post.content))
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form,
                                           'share_string' : share_string }
    ) 