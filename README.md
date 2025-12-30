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

## Deployment to Vercel

**Important Note**: Vercel is not ideal for Django applications, especially with SQLite databases. Consider using:
- **Railway** (Recommended for Django)
- **Render**
- **PythonAnywhere**
- **Heroku**

If you still want to deploy to Vercel:

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Login to Vercel:
```bash
vercel login
```

3. Deploy:
```bash
vercel
```

4. Set environment variables in Vercel dashboard:
   - `DJANGO_SECRET_KEY`: Your Django secret key
   - `DEBUG`: Set to `False` for production

5. Run migrations on Vercel:
```bash
vercel env pull .env.local
python manage.py migrate
```

**Limitations on Vercel**:
- SQLite database won't persist (data will be lost on each deployment)
- Consider using PostgreSQL or another database service
- Static files need proper configuration
- Some Django features may not work in serverless environment

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

