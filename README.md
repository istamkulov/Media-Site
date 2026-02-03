Media Site (Django + DRF + HTML/CSS)

Media Site is a backend project built with Django and Django REST Framework, designed to store and serve data about movies and TV shows, including seasons, episodes, ratings, and streaming/download sources. The project is structured as an API-first backend, while also using HTML/CSS for the admin interface and potential frontend templates.

🚀 Project Features

📽 Storage of Movies and TV Shows

📺 Support for Seasons and Episodes with proper ordering

⭐ IMDb and Kinopoisk Ratings

🔗 Streaming Sources (playlists, direct links)

🧩 REST API with Django REST Framework

🖥 Django Admin with custom HTML/CSS interface for easy data management

📦 Ready for Extension: Celery, FastAPI, Docker

🎨 Option to integrate a custom HTML/CSS frontend

🧱 Technology Stack

Python 3.10+

Django

Django REST Framework

PostgreSQL / SQLite

Requests (for data import)

Swagger / DRF Browsable API

HTML/CSS (for admin and potential frontend)

📁 Project Structure

Media-Site/
│
├── mediasite/           # Main Django configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── mediaapp/            # Main application
│   ├── models.py        # Database models
│   ├── serializers.py   # DRF serializers
│   ├── views.py         # API Views / ViewSets
│   ├── urls.py          # API routes
│   ├── admin.py         # Django Admin + custom HTML/CSS templates
│   └── services.py      # Data import services
│
├── manage.py
├── requirements.txt
└── README.md


🗃 Data Models

Movie

title

description

release_date

imdb_rating

kinopoisk_rating

image

sources

Show (TV Series)

title

description

release_date

imdb_rating

kinopoisk_rating

image

seasons

Season

number

show

Episode

number

title

season

sources

Source

url

is_active

movie / episode

🔗 API Endpoints

Movies

GET /api/movies/

GET /api/movies/{id}/

GET /api/movies/{id}/sources/

TV Shows

GET /api/shows/

GET /api/shows/{id}/

GET /api/shows/{id}/seasons/

GET /api/seasons/{id}/episodes/

GET /api/episodes/{id}/sources/

All endpoints are available through the DRF Browsable API and can be extended with custom HTML/CSS templates.

🧪 Example API Response

{
  "id": 1,
  "title": "Breaking Bad",
  "imdb_rating": 9.5,
  "kinopoisk_rating": 9.0,
  "seasons": [
    {
      "number": 1,
      "episodes": [
        {
          "number": 1,
          "title": "Pilot",
          "sources": [
            {
              "url": "https://example.com/video.m3u8",
              "is_active": true
            }
          ]
        }
      ]
    }
  ]
}


📥 Data Import

Supports importing data from external sources:

Movies
https://channelsapi.s3.amazonaws.com/media/test/movies.json

Shows
https://channelsapi.s3.amazonaws.com/media/test/shows.json

The import is implemented in mediaapp/services.py and can be:

run manually

connected to Celery

scheduled with cron

⚙️ Installation and Run

git clone https://github.com/istamkulov/Media-Site.git
cd Media-Site
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


🔐 Admin Interface
http://127.0.0.1:8000/admin/

Allows:

adding movies and shows

managing seasons and episodes

enabling/disabling sources

using a custom HTML/CSS interface for convenience

🧩 Planned Extensions

✅ FastAPI microservice for high-load API
✅ Celery + Redis for background tasks
⏳ Source validation
⏳ Docker / Docker Compose
⏳ JWT authentication
🎨 Integration of custom frontend with HTML/CSS
