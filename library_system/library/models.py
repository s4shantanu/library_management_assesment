from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now

class User(AbstractUser):
    is_librarian = models.BooleanField(default=False)

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    is_available = models.BooleanField(default=True)

class BorrowRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrow_requests')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrow_requests')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, choices=(('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')), default='Pending')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['book', 'start_date', 'end_date'],
                name='unique_borrow_request'
            )
        ]
