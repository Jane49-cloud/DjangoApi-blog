from rest_framework import generics, permissions, viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .serializers import (
    BlogCreateSerializer, BlogSerializer, BlogDetailSerializer,
    CategorySerializer, CategoryDetailSerializer, AuthorSerializer, AuthorDetailSerializer,
    CommentSerializer,CategoryCreateSerializer
)
from .models import Blog, Category, Author, Comment

class CreateBlogView(generics.CreateAPIView):
    serializer_class = BlogCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        author, created = Author.objects.get_or_create(user=user)
        serializer.save(author=author)

class BlogsListView(generics.ListAPIView):
    serializer_class = BlogSerializer

    @method_decorator(cache_page(60*2))  # Cache for 2 minutes
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

    queryset = Blog.objects.filter(published=True).select_related('author', 'category').prefetch_related('comments')

class AllBlogsListView(generics.ListAPIView):
    serializer_class = BlogSerializer
    
    @method_decorator(cache_page(60*2))  # Cache for 2 minutes
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)
    queryset = Blog.objects.all().select_related('author', 'category').prefetch_related('comments')

class BlogDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BlogDetailSerializer
    queryset = Blog.objects.all().select_related('author', 'category').prefetch_related('comments')

class CreateCategoryView(generics.CreateAPIView):
    serializer_class = CategoryCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class CategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all().prefetch_related('category_blogs')

class UpdateCategoryView(generics.UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

class AuthorListView(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()

class AuthorDetailsView(generics.RetrieveDestroyAPIView):
    serializer_class = AuthorDetailSerializer
    queryset = Author.objects.all()

class CommentViewset(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
