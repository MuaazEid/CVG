import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash
from forms import ResumeForm
from nlp_processor import NLPProcessor

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "fallback-secret-key-for-development")

# Initialize NLP processor
nlp_processor = NLPProcessor()

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ResumeForm()
    
    if form.validate_on_submit():
        try:
            # Process form data
            job_titles = form.job_titles.data
            projects = form.projects.data
            skills = form.skills.data
            education = form.education.data
            
            # Extract skills using NLP
            extracted_skills = nlp_processor.extract_skills(
                job_titles + " " + projects + " " + skills
            )
            
            # Get optimization suggestions
            suggestions = nlp_processor.get_optimization_suggestions(
                job_titles, projects, skills, education
            )
            
            # Prepare data for resume generation
            resume_data = {
                'job_titles': job_titles,
                'projects': projects,
                'skills': skills,
                'education': education,
                'extracted_skills': extracted_skills,
                'suggestions': suggestions
            }
            
            return render_template('resume.html', data=resume_data)
            
        except Exception as e:
            logging.error(f"Error processing resume data: {str(e)}")
            flash('An error occurred while processing your resume. Please try again.', 'error')
            return redirect(url_for('index'))
    
    return render_template('index.html', form=form)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('index.html', form=ResumeForm()), 404

@app.errorhandler(500)
def internal_server_error(e):
    logging.error(f"Internal server error: {str(e)}")
    flash('An internal error occurred. Please try again later.', 'error')
    return render_template('index.html', form=ResumeForm()), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
