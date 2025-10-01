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
