from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class ResumeForm(FlaskForm):
    job_titles = TextAreaField(
        'Job Titles & Experience',
        validators=[
            DataRequired(message='Please provide your job titles and experience.'),
            Length(min=10, max=2000, message='Please provide between 10 and 2000 characters.')
        ],
        render_kw={
            'placeholder': 'e.g., Software Engineer at TechCorp (2020-2023)\nDeveloped web applications using Python and React...',
            'rows': 5,
            'class': 'form-control'
        }
    )
    
    projects = TextAreaField(
        'Projects',
        validators=[
            DataRequired(message='Please describe your projects.'),
            Length(min=10, max=2000, message='Please provide between 10 and 2000 characters.')
        ],
        render_kw={
            'placeholder': 'e.g., E-commerce Platform\nBuilt a full-stack e-commerce application using Django, PostgreSQL, and React...',
            'rows': 5,
            'class': 'form-control'
        }
    )
    
    skills = TextAreaField(
        'Skills',
        validators=[
            DataRequired(message='Please list your skills.'),
            Length(min=5, max=1000, message='Please provide between 5 and 1000 characters.')
        ],
        render_kw={
            'placeholder': 'e.g., Python, JavaScript, React, Django, PostgreSQL, AWS, Docker...',
            'rows': 3,
            'class': 'form-control'
        }
    )
    
    education = TextAreaField(
        'Education',
        validators=[
            DataRequired(message='Please provide your educational background.'),
            Length(min=10, max=1000, message='Please provide between 10 and 1000 characters.')
        ],
        render_kw={
            'placeholder': 'e.g., Bachelor of Science in Computer Science\nUniversity of Technology (2016-2020)\nRelevant Coursework: Data Structures, Algorithms, Software Engineering...',
            'rows': 4,
            'class': 'form-control'
        }
    )
    
    submit = SubmitField('Generate Resume', render_kw={'class': 'btn btn-primary btn-lg'})
