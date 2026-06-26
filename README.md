# 🗄️ SQL Agent Chatbot
> Natural language → SQL queries, powered by **LangChain + OpenAI + SQLite + Flask**

---

## 📁 Project Structure

```
sql_agent_chatbot/
│
├── app.py            ← Flask server (run this)
├── agent.py          ← LangChain SQL Agent logic
├── create_db.py      ← Creates company.db with sample data
├── requirements.txt  ← Python dependencies
├── .env              ← Your OpenAI API key goes here
│
└── static/
    └── index.html    ← Chat UI (served by Flask)
```

---

## 🚀 How to Run in VS Code

### Step 1 — Open the folder in VS Code
Extract the zip, then:
```
File → Open Folder → select `sql_agent_chatbot`
```

### Step 2 — Open the Terminal
```
Terminal → New Terminal   (or Ctrl + `)
```

### Step 3 — Create a virtual environment
```bash
python -m venv venv
```

Activate it:
- **Windows:**  `venv\Scripts\activate`
- **Mac/Linux:** `source venv/bin/activate`

### Step 4 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 5 — Add your Groq API key
Open `.env` and replace the placeholder:
```
GROQ_API_KEY=your-groq-api-key-here
```
Get your key from: https://console.groq.com/account/api-keys

### Step 6 — Create the sample database
```bash
python create_db.py
```
This creates `company.db` with employees, departments, and projects.

### Step 7 — Start the server
```bash
python app.py
```
You'll see:
```
🔧 Initializing SQL Agent...
✅ SQL Agent ready!
 * Running on http://127.0.0.1:5000
```

### Step 8 — Open the chatbot
Go to: **http://localhost:5000**

---

## 💬 Sample Questions to Try

| Question | What it does |
|---|---|
| Who are the top 3 highest-paid employees? | Sorts by salary DESC |
| List all In Progress projects | Filters by status |
| Which department has the highest budget? | Aggregation |
| How many employees are in each department? | GROUP BY |
| Show employees hired after 2022 | Date filtering |
| Which employees are assigned to project 4? | JOIN query |

---

## 🧠 How it Works

```
User types question
       ↓
Flask /api/chat endpoint
       ↓
LangChain SQL Agent (GPT-3.5-turbo)
  → inspects DB schema
  → writes SQL query
  → executes it on company.db
  → interprets results
       ↓
Natural language answer returned to UI
```

---

## ⚙️ Customizing

**Change the database:** Edit `db_path` in `app.py → build_agent()`

**Use GPT-4:** Edit `model` in `app.py → build_agent(model="gpt-4")`

**Connect your own DB:** Replace the SQLite URI in `agent.py`:
```python
db = SQLDatabase.from_uri("postgresql://user:pass@host/dbname")
```
