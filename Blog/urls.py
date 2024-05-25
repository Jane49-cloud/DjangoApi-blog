from django.urls import path
from rest_framework import routers
from . import views

router=routers.DefaultRouter()
router.register(r'comments', views.CommentViewset)

urlpatterns = [

    path("blogs" , views.BlogsListView.as_view()),
    path("blogs/all" , views.AllBlogsListView.as_view()),
    path("blogs/create" , views.CreateBlogView.as_view()),
    path("blogs/<int:pk>" , views.BlogDetailsView.as_view()),
    path("authors" , views.AuthorListView.as_view()),
    path("author/<int:pk>" , views.AuthorDetailsView.as_view()),
    path("categories" , views.CategoryListView.as_view()),
     path("categories/create" , views.CreateCategoryView.as_view()),
    path("category/<int:pk>" , views.CategoryDetailsView.as_view()),
]
urlpatterns+=router.urls