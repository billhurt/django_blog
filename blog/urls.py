from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = "blog"

urlpatterns = [
    path('', TemplateView.as_view(template_name="blog/index.html"), name='index'),
    path('posts/', views.PostsView.as_view(), name='posts'),
    path('contactme/', views.ContactMeView.as_view(), name="contactme"),
    path('contactme/thanks/', TemplateView.as_view(template_name="blog/thanks.html"), name="thanks"),
    path('<slug:slug>/', views.post_detail, name="post_detail"),
]
