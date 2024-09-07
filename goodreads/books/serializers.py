from django.db.models import Avg, Count
from rest_framework import serializers
from .models import Author, Book, Bookmark, Rating

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'biography']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    detail_link = serializers.HyperlinkedIdentityField(view_name='book-detail', lookup_field='slug')
    bookmarked_by_count = serializers.SerializerMethodField()
    is_bookmarked = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'content', 'slug', 'detail_link', 'bookmarked_by_count', 'is_bookmarked']

    def get_bookmarked_by_count(self, obj):
        return obj.bookmarked_by.count()

    def get_is_bookmarked(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return Bookmark.objects.filter(book=obj, user=user).exists()
        return False

class BookDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    comments = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()
    rating_distribution = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = ['id', 'name', 'author', 'content', 'comments', 'ratings', 'average_rating', 'rating_distribution']

    def get_comments(self, obj):
        return obj.comments.values('user__email', 'content')

    def get_ratings(self, obj):
        return obj.ratings.values('user__email', 'rating')

    def get_average_rating(self, obj):
        return obj.ratings.aggregate(Avg('rating'))['rating__avg']

    def get_rating_distribution(self, obj):
        distribution = obj.ratings.values('rating').annotate(count=Count('rating')).order_by('rating')
        return {entry['rating']: entry['count'] for entry in distribution}
