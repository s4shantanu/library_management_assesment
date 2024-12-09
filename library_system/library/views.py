from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Book, BorrowRequest
from .serializers import UserSerializer, BookSerializer, BorrowRequestSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.http import HttpResponse
import csv

class RegisterUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [JWTAuthentication]

class BorrowRequestView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        if request.user.is_librarian:
            requests = BorrowRequest.objects.all()
        else:
            requests = BorrowRequest.objects.filter(user=request.user)
        serializer = BorrowRequestSerializer(requests, many=True)
        return Response(serializer.data)

    def post(self, request):
        book = Book.objects.get(id=request.data['book_id'])
        if not book.is_available:
            return Response({"error": "Book is not available"}, status=status.HTTP_400_BAD_REQUEST)
        request.data['user'] = request.user.id
        serializer = BorrowRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ApproveBorrowRequestView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def post(self, request, request_id):
        borrow_request = BorrowRequest.objects.get(id=request_id)
        borrow_request.status = 'Approved'
        borrow_request.save()
        return Response({"message": "Request approved."}, status=status.HTTP_200_OK)

class DownloadBorrowHistoryView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        borrow_requests = BorrowRequest.objects.filter(user=request.user)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="borrow_history.csv"'

        writer = csv.writer(response)
        writer.writerow(['Book Title', 'Start Date', 'End Date', 'Status'])
        for request in borrow_requests:
            writer.writerow([request.book.title, request.start_date, request.end_date, request.status])

        return response
