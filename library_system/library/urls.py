from django.urls import path
from .views import RegisterUserView, BookListView, BorrowRequestView, ApproveBorrowRequestView, DownloadBorrowHistoryView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('books/', BookListView.as_view(), name='book-list'),
    path('borrow-requests/', BorrowRequestView.as_view(), name='borrow-requests'),
    path('approve-request/<int:request_id>/', ApproveBorrowRequestView.as_view(), name='approve-request'),
    path('download-history/', DownloadBorrowHistoryView.as_view(), name='download-history'),
]
