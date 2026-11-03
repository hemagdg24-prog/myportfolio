from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'hemaaswini_portfolio_secret_key_2024'

# ─── Portfolio Data ───────────────────────────────────────────────────────────
PORTFOLIO_DATA = {
    "personal": {
        "name": "Hemaaswini Pericharla",
        "title": "Computer Science & Design (CSD) Engineer · Full-Stack & Flutter Developer",
        "tagline": "Passionate about Flutter, Python, Flask & Building Intuitive Applications",
        "email": "hemaaswini@example.com",
        "phone": "+91 8142333445",
        "location": "India",
        "github": "https://github.com/hemagdg24-prog",
        "linkedin": "https://www.linkedin.com/in/hemaaswini-pericharla-688708350",
        "avatar": "/static/images/avatar_square.jpg",
        "resume": "/static/images/hemaresume.pdf",
        "about": (
            "I am a Computer Science & Design (CSD) undergraduate (Class of 2027) with hands-on experience as a "
            "Flutter Developer at 90 Heal and a strong passion for full-stack web and mobile development. "
            "I specialize in building cross-platform mobile apps with Flutter & Dart, coupled with robust "
            "backends using Python & Flask to deliver scalable, user-centric software."
        ),
    },
    "education": [
        {
            "degree": "B.Tech – Computer Science and Design (CSD)",
            "institution": "Raghu Venkaiah Rajiv Engineering College of Engineering (R), Bhimavaram",
            "period": "2023 – 2027",
            "grade": "Class of 2027 · Currently Pursuing",
            "icon": "🎓",
        },
        {
            "degree": "Intermediate (MPC)",
            "institution": "Sri Chaitanya Junior College, Ongole",
            "period": "2021 – 2023",
            "grade": "87%",
            "icon": "📚",
        },
    ],
    "skills": {
        "Languages": ["Python", "Dart", "Java", "C", "HTML", "CSS", "JavaScript", "SQL"],
        "Frameworks": ["Flutter", "Flask", "Django", "Bootstrap"],
        "Tools": ["Git", "GitHub", "VS Code", "Android Studio", "MySQL", "PostgreSQL"],
        "AI / ML": ["Machine Learning", "NLP", "LLM APIs", "OpenAI API"],
        "Platforms": ["Android", "iOS", "Vercel", "Render", "Linux", "Windows"],
    },
    "experience": [
        {
            "role": "Flutter Developer",
            "company": "90 Heal",
            "period": "2025",
            "description": (
                "Developed cross-platform mobile applications using Flutter and Dart. "
                "Architected reusable responsive UI widgets, integrated RESTful APIs, managed application state, and "
                "collaborated on digital healthcare features to streamline user accessibility and performance."
            ),
            "tech": ["Flutter", "Dart", "REST API", "Mobile App Dev", "State Management", "UI/UX"],
            "icon": "📱",
        },
        {
            "role": "Software Developer Intern",
            "company": "Vitreel",
            "period": "Oct 2024 – Mar 2025",
            "description": (
                "Developed web applications using Flask and integrated API solutions. "
                "Implemented advanced backend features, conducted unit tests, and collaborated on data-driven platforms."
            ),
            "tech": ["Python", "Flask", "REST API", "Bootstrap", "MySQL"],
            "icon": "💼",
        }
    ],
    "projects": [
        {
            "name": "Sri Roofings — Industrial & Roofing Solutions",
            "date": "2026",
            "tech": ["HTML5", "CSS3", "JavaScript", "Responsive Design", "SEO"],
            "description": (
                "Official modern commercial web platform built for Sri Roofings, showcasing industrial "
                "and residential roofing solutions, product catalogs, customer inquiry management, and "
                "mobile-first responsive architecture."
            ),
            "github": "https://github.com/hemagdg24-prog",
            "live": "https://sriroof.in/",
            "icon": "🏗️",
        },
        {
            "name": "PM AJAY — Smart Scheme Portal",
            "date": "2025 – 2026",
            "tech": ["Python", "Django", "PostgreSQL", "Bootstrap"],
            "description": (
                "Full-stack digital portal built for Pradhan Mantri Anusuchit Jaati Abhyuday Yojana "
                "(PM-AJAY) facilitating smart role-based benefit allocation, healthcare scheme "
                "administration, and data-driven reporting. Won AI Summit at IST Delhi NCR."
            ),
            "github": "https://github.com/hemagdg24-prog/pmajayportal7",
            "live": "https://pm-ajay-scheme.vercel.app/",
            "icon": "🏛️",
        },
        {
            "name": "Krishi Sakhi — AI Farmer Assistant",
            "date": "2025 – 2026",
            "tech": ["Python", "Flask", "Machine Learning", "AI API", "Render"],
            "description": (
                "An intelligent agricultural assistant developed to empower farmers with AI-driven "
                "crop recommendations, soil condition analysis, weather forecasting insights, and "
                "plant disease diagnostics to optimize yield."
            ),
            "github": "https://github.com/hemagdg24-prog",
            "live": "https://krishi-sakhi-1.onrender.com/",
            "icon": "🌾",
        },
        {
            "name": "2026 World — AI Career Platform",
            "date": "Currently Working",
            "status": "Currently Working",
            "is_current": True,
            "tech": ["Python", "Flask", "REST API", "Bootstrap"],
            "description": (
                "AI-driven career advisor and welfare scheme benefit allocation platform using "
                "AI/ML tools with smart role-based administration and data-driven reporting."
            ),
            "github": "https://github.com/hemagdg24-prog/flask-app",
            "live": "https://hemapmajay.vercel.app",
            "icon": "🤖",
        },
        {
            "name": "MindAI — Health Awareness Chatbot",
            "date": "Mar 2024",
            "tech": ["Python", "Flask", "NLP", "AI API"],
            "description": (
                "Developed an AI-powered health chatbot providing informative guidance, "
                "leveraging NLP and machine learning for real-time mental health and wellness "
                "awareness, accessible through an intuitive digital interface."
            ),
            "github": "https://github.com/hemagdg24-prog",
            "live": None,
            "icon": "🧠",
        },
        
    ],
    "achievements": [
        {
            "title": "Smart India Hackathon (SIH)",
            "subtitle": "Finalist & Winner",
            "org": "Ministry of Education · Delhi NCR",
            "year": "2025 – 2026",
            "badge": "National Finalist",
            "description": "Selected among thousands of nationwide participants to solve real-world governance challenges with innovative AI & software solutions.",
            "icon": "🏆",
        },
        {
            "title": "Ideathon Winner",
            "subtitle": "1st Prize Winner",
            "org": "Engineering Fest",
            "year": "2025 – 2026",
            "badge": "1st Place",
            "description": "Awarded 1st place champion for conceptualizing and prototyping high-impact scalable technology architecture.",
            "icon": "🥇",
        },
        {
            "title": "Project Expo Winner",
            "subtitle": "Winner — AI/ML Track",
            "org": "Institute of Science and Technology, Delhi NCR",
            "year": "2025 – 2026",
            "badge": "Track Champion",
            "description": "Secured top honours in the AI/ML competition for engineering and deploying a functional machine learning welfare platform.",
            "icon": "🎖️",
        },
    ],
    "certifications": [
        {
            "name": "Google Cloud Fundamentals Certification",
            "issuer": "Google",
            "icon": "☁️",
        },
        {
            "name": "Generative AI Training",
            "issuer": "Google Cloud",
            "icon": "🤖",
        },
        {
            "name": "Smart India Hackathon — AI & Cyber Certification",
            "issuer": "Government of India",
            "icon": "🇮🇳",
        },
        {
            "name": "AWS Cloud Practitioner Foundations",
            "issuer": "Amazon Web Services",
            "icon": "🔶",
        },
    ],
    "activities": [
        "Participated in Smart India Hackathon 2024",
        "Tech-Talk Session 2023 – Participated in Offline AI, Language AI Camp",
        "DevFest Hackathon 2024 – Participated in Machine Learning track",
        "MHM SANSAD AI Premium Post – Anchoring, Felicitation, Proof-reading, Lobby, and Token Power",
    ],
}

# ─── Routes ──────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html', data=PORTFOLIO_DATA)


@app.route('/about')
def about():
    return render_template('about.html', data=PORTFOLIO_DATA)


@app.route('/projects')
def projects():
    return render_template('projects.html', data=PORTFOLIO_DATA)


@app.route('/skills')
def skills():
    return render_template('skills.html', data=PORTFOLIO_DATA)


@app.route('/contact')
def contact():
    return render_template('contact.html', data=PORTFOLIO_DATA)


@app.route('/resume')
def resume():
    return redirect(url_for('static', filename='images/hemaresume.pdf'))


@app.route('/api/portfolio', methods=['GET'])
def api_portfolio():
    """JSON API endpoint that returns portfolio data"""
    return jsonify(PORTFOLIO_DATA)


@app.route('/contact/submit', methods=['POST'])
def contact_submit():
    """Handle contact form submission"""
    name    = request.form.get('name', '').strip()
    email   = request.form.get('email', '').strip()
    subject = request.form.get('subject', '').strip()
    message = request.form.get('message', '').strip()

    errors = []
    if not name:
        errors.append('Name is required.')
    if not email or '@' not in email:
        errors.append('A valid email is required.')
    if not message:
        errors.append('Message is required.')

    if errors:
        return jsonify({'success': False, 'errors': errors}), 400

    # In production, integrate Flask-Mail or a service like SendGrid here.
    # For now we log and return success.
    print(f"[{datetime.now()}] Contact from {name} <{email}>: {subject}\n{message}")

    return jsonify({
        'success': True,
        'message': f"Thank you {name}! Your message has been received. I'll get back to you soon.",
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
