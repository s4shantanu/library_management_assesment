# Library Management System

This project is a backend implementation of a Library Management System using **Python**, **Django Rest Framework (DRF)**, and **PostgreSQL**. It provides APIs for librarians (admins) and library users to manage books, users, and borrow requests.

---

## Features

### Librarian (Admin) APIs:
- **Create Library Users:** Add a new user with email and password.
- **Manage Borrow Requests:** Approve or deny book borrowing requests.
- **View Borrow Requests:** See all borrow requests submitted by users.
- **User Borrow History:** View borrowing history of a specific user.

### Library User APIs:
- **View Books:** List all books available in the library.
- **Borrow Books:** Request to borrow a book for specific dates.
- **Borrow History:** View personal borrowing history.
- **Download History:** Export borrowing history as a CSV file.

### Authentication:
- **JWT-based Authentication:** Secure the APIs using JSON Web Tokens.

---

## Installation

### Prerequisites:
- Python 3.8 or higher
- PostgreSQL 12 or higher
- Pip (Python package manager)

### Steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system
