from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from .models import Book, Bookmark, Rating, Comment
from .serializers import BookSerializer, BookDetailSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    lookup_field = 'slug'

class ToggleBookmark(APIView):
    def post(self, request, slug):
        book = get_object_or_404(Book, slug=slug)
        user = request.user

        bookmark, created = Bookmark.objects.get_or_create(user=user, book=book)
        if not created:
            bookmark.delete()
            return Response({"message": "Book unbookmarked"}, status=status.HTTP_200_OK)
        return Response({"message": "Book bookmarked"}, status=status.HTTP_200_OK)

class SubmitReview(APIView):
    def post(self, request, slug):
        book = get_object_or_404(Book, slug=slug)
        user = request.user

        rating = request.data.get('rating')
        comment_content = request.data.get('content')

        if rating is not None:
            if not (1 <= int(rating) <= 5):
                return Response({"error": "Rating must be between 1 and 5"}, status=status.HTTP_400_BAD_REQUEST)

        if rating is None and not comment_content:
            return Response({"error": "Either rating or comment content must be provided"}, status=status.HTTP_400_BAD_REQUEST)

        if rating:
            Rating.objects.update_or_create(user=user, book=book, defaults={'rating': rating})

        if comment_content:
            Comment.objects.update_or_create(user=user, book=book, defaults={'content': comment_content})

        return Response({"message": "Comment and/or rating submitted/updated"}, status=status.HTTP_200_OK)
