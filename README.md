# Django Polling App

This is a simple polling web application built using the Django framework. It allows users to view polls, vote on them, and see results. This project is based on the official [Django tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/).

## 🔧 Features

- Create and manage questions with multiple choices
- Vote on poll questions
- View real-time results after voting
- Admin interface for managing polls

## 🚀 Getting Started

Follow these steps to get a local copy up and running:

### 1. Clone the repository

git clone https://github.com/Aditya12332/polling-website.git
cd polling-website

2. Create and activate a virtual environment

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt
4. Apply migrations and run the server
bash

python manage.py migrate
python manage.py runserver
Visit http://127.0.0.1:8000/polls/ in your browser.

🛠 Project Structure
bash

django-polling-app/
│
├── manage.py
├── mysite/           # Project config
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── polls/            # Poll app
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── templates/
    └── ...
🧑‍💻 Admin Access
To use the admin interface:

bash
Copy
Edit
python manage.py createsuperuser
Then go to: http://127.0.0.1:8000/admin/

📦 Requirements
You can generate requirements.txt with:

pip freeze > requirements.txt

