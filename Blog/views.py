from rest_framework import generics, permissions,viewsets
from . import serializers, models





class CreateBlogView(generics.CreateAPIView):
    serializer_class = serializers.BlogCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    
    def perform_create(self, serializer):
        user = self.request.user
        author, created = models.Author.objects.get_or_create(user=user)
        serializer.save(author=author)

class BlogsListView(generics.ListAPIView):
    serializer_class=serializers.BlogSerializer
    queryset = models.Blog.objects.filter(published=True)

class AllBlogsListView(generics.ListAPIView):
    serializer_class=serializers.BlogSerializer
    queryset = models.Blog.objects.filter()


class BlogDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=serializers.BlogDetailSerializer
    queryset = models.Blog.objects.all()



class CreateCategoryView(generics.CreateAPIView):
    serializer_class = serializers.categoryCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

   

class CategoryListView(generics.ListAPIView):
    serializer_class=serializers.CategorySerializer
    queryset = models.Category.objects.all()


class CategoryDetailsView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=serializers.CategoryDetailSerializer
queryset = models.Category.objects.all()


class UpdateCategoryView(generics.UpdateAPIView):
    queryset = models.Category.objects.all()
    serializer_class =serializers.categoryCreateSerializer
    permission_classes = [permissions.IsAuthenticated]
    # lookup_field = 'id'


class AuthorListView(generics.ListAPIView):
    serializer_class=serializers.AuthorSerializer
    queryset = models.Author.objects.all()


class AuthorDetailsView(generics.RetrieveDestroyAPIView):
    serializer_class=serializers.AuthorDetailSerializer
    queryset = models.Author.objects.all()    


class CommentViewset(viewsets.ModelViewSet):
     serializer_class=serializers.CommentSerializer
     queryset =models.Comment.objects.all()