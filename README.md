# To-Do API (FastAPI + SQLite)\nSimple CRUD API with FastAPI, SQLAlchemy, SQLite.

# 📝 FastAPI To-Do API  

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/)  
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green?logo=fastapi)](https://fastapi.tiangolo.com/)  
[![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey?logo=sqlite)](https://www.sqlite.org/)  
[![Tests](https://img.shields.io/badge/tests-pytest-yellow?logo=pytest)](https://docs.pytest.org/)  
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)  

---

## 📌 About the Project
This is a simple **To-Do API** built with **FastAPI + SQLAlchemy + SQLite**.  
The goal was to practice building a production-like backend project from scratch, including CRUD operations, database integration, validation, testing and containerization with Docker.  

This project is part of my **Computer Science journey** and also my **portfolio for job opportunities**, showing recruiters that I can structure a clean, well-documented and tested API.

---

## 🎯 Objectives
- Learn **how to design and implement RESTful APIs** in Python.  
- Practice **clean code organization** (models, schemas, CRUD, routes).  
- Apply **database integration** with SQLAlchemy + SQLite.  
- Use **Pydantic** for input validation.  
- Add **automated tests** with Pytest.  
- Make the project **easy to run** (venv + Docker).  

---

## 🛠️ Tech Stack
- **Python 3.12**  
- **FastAPI** (API framework)  
- **SQLAlchemy** (ORM for database)  
- **SQLite** (local DB for simplicity)  
- **Pydantic v2** (validation)  
- **Pytest** (testing)  
- **Docker** (containerization)

---

## 🚀 Quickstart

### Clone and run locally
```bash
git clone https://github.com/CaioFPaiva/fastapi-todo-api.git
cd fastapi-todo-api

python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\Activate
pip install -r requirements.txt

uvicorn app.main:app --reload

Run with Docker

docker build -t fastapi-todo .
docker run -p 8000:8000 fastapi-todo


🔍 API Overview

POST /tasks → create task

GET /tasks → list tasks

GET /tasks/{id} → get task by id

PATCH /tasks/{id} → update task (title, description, done)

DELETE /tasks/{id} → remove task

📚 What I Learned

How to structure a FastAPI project professionally (folders for models, schemas, crud, routes).

The importance of input validation with Pydantic.

How to use SQLAlchemy ORM with SQLite.

Writing unit/integration tests with Pytest.

Using Docker to containerize a Python API.

Writing a clear README in English to present a project to recruiters.

🚧 Next Steps

Add pagination and filtering to /tasks.

Implement user authentication (JWT/OAuth2).

Deploy to Render/Railway/Fly.io and provide live demo link.

Integrate with a simple frontend (React or HTML/JS).

🙋 About This Project

I developed this project as part of my studies in Computer Science at Estácio and as a way to build my international portfolio.

The main idea was to simulate a real-world project, showing recruiters that I can:

Work with modern frameworks used in the industry.

Write clean, tested and documented code.

Organize a repository that looks professional and easy to understand.

👉 This repository represents one of my first complete backend projects in Python. It shows not only coding ability, but also project organization, documentation and a professional mindset.
