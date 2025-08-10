import re
import logging
from typing import List, Dict, Set

class NLPProcessor:
    """
    NLP processor for extracting skills and providing resume optimization suggestions.
    Uses pattern matching and keyword analysis instead of spaCy for simplicity.
    """
    
    def __init__(self):
        # Comprehensive tech skills database
        self.tech_skills = {
            # Programming Languages
            'python', 'javascript', 'java', 'c++', 'c#', 'php', 'ruby', 'go', 'rust', 'swift',
            'kotlin', 'typescript', 'scala', 'r', 'matlab', 'perl', 'lua', 'dart', 'elixir',
            
            # Web Technologies
            'html', 'css', 'react', 'angular', 'vue', 'nodejs', 'express', 'django', 'flask',
            'laravel', 'spring', 'asp.net', 'jquery', 'bootstrap', 'sass', 'less', 'webpack',
            'babel', 'npm', 'yarn', 'gulp', 'grunt',
            
            # Databases
            'mysql', 'postgresql', 'mongodb', 'redis', 'elasticsearch', 'sqlite', 'oracle',
            'sql server', 'cassandra', 'dynamodb', 'firebase', 'neo4j',
            
            # Cloud & DevOps
            'aws', 'azure', 'google cloud', 'gcp', 'docker', 'kubernetes', 'jenkins', 'terraform',
            'ansible', 'puppet', 'chef', 'vagrant', 'git', 'github', 'gitlab', 'bitbucket',
            'ci/cd', 'devops',
            
            # Data Science & AI
            'machine learning', 'deep learning', 'tensorflow', 'pytorch', 'scikit-learn',
            'pandas', 'numpy', 'matplotlib', 'seaborn', 'jupyter', 'apache spark', 'hadoop',
            'data analysis', 'data science', 'artificial intelligence', 'nlp', 'computer vision',
            
            # Mobile Development
            'android', 'ios', 'react native', 'flutter', 'xamarin', 'cordova', 'ionic',
            
            # Testing
            'unit testing', 'integration testing', 'jest', 'pytest', 'selenium', 'cypress',
            'mocha', 'jasmine', 'tdd', 'bdd',
            
            # Other Technologies
            'rest api', 'graphql', 'microservices', 'agile', 'scrum', 'kanban', 'jira',
            'confluence', 'slack', 'linux', 'unix', 'bash', 'powershell', 'vim', 'emacs'
        }
        
        # Soft skills database
        self.soft_skills = {
            'leadership', 'teamwork', 'communication', 'problem solving', 'critical thinking',
            'project management', 'time management', 'analytical thinking', 'creativity',
            'adaptability', 'collaboration', 'mentoring', 'presentation', 'negotiation'
        }
        
        logging.info("NLP Processor initialized successfully")
    
    def extract_skills(self, text: str) -> Dict[str, List[str]]:
        """
        Extract technical and soft skills from the given text.
        
        Args:
            text: Input text to analyze
            
        Returns:
            Dictionary containing extracted technical and soft skills
        """
        if not text:
            return {'technical': [], 'soft': []}
        
        # Convert to lowercase for matching
        text_lower = text.lower()
        
        # Extract technical skills
        technical_skills = []
        for skill in self.tech_skills:
            if re.search(r'\b' + re.escape(skill) + r'\b', text_lower):
                technical_skills.append(skill.title())
        
        # Extract soft skills
        soft_skills = []
        for skill in self.soft_skills:
            if re.search(r'\b' + re.escape(skill) + r'\b', text_lower):
                soft_skills.append(skill.title())
        
        # Remove duplicates and sort
        technical_skills = sorted(list(set(technical_skills)))
        soft_skills = sorted(list(set(soft_skills)))
        
        logging.info(f"Extracted {len(technical_skills)} technical skills and {len(soft_skills)} soft skills")
        
        return {
            'technical': technical_skills,
            'soft': soft_skills
        }
    
    def get_optimization_suggestions(self, job_titles: str, projects: str, 
                                   skills: str, education: str) -> List[str]:
        """
        Provide optimization suggestions for the resume.
        
        Args:
            job_titles: Job titles and experience text
            projects: Projects description text
            skills: Skills text
            education: Education text
            
        Returns:
            List of optimization suggestions
        """
        suggestions = []
        
        # Combine all text for analysis
        full_text = f"{job_titles} {projects} {skills} {education}".lower()
        
        # Check for quantifiable achievements
        if not re.search(r'\d+[%]?|\$\d+|increase|improve|reduce|optimize', full_text):
            suggestions.append("Add quantifiable achievements (e.g., 'Improved performance by 30%', 'Managed team of 5 developers')")
        
        # Check for action verbs
        action_verbs = ['developed', 'created', 'implemented', 'designed', 'built', 'managed', 
                       'led', 'optimized', 'improved', 'automated', 'deployed']
        if not any(verb in full_text for verb in action_verbs):
            suggestions.append("Use strong action verbs like 'developed', 'implemented', 'optimized', 'led'")
        
        # Check for modern technologies
        modern_tech = ['cloud', 'aws', 'azure', 'docker', 'kubernetes', 'react', 'vue', 'angular']
        if not any(tech in full_text for tech in modern_tech):
            suggestions.append("Consider highlighting experience with modern technologies like cloud platforms, containerization, or modern frameworks")
        
        # Check length and detail
        if len(job_titles.split()) < 50:
            suggestions.append("Expand your job experience section with more detailed descriptions of your responsibilities and achievements")
        
        if len(projects.split()) < 30:
            suggestions.append("Provide more detailed project descriptions including technologies used and outcomes achieved")
        
        # Check for specific skill categories
        extracted_skills = self.extract_skills(full_text)
        technical_count = len(extracted_skills['technical'])
        
        if technical_count < 5:
            suggestions.append("Consider adding more technical skills to strengthen your profile")
        
        if technical_count > 20:
            suggestions.append("Consider focusing on your strongest and most relevant technical skills")
        
        # Check for soft skills
        if len(extracted_skills['soft']) < 2:
            suggestions.append("Include soft skills like leadership, teamwork, or communication to create a well-rounded profile")
        
        # Default suggestion if no issues found
        if not suggestions:
            suggestions.append("Your resume looks comprehensive! Consider tailoring it for specific job applications by emphasizing relevant skills and experiences.")
        
        logging.info(f"Generated {len(suggestions)} optimization suggestions")
        return suggestions
    
    def analyze_keyword_density(self, text: str) -> Dict[str, int]:
        """
        Analyze keyword density in the text.
        
        Args:
            text: Text to analyze
            
        Returns:
            Dictionary of keywords and their frequencies
        """
        if not text:
            return {}
        
        # Simple keyword frequency analysis
        words = re.findall(r'\b\w+\b', text.lower())
        keyword_count = {}
        
        for word in words:
            if word in self.tech_skills or word in self.soft_skills:
                keyword_count[word] = keyword_count.get(word, 0) + 1
        
        return keyword_count
