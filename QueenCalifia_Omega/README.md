
# QueenCalifia-Ω

This repository contains a minimal deployable version of the QueenCalifia-Ω stack. It features:

- ✅ Flask API with ingest and sync endpoints
- 👑 Dynamic dashboard UI
- ☁️ Simulated Google Drive sync

---

## 🛠 Project Structure

```
QueenCalifia_Omega/
├── main.py
├── drive_sync.py
├── requirements.txt
├── templates/
│   └── dashboard.html
├── log/
│   └── interactions.log
```

---

## 🚀 Deployment on Render

1. Push this repo to GitHub
2. Go to [https://render.com](https://render.com) and connect your GitHub
3. Create a new **Web Service**
4. Set the **Build Command** to:

```
pip install -r requirements.txt
```

5. Set the **Start Command** to:

```
python main.py
```

6. Set the environment to **Python 3.11**
7. Click **Deploy**

---

## 🔗 Live Access

After deployment, navigate to:

- `/dashboard`: Dashboard UI
- `/sync`: Log sync
- `/ingest`: POST endpoint to store cognitive data

---

🧠 Evolve QueenCalifia-Ω at will!
