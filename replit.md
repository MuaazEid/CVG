# Overview

This is a Flask-based AI-powered resume generator that uses Natural Language Processing to extract skills from user input and create optimized professional resumes. The application takes user information about job experience, projects, skills, and education, then processes this data to identify technical and soft skills while providing optimization suggestions for better resume formatting.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Template Engine**: Jinja2 templating with Flask for server-side rendering
- **CSS Framework**: Bootstrap 5.3.0 for responsive design and UI components
- **Icons**: Font Awesome 6.4.0 for consistent iconography
- **Typography**: Google Fonts (Inter) for modern, readable text
- **JavaScript**: Vanilla JavaScript for form validation, character counters, and interactive features
- **Styling**: Custom CSS with CSS variables for consistent theming and gradient backgrounds

## Backend Architecture
- **Web Framework**: Flask as the lightweight Python web framework
- **Form Handling**: Flask-WTF with WTForms for secure form processing and validation
- **NLP Processing**: Custom NLPProcessor class using pattern matching and keyword analysis instead of heavy ML libraries
- **Session Management**: Flask's built-in session handling with configurable secret key
- **Error Handling**: Flash message system for user feedback and form validation errors

## Data Processing
- **Skill Extraction**: Pattern-based NLP processor that identifies technical skills from unstructured text
- **Skill Categories**: Comprehensive databases for technical skills (programming languages, frameworks, databases, cloud services) and soft skills
- **Text Processing**: Regular expressions and string manipulation for extracting relevant information
- **Resume Generation**: Server-side processing that combines user input with extracted skills to generate formatted resume content

## Security Features
- **CSRF Protection**: Flask-WTF provides CSRF tokens for form security
- **Input Validation**: Server-side validation with length limits and required field checks
- **Environment Variables**: Configuration through environment variables for sensitive data
- **XSS Prevention**: Jinja2 template auto-escaping with selective safe rendering for formatted content

# External Dependencies

## Python Packages
- **Flask**: Core web framework for handling HTTP requests and responses
- **Flask-WTF**: Form handling and CSRF protection
- **WTForms**: Form validation and rendering

## Frontend Libraries
- **Bootstrap 5.3.0**: CSS framework loaded via CDN for responsive design
- **Font Awesome 6.4.0**: Icon library loaded via CDN
- **Google Fonts**: Inter font family for typography

## Development Tools
- **Python Logging**: Built-in logging module for debugging and monitoring
- **Environment Configuration**: Uses os.environ for configuration management

## Infrastructure
- **Host Configuration**: Designed to run on 0.0.0.0:5000 for container compatibility
- **Static File Serving**: Flask's built-in static file handling for CSS and JavaScript
- **Template Rendering**: Jinja2 template inheritance system for maintainable UI components