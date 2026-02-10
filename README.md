# 🥗 Nutrition AI – AI Powered Diet Improvement Notifier

Nutrition AI is an AI-powered notification system that analyzes a user’s daily meals — breakfast, lunch, and dinner — and provides scientifically guided diet improvement recommendations. The system learns from the user’s complete daily diet pattern and sends personalized improvement suggestions via email.

---

## 📌 Project Motivation

Maintaining a healthy diet requires consistency, awareness, and scientific guidance — which is often difficult to achieve manually.  

**Nutrition AI** aims to automate this process by:
- Continuously analyzing daily dietary inputs
- Applying AI-driven reasoning and scientific nutrition principles
- Providing timely, actionable feedback without manual intervention  

The goal is to create an **automated, intelligent nutrition guide** that helps people improve their eating habits in a practical and sustainable way.

---

## 🚀 Key Features

- 🧠 **AI-powered diet analysis** using Large Language Models  
- 🍽️ **Daily meal evaluation** (breakfast, lunch, and dinner)  
- 📊 **Learning-based analysis** of the user's full-day diet pattern  
- 📧 **Automated email notifications** with diet improvement plans  
- 🥦 **Personalized recommendations** based on food balance and habits  
- ⚡ **Fast and scalable backend** using modern web technologies  

---

## 🛠 Tech Stack

### **AI / Intelligence**
- OpenAI API (LLM-based reasoning and analysis)

### **Backend**
- Python
- FastAPI

### **Frontend**
- React

### **Database**
- PostgreSQL

### **Notifications**
- Email-based notification system

---

## 🧩 System Workflow

1. User logs their daily meals (breakfast, lunch, dinner)
2. Data is stored securely in the database
3. AI model analyzes the complete day’s diet
4. Scientific reasoning is applied to identify improvements
5. Personalized diet improvement plan is generated
6. Email notification is sent to the user with recommendations

---

## Installation & setup

### 1) Clone the repository

- `git clone https://github.com/gashutosh2501/Nutrition-AI.git`
- `cd Nutrition-AI`

### 2) Prerequisites

- Python 3.9+
- Node.js 18+
- PostgreSQL (running locally)

### 3) Backend (FastAPI)

1. Create a virtual environment and install dependencies:
   - `cd backend`
   - `python -m venv .venv`
   - `source .venv/bin/activate`
   - `pip install -r requirements.txt`

2. Create `backend/.env` with your secrets:
   - `OPENAI_API_KEY=your_api_key_here`
   - `SMTP_APP_PASSWORD=your_gmail_app_password` (only required if email features are used)

3. Configure the database connection in `database/database.py` if your local Postgres settings differ.

### 4) Database (PostgreSQL)

1. Create a database named `nutrition_db` (or update the connection string in `database/database.py`).
2. Run the schema in `database/schema.sql` to create the `meals` table.

### 5) Run the API

From the repo root (with the virtual environment active):

- `uvicorn backend.main:app --reload`

API should be available at `http://localhost:8000`.

### 6) Frontend (Vite + React)

1. Install dependencies:
   - `cd frontend`
   - `npm install`

2. Start the dev server:
   - `npm run dev`

Frontend should be available at `http://localhost:5173`.

# Email Configuration (Important)

This application sends a **daily nutrition summary email** once a user has logged **breakfast, lunch, and dinner** for the day.

## Required setup

The recipient email address is currently **hard-coded** in the backend and must be updated before running the app.

**File to edit:** `backend/agents/nutrition_agent.py`

**Current code:**

- `to="g.ashutosh2502@gmail.com"`

## What you need to do

Replace the email with your own:

- `to="your-email@example.com"`

Once dinner is recorded, the app will automatically send the daily nutrition summary to this email.

## Note

This is a **temporary setup**. In production, the email should be fetched dynamically from the authenticated user profile instead of being hard-coded.

