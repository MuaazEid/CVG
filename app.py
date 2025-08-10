import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash
from forms import ResumeForm
from nlp_processor import NLPProcessor
import re

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "fallback-secret-key-for-development")

# Initialize NLP processor
nlp_processor = NLPProcessor()

# Custom template filter for newline to <br> conversion
@app.template_filter('nl2br')
def nl2br_filter(text):
    """Convert newlines to HTML line breaks"""
    if text is None:
        return ''
    # Replace newlines with <br> tags
    return re.sub(r'\n', '<br>', str(text))

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ResumeForm()
    
    if request.method == 'POST':
        logging.debug(f"Form data received: {request.form}")
        logging.debug(f"Form errors: {form.errors}")
        logging.debug(f"Form validation result: {form.validate_on_submit()}")
    
    if form.validate_on_submit():
        try:
            logging.info("Form validation successful, processing resume data...")
            
            # Process form data
            job_titles = form.job_titles.data
            projects = form.projects.data
            skills = form.skills.data
            education = form.education.data
            
            logging.debug(f"Processing data - Job titles: {len(job_titles)} chars, Projects: {len(projects)} chars, Skills: {len(skills)} chars, Education: {len(education)} chars")
            
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
            
            logging.info(f"Resume generated successfully with {len(extracted_skills['technical'])} technical skills and {len(extracted_skills['soft'])} soft skills")
            return render_template('resume.html', data=resume_data)
            
        except Exception as e:
            logging.error(f"Error processing resume data: {str(e)}")
            flash('An error occurred while processing your resume. Please try again.', 'error')
            return redirect(url_for('index'))
    elif request.method == 'POST':
        # Form validation failed
        logging.warning(f"Form validation failed with errors: {form.errors}")
        for field_name, errors in form.errors.items():
            for error in errors:
                flash(f"{field_name}: {error}", 'error')
    
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
