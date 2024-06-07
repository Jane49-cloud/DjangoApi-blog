from rest_framework import serializers
from . import models
from Accounts.serializers import UserSerializer

# Author serializers
class AuthorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = models.Author
        fields = ['user', 'id']

class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = ['user', 'id']

# Comment serializers
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'

class CommentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = '__all__'

# Category serializers
class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ['name', 'description', 'id']

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='pk')

    class Meta:
        model = models.Category
        fields = ['id', 'name', 'description']

# Blog serializers
class BlogCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Blog
        fields = ['title', 'id', 'author', 'created_at', 'category', 'description', 'published', 'image', 'content']


class BlogSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='pk')
    category = serializers.PrimaryKeyRelatedField(queryset=models.Category.objects.all())
    author = AuthorSerializer()
    category = CategorySerializer()

    class Meta:
        model = models.Blog
        fields = ['title', 'id', 'author', 'created_at', 'category', 'description', 'published', 'image']



        

class BlogDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    id = serializers.CharField()
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = models.Blog
        fields = ['title', 'id', 'author', 'created_at', 'category', 'description', 'comments', 'published', 'content', 'image']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        request = self.context.get('request')
        if request:
            ret['image'] = request.build_absolute_uri(instance.image.url)
        return ret

class CategoryDetailSerializer(serializers.ModelSerializer):
    category_blogs = BlogSerializer(many=True, read_only=True)
    id = serializers.CharField(source='pk')

    class Meta:
        model = models.Category
        fields = ['id', 'name', 'description', 'category_blogs']