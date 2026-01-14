AI-Powered RFP Management System

An end-to-end AI-powered system that automates Request for Proposal (RFP) creation, vendor communication, proposal ingestion, and vendor recommendation.

Built as a real-world procurement workflow using Django, OpenAI, and SMTP email integration.

🚀 Features

AI-generated RFPs
Convert plain-English procurement requirements into structured RFPs using OpenAI.

Vendor Management
Add and manage vendors to whom RFPs can be sent.

Automated RFP Distribution
Send RFPs to multiple vendors via real email (SMTP).

Proposal Ingestion
Capture and store vendor proposals received via email.

AI-based Vendor Recommendation
Compare proposals and recommend the best vendor based on cost, delivery, warranty, and payment terms.

Modern UI
Clean, responsive frontend built with Tailwind CSS.

🧠 Tech Stack

Backend

Python 3

Django

SQLite (for simplicity)

AI

OpenAI API (GPT-4 family)

Email

Gmail SMTP (App Password)

Frontend

Django Templates

Tailwind CSS (CDN)

🏗️ Architecture Overview
User (Browser)
   ↓
Django Views & Templates
   ↓
REST-style API Endpoints
   ↓
Database (RFPs, Vendors, Proposals)
   ↓
External Services
   ├── OpenAI (RFP generation & recommendations)
   └── SMTP (Email sending)


Key design choices:

Clear separation between frontend pages and API endpoints

External services (AI, email) isolated behind service logic

Fault-tolerant email sending (one bad email does not block others)

⚙️ Setup Instructions
1. Clone the repository
git clone https://github.com/your-username/ai-rfp-management-system.git
cd ai-rfp-management-system

2. Create virtual environment & install dependencies
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Environment variables

Create a .env file in the project root:

SECRET_KEY=your-django-secret-key
DEBUG=True

OPENAI_API_KEY=your-openai-api-key

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=yourgmail@gmail.com
EMAIL_HOST_PASSWORD=your-gmail-app-password
EMAIL_USE_TLS=True


⚠️ Do not commit .env to GitHub

4. Run migrations
python manage.py migrate

5. Start the server
python manage.py runserver


Visit:

http://127.0.0.1:8000/

🧪 End-to-End Workflow

Create RFP
Enter procurement requirements in plain English → AI generates structured RFP.

Manage Vendors
Add vendor names and email addresses.

Send RFP
Select an RFP and vendors → RFP is sent via email.

Receive Proposals
Vendors reply via email → proposals are ingested.

Compare & Recommend
AI analyzes proposals and recommends the best vendor.

⚠️ Error Handling & Tradeoffs

Email sending is handled per vendor, so a single invalid email does not block dispatch.

SQLite is used for simplicity; can be replaced with PostgreSQL in production.

Tailwind is loaded via CDN for speed; production builds should use compiled CSS.

🔮 Future Improvements

Authentication & role-based access

Async email processing (Celery)

Rich proposal comparison UI

Vendor scoring customization

Production-grade deployment setup

📌 Summary

This project demonstrates:

Full-stack development

API integrations

Real-world system design

Error handling and tradeoff reasoning

Ability to ship a complete, working product

📽️ Demo

A short walkthrough video demonstrates:

RFP creation

Vendor management

Email dispatch

Proposal comparison

AI-based recommendation

👤 Author

Tarun HT
Software Engineer
