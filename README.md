# Django Portfolio Website

A modern, responsive portfolio website built with Django that showcases your skills, projects, achievements, and more.

## Features

### 📄 Pages
- **Home Page**: Hero section with introduction and featured content
- **About Page**: Personal information, career objective, and contact details
- **Skills Page**: Categorized technical skills with proficiency levels
- **Education Page**: Academic background and qualifications
- **Projects Page**: Portfolio of work with filtering and search
- **Achievements Page**: Awards, recognitions, and milestones
- **Certifications Page**: Professional certifications and qualifications
- **Hobbies Page**: Personal interests and activities
- **Contact Page**: Contact form and information

### 🔍 Functionality
- **Responsive Design**: Works perfectly on all devices
- **Modern UI**: Clean, professional design with Bootstrap 5
- **Admin Panel**: Easy content management through Django admin
- **Contact Form**: Functional contact form with email validation
- **Search & Filter**: Advanced filtering for projects and achievements
- **Pagination**: Efficient content organization
- **Image Upload**: Support for profile pictures and project images
- **Social Links**: Integration with GitHub, LinkedIn, and more

### 📦 Bonus Features
- **Dark Mode Toggle**: Optional dark theme (JavaScript)
- **Smooth Animations**: CSS animations and transitions
- **SEO Optimized**: Meta tags and structured content
- **Performance Optimized**: Efficient database queries
- **Security**: CSRF protection and form validation

## Technology Stack

- **Backend**: Django 5.2.3
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Database**: SQLite (can be easily changed to PostgreSQL/MySQL)
- **Icons**: FontAwesome 6
- **Fonts**: Google Fonts (Poppins)

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd portfolio
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser
```bash
python manage.py createsuperuser
```

### Step 6: Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see your portfolio website!

## Admin Panel Setup

1. Go to `http://127.0.0.1:8000/admin/`
2. Login with your superuser credentials
3. Add your content through the admin interface:

### Required Content (in order):
1. **Profile**: Add your personal information
2. **Skill Categories**: Create categories like "Frontend", "Backend", etc.
3. **Skills**: Add skills under each category
4. **Education**: Add your educational background
5. **Projects**: Add your portfolio projects
6. **Achievements**: Add awards and recognitions
7. **Certifications**: Add professional certifications
8. **Hobbies**: Add your interests (optional)

## Customization

### Styling
- Edit `static/css/style.css` to customize colors, fonts, and layout
- Modify `templates/base.html` for global changes
- Update individual template files for page-specific changes

### Content
- All content is managed through the Django admin panel
- No coding required to update your portfolio
- Images are automatically optimized and stored

### Deployment
The website is ready for deployment on platforms like:
- Heroku
- Vercel
- DigitalOcean
- AWS
- Any VPS with Python support

## File Structure

```
portfolio/
├── main/                    # Main Django app
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── forms.py            # Contact form
│   ├── admin.py            # Admin configuration
│   └── urls.py             # URL patterns
├── templates/              # HTML templates
│   ├── base.html           # Base template
│   └── main/               # App-specific templates
├── static/                 # Static files
│   ├── css/                # Stylesheets
│   ├── js/                 # JavaScript files
│   └── images/             # Images
├── media/                  # User-uploaded files
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).

## Support

If you encounter any issues or have questions:
1. Check the documentation
2. Search existing issues
3. Create a new issue with detailed information

## Acknowledgments

- Django team for the amazing framework
- Bootstrap team for the responsive CSS framework
- FontAwesome for the beautiful icons
- All contributors and users of this project

---

**Happy Coding! 🚀** 