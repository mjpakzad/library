from django.urls import path
from .views import BookList, BookDetail, ToggleBookmark, SubmitReview

urlpatterns = [
    path('', BookList.as_view(), name='book-list'),
    path('/<slug:slug>', BookDetail.as_view(), name='book-detail'),
    path('/<slug:slug>/bookmark', ToggleBookmark.as_view(), name='toggle-bookmark'),
    path('/<slug:slug>/review', SubmitReview.as_view(), name='submit-review'),
]
