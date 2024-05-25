from rest_framework import serializers
from . import models
from Accounts.serializers import UserSerializer


# Author serializers
class AuthorSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=models.Author
        fields=[ 'user', 'id']
        depth=1

    # this manipulates or allows related
    def __init__(self, *args, **kwargs):
        super(AuthorSerializer, self).__init__(*args, **kwargs)
        # request =self.context.get('request')
        self.Meta.depth =1 # depth means it will go  one level in the relative model


class AuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Author
        fields=['user', 'id']

    def __init__(self, *args, **kwargs):
        super(AuthorDetailSerializer, self).__init__(*args, **kwargs)
        # request =self.context.get('request')
        self.Meta.depth =1




#comment Serializers

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Comment
        fields='__all__'

    # this manipulates or allows related
    def __init__(self, *args, **kwargs):
        super(CommentSerializer, self).__init__(*args, **kwargs)
        # request =self.context.get('request')
        self.Meta.depth =1 # depth means it will go  one level in the relative model


class CommentDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=models.Comment
        fields="__all__"

    def __init__(self, *args, **kwargs):
        super(CommentDetailSerializer, self).__init__(*args, **kwargs)
        # request =self.context.get('request')
        self.Meta.depth =1




#Category Serializers

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='pk') 
    class Meta:
        model=models.Category
        fields=["id", 'name', 'description']

    # this manipulates or allows related
    def __init__(self, *args, **kwargs):
        super(CategorySerializer, self).__init__(*args, **kwargs)
        # request =self.context.get('request')
        self.Meta.depth =1 # depth means it will go  one level in the relative model


class CategoryDetailSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='pk') 
   
    class Meta:
        model=models.Category
        fields=["id", 'name', 'description']

    def __init__(self, *args, **kwargs):
        super(CategoryDetailSerializer, self).__init__(*args, **kwargs)
        # request =self.context.get('request')
        self.Meta.depth =1

#Blog Serializers

class BlogCreateSerializer(serializers.ModelSerializer): 
    # id = serializers.CharField(source='pk') 
    class Meta:
        model=models.Blog
        fields=[ 'title', 'id', 'author', 'created_at', 'category' ,'description' , "published" , "image"]


class BlogSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='pk') 
    category = serializers.PrimaryKeyRelatedField(queryset=models.Category.objects.all())
   
  
    author = AuthorSerializer()
    category=CategorySerializer()
    class Meta:
        model=models.Blog
        fields=[ 'title', 'id', 'author', 'created_at', 'category' ,'description' , "published" , "image"]


        

    # this manipulates or allows related
    def __init__(self, *args, **kwargs):
        super(BlogSerializer, self).__init__(*args, **kwargs)
        # request =self.context.get('request')
        self.Meta.depth =1 # depth means it will go  one level in the relative model


    def create(self, validated_data):
        category = validated_data.pop('category')
        blog = models.Blog.objects.create(category=category, **validated_data)
        return blog


class BlogDetailSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    id = serializers.CharField()

    class Meta:
        model = models.Blog
        fields = ['title', 'id', 'author', 'created_at', 'category', 'description', 'comments', 'published', 'content']
        depth = 1

    def __init__(self, *args, **kwargs):
        super(BlogDetailSerializer, self).__init__(*args, **kwargs)
        # request =self.context.get('request')
        self.Meta.depth =1






