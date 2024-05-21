from rest_framework import generics, permissions,viewsets
from . import serializers, models





class BlogsListView(generics.ListAPIView):
    serializer_class=serializers.BlogSerializer
    queryset = models.Blog.objects.filter(published=True)


class BlogDetailsView(generics.RetrieveDestroyAPIView):
    serializer_class=serializers.BlogDetailSerializer
    queryset = models.Blog.objects.filter(published=True)



class CategoryListView(generics.ListAPIView):
    serializer_class=serializers.CategorySerializer
    queryset = models.Category.objects.all()


class CategoryDetailsView(generics.RetrieveDestroyAPIView):
    serializer_class=serializers.CategoryDetailSerializer
    queryset = models.Category.objects.all()


class AuthorListView(generics.ListAPIView):
    serializer_class=serializers.AuthorSerializer
    queryset = models.Author.objects.all()


class AuthorDetailsView(generics.RetrieveDestroyAPIView):
    serializer_class=serializers.AuthorDetailSerializer
    queryset = models.Author.objects.all()    


class CommentViewset(viewsets.ModelViewSet):
     serializer_class=serializers.CommentSerializer
     queryset =models.Comment.objects.all()