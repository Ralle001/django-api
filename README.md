# Simple Quote API

A RESTful API to manage a collection of quotes built with Django and Django REST Framework.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## Setup Instructions

1. **Clone the Repository**
```
git clone <repository-url>
cd <repository-directory>
```

2. **Create and Activate Virtual Environment**
```
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

3. **Install Dependencies**
```
pip install -r requirements.txt
```

4. **Run Database Migrations**
```
python manage.py migrate
```

5. **Start Development Server**
```
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/api/`

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET    | `/api/quotes/` | List all quotes |
| POST   | `/api/quotes/` | Create new quote |
| GET    | `/api/quotes/<id>/` | Get specific quote |
| PUT    | `/api/quotes/<id>/` | Update quote |
| DELETE | `/api/quotes/<id>/` | Delete quote |
| GET    | `/api/quotes/random/` | Get random quote |

## Running Tests

Execute the test suite using:
```
python manage.py test
```

## Example API Usage

### Create Quote
```
curl -X POST http://127.0.0.1:8000/api/quotes/ \
-H "Content-Type: application/json" \
-d '{"text": "Life is what happens while you are busy making other plans", "author": "John Lennon"}'
```

### Get Random Quote
```
curl -X GET http://127.0.0.1:8000/api/quotes/random/
```

## Project Structure
```
quote_api/
├── quotes/              # Main app directory
├── quote_api/          # Project configuration
├── manage.py           # Django management script
├── requirements.txt    # Project dependencies
└── README.md          # This file
```

## Dependencies
- Django
- Django REST Framework

All dependencies are listed in `requirements.txt`