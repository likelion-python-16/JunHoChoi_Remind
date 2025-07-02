from rest_framework import serializers
from .models import Todo
from interaction.models import Like, Bookmark, Comment
from django.forms.models import model_to_dict


class TodoSerializer(serializers.ModelSerializer):
    is_liked = serializers.SerializerMethodField()
    is_marked = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    bookmark_count = serializers.SerializerMethodField()
    is_bookmarked = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = [*model_to_dict(Todo()).keys(), "is_liked", "is_marked", "like_count", "comments_count" , "is_bookmarked", "bookmark_count"]

    def get_is_liked(self, obj):
        
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return Like.objects.filter(user=request.user, todo=obj, is_like=True).exists()
        return False

    def get_is_marked(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return Bookmark.objects.filter(user=request.user, todo=obj, is_marked=True).exists()
        return False

    def get_like_count(self, obj):
        return Like.objects.filter(todo=obj, is_like=True).count()

    def get_comments_count(self, obj):
        return Comment.objects.filter(todo=obj).count()
    
    def get_bookmark_count(self, obj):
        return Bookmark.objects.filter(todo=obj, is_marked=True).count()

    def get_is_bookmarked(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return Bookmark.objects.filter(user=request.user, todo=obj, is_marked=True).exists()
        return False