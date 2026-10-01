# QSS | Home Services Marketplace

> A full-stack service marketplace that connects customers with trusted professionals for on-demand home and personal services.

## 🚀 Overview

QSS is a Django-based marketplace designed to simplify the process of discovering, comparing, and booking professional services. The platform brings customers and service providers together through structured service listings, provider profiles, booking workflows, dashboards, and role-based access.

The project demonstrates full-stack application development with practical business workflows, responsive interfaces, structured backend development, and deployment-oriented engineering.

## ✨ Features

- Customer and service-provider authentication
- Service categories and service listings
- Provider profiles and service information
- Service discovery and booking workflows
- Customer dashboard and booking management
- Provider dashboard and service management
- Reviews and ratings
- Location-aware service discovery
- Role-based access control
- Responsive web interface
- Django database models and migrations
- Automated testing and CI workflow
- Deployment configuration

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- PostgreSQL
- HTML, CSS, JavaScript
- Bootstrap
- GitHub Actions
- Docker
- Render

## 📦 Installation

```bash
git clone https://github.com/Anurag20048/qss-new.git
cd qss-new
python -m venv .venv
```

Windows:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
```

## ▶️ Usage

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/`.

## 📁 Project Structure

```text
qss-new/
├── qss/
├── manage.py
├── templates/
├── static/
├── tests/
├── requirements.txt
└── README.md
```

## 🔧 Configuration

Use environment variables for local and deployment configuration. Keep application secrets outside version control.

```text
DJANGO_SECRET_KEY=your_secret_key
DJANGO_DEBUG=True
DATABASE_URL=your_database_url
```

## 🧪 Running Tests

```bash
python manage.py test
```

## 🗺️ Roadmap

- [ ] Online payment integration
- [ ] Advanced provider matching
- [ ] Real-time booking notifications
- [ ] Enhanced service analytics

## 🤝 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss the proposed improvement.

## 📄 License

See the `LICENSE` file for licensing information.

## 👤 Author

**Anurag Pareek**

- GitHub: https://github.com/Anurag20048
