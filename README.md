# 🚀 Task Manager API

Production-ready REST API built with FastAPI, featuring authentication, task management, and cloud deployment.

## 🌐 Live Demo
http://13.58.90.10:8000/docs

## 🛠️ Tech Stack

- FastAPI
- SQLAlchemy
- JWT Authentication
- Docker
- AWS EC2

## 🔐 Features

- User registration & authentication (JWT)
- Protected routes
- Task CRUD (Create, Read, Update, Delete)
- Secure password hashing
- Modular architecture

## ☁️ Deployment

Deployed on AWS EC2 using Docker containers.

## 📦 Run locally

```bash
docker build -t task-manager-api .
docker run -p 8000:8000 task-manager-api
