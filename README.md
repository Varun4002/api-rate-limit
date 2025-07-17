# ⚡ FastAPI Rate-Limited Quote Generator

A simple full-stack project demonstrating how to implement **API rate limiting** using FastAPI middleware. It provides random motivational quotes and blocks users who exceed a set number of API requests per minute. Includes a React frontend to test and visualize the rate limit in action.

---

## 🚀 Features

- ✅ FastAPI backend with IP-based rate limiter
- ✅ React frontend to interact with the API
- ✅ Limits clients to **5 requests per minute**
- ✅ Returns `429 Too Many Requests` when limit is exceeded
- ✅ CORS-enabled for frontend-backend communication

---

## 🧠 How Rate Limiting Works

- Each user's IP address is tracked in memory.
- Requests are timestamped and stored in a list.
- Old requests (older than 60 seconds) are cleaned up automatically.
- If the number of recent requests ≥ 5, the user is blocked for the rest of the minute.

---

## ⚙️ Setup Instructions

### 🔧 Backend (FastAPI)

bash
cd backend
python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install fastapi uvicorn
uvicorn main:app --reload

💻 Frontend (React + Vite)
cd frontend
npm install
npm run dev

🔍 Sample Response Json
// Success
{
  "quote": "Dream big and dare to fail."
}

// Rate Limit Exceeded
{
  "detail": "Rate limit exceeded. Please wait a minute."
}

🧾 License

---

### ✅ How to Use It

1. Copy this whole thing.
2. Paste it in your `README.md` file in the root of your repo.
3. Commit and push:

```bash
git add README.md
git commit -m "Add project documentation"
git push
