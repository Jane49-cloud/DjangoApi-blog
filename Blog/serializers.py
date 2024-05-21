from rest_framework import serializers
from . import models


# Author serializers
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Author
        fields=[ 'user', 'id']

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

#Blog Serializers

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Blog
        fields=[ 'title', 'id', 'author', 'created_at', 'category' ,'description' , "published"]

    # this manipulates or allows related
    def __init__(self, *args, **kwargs):
        super(BlogSerializer, self).__init__(*args, **kwargs)
        # request =self.context.get('request')
        self.Meta.depth =1 # depth means it will go  one level in the relative model


class BlogDetailSerializer(serializers.ModelSerializer):
    comments =CommentSerializer(many=True,read_only=True)
    class Meta:
        model=models.Blog
        fields=[ 'title', 'id', 'author', 'created_at', 'category' ,'description', 'comments' , "published"]

    def __init__(self, *args, **kwargs):
        super(BlogDetailSerializer, self).__init__(*args, **kwargs)
        # request =self.context.get('request')
        self.Meta.depth =1



#Category Serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Category
        fields='__all__'

    # this manipulates or allows related
    def __init__(self, *args, **kwargs):
        super(CategorySerializer, self).__init__(*args, **kwargs)
        # request =self.context.get('request')
        self.Meta.depth =1 # depth means it will go  one level in the relative model


class CategoryDetailSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=models.Category
        fields='__all__'

    def __init__(self, *args, **kwargs):
        super(CategoryDetailSerializer, self).__init__(*args, **kwargs)
        # request =self.context.get('request')
        self.Meta.depth =1


