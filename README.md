# Django Portfolio Project

A full-featured Django portfolio application with CRUD operations for Projects, Hobbies, and Profiles.

## Features

- **Projects Management**: Create, read, update, and delete projects with search, filter, and pagination
- **Hobbies Management**: Manage your hobbies with full CRUD operations
- **Profile Management**: Create and manage your portfolio profiles
- **Search & Filter**: Advanced search and filtering capabilities
- **Pagination**: Efficient pagination for large datasets
- **Modern UI**: Beautiful, responsive design with Tailwind CSS

## Tech Stack

- Django 5.2.8
- Python 3.x
- SQLite (development)
- Tailwind CSS

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Sofia-Asad/portfolio.git
cd portfolio
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create a superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Deployment to Render

Render is an excellent platform for deploying Django applications. Follow these steps:

### Step 1: Create a Render Account
1. Go to [render.com](https://render.com) and sign up/login
2. Connect your GitHub account

### Step 2: Create a New Web Service
1. Click "New +" → "Web Service"
2. Connect your GitHub repository: `Sofia-Asad/portfolio`
3. Configure the service:
   - **Name**: `portfolio-django` (or your preferred name)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
   - **Start Command**: `gunicorn portfolio_project.wsgi:application`

### Step 3: Set Environment Variables
In the Render dashboard, go to "Environment" and add:
- `SECRET_KEY`: Generate a new secret key (you can use: `python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"`)
- `DEBUG`: `False`
- `ALLOWED_HOSTS`: `your-app-name.onrender.com` (Render will provide this)

### Step 4: (Optional) Add PostgreSQL Database
1. In Render dashboard, click "New +" → "PostgreSQL"
2. Create a free PostgreSQL database
3. Copy the "Internal Database URL"
4. Add environment variable: `DATABASE_URL` with the copied URL
5. The app will automatically use PostgreSQL instead of SQLite

### Step 5: Deploy
1. Click "Create Web Service"
2. Render will automatically build and deploy your application
3. Your app will be available at `https://your-app-name.onrender.com`

### Using render.yaml (Alternative Method)
If you prefer using the `render.yaml` file:
1. The `render.yaml` file is already configured in the repository
2. In Render dashboard, select "Apply render.yaml" when creating the service
3. Render will automatically read the configuration

### Post-Deployment
1. Create a superuser:
   - Go to your Render service → "Shell"
   - Run: `python manage.py createsuperuser`
2. Access your admin panel at: `https://your-app-name.onrender.com/admin/`

## Deployment to Other Platforms

### Railway
- Excellent Django support
- Free tier available
- Easy PostgreSQL setup

### PythonAnywhere
- Beginner-friendly
- Free tier available
- Good for learning

### Heroku
- Popular platform
- Requires credit card for free tier
- Good documentation

## Project Structure

```
portfolio/
├── core/                 # Main application
│   ├── models.py        # Database models
│   ├── views.py         # View functions
│   ├── forms.py         # Form classes
│   └── urls.py          # URL routing
├── templates/           # HTML templates
│   ├── projects/        # Project templates
│   ├── hobbies/         # Hobby templates
│   └── profiles/        # Profile templates
├── portfolio_project/  # Django project settings
└── manage.py           # Django management script
```

## Usage

- Access admin panel: `/admin/`
- View projects: `/projects/`
- View hobbies: `/hobbies/`
- View profiles: `/profiles/`

## License

This project is open source and available under the MIT License.

