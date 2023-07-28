from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from django.views.generic.edit import FormView
from django.views.generic.detail import SingleObjectMixin
from .models import Post, Comment
from django.template import loader
from .forms import ContactForm, CommentForm
from django.core.mail import send_mail
from django.urls import reverse

# Create your views here.

class PostsView(generic.ListView):
    model = Post
    template_name = "blog/posts.html"
    context_object_name = "latest_blog_posts"
    paginate_by = 10

    def get_queryset(self):
        """Return the last fifty blog posts."""
        return Post.objects.order_by("-created_at")


def post_detail(request, slug):
    template_name = "blog/post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_at")
    new_comment = None
    # Comment posted
    if request.method == "POST":
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

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )

    
class ContactMeView(FormView):
    
    template_name = "blog/contact_me.html"
    form_class = ContactForm
    success_url = "./thanks/"
    
    def form_valid(self, form):
        name=form.cleaned_data.get('name')
        email=form.cleaned_data.get('email')
        message=f'CONTACT FORM MSG billhurt.com \n\n' + form.cleaned_data.get('message')
        send_mail(
            subject=f'{name} has sent a message',
            message=message,
            from_email=email,
            recipient_list=['william.hurt6@gmail.com'],
        )
        return super(ContactMeView, self).form_valid(form)





