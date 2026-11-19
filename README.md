<!-- ✨ Animated banner: generated in github.com/Neelimapasala/Neelimapasala -->
<p align="center">
  <a href="https://github.com/Neelimapasala"><img src="https://raw.githubusercontent.com/Neelimapasala/Neelimapasala/output/banner-querymind.svg?v=1" width="100%" alt="QueryMind · SQL Agent: Talk to your database in plain English."/></a>
</p>

<p align="center">
  <img src="https://img.shields.io/github/languages/top/Neelimapasala/SQL-agent-chatbot?style=for-the-badge&color=7f00ff&labelColor=0d1117" alt="top language"/>
  <img src="https://img.shields.io/github/last-commit/Neelimapasala/SQL-agent-chatbot?style=for-the-badge&color=00d4ff&labelColor=0d1117" alt="last commit"/>
  <img src="https://img.shields.io/github/stars/Neelimapasala/SQL-agent-chatbot?style=for-the-badge&color=ff2bd6&labelColor=0d1117" alt="stars"/>
  <img src="https://img.shields.io/badge/AGENTIC%20AI-a78bfa?style=for-the-badge&labelColor=0d1117" alt="AGENTIC AI"/>
</p>

<p align="center"><img src="https://raw.githubusercontent.com/Neelimapasala/Neelimapasala/output/divider.svg?v=1" width="100%"/></p>

# 🧠 QueryMind — Natural Language SQL Agent

QueryMind lets you ask questions about your database in plain English. An AI agent writes the SQL, runs it against your database, and returns a clean, readable answer — no SQL knowledge required.

> Built as part of a hands-on Agentic AI learning journey — exploring how LLM agents reason, plan, and act on real data.

---

## ✨ Features

- **Natural language → SQL** — ask "Who are the top 3 highest-paid employees?" and get an instant answer
- **Live schema browser** — searchable sidebar showing every table and column
- **Query history** — last 5 questions saved and reusable with one click
- **Chat persistence** — conversation survives page refresh (stored in `localStorage`)
- **Error handling with retry** — failed requests show a clear error and a one-click retry
- **Offline detection** — automatically detects if the Flask backend is down and shows a banner
- **Input validation** — blocks empty input, overly long questions, and raw SQL injection attempts
- **Auto-rendered result tables** — tabular answers render as a real HTML table, not plain text
- **Copy buttons** — copy the generated SQL or the full answer in one click
- **Model selector** — switch between Groq models (`llama-3.3-70b-versatile`, `llama-3.1-8b-instant`, `mixtral-8x7b`)
- **Dark / light theme toggle**
- **Query execution time** displayed per response
- **Chat export** — download the full conversation as a `.txt` file

---

## 🏗️ Tech Stack

| Layer       | Technology                          |
|-------------|--------------------------------------|
| Agent       | LangChain SQL Agent + Groq API       |
| Backend     | Flask (Python)                       |
| Frontend    | Single-file HTML/CSS/JS (no build tools) |
| Database    | SQLite (`company.db`)                |

---

## 📁 Project Structure

```
querymind/
├── app.py              # Flask server + API routes
├── agent.py            # LangChain SQL agent setup & query execution
├── company.db          # SQLite database
├── static/
│   └── index.html      # Frontend (chat UI)
├── .env                # API keys (not committed)
└── requirements.txt
```

---

## ⚙️ Setup

### 1. Clone & install dependencies
```bash
git clone <your-repo-url>
cd querymind
pip install -r requirements.txt
```

### 2. Add your environment variables
Create a `.env` file in the project root:
```
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Run the app
```bash
python app.py
```

This starts the Flask server on `http://127.0.0.1:5000/` and **automatically opens it in your default browser** — no Live Server, no VS Code extension needed.

---

## 🧩 How It Works

1. You type a question in the chat input.
2. The frontend sends it to `POST /api/chat`.
3. The LangChain agent interprets the question, generates SQL against the known schema, and executes it on `company.db`.
4. The result is returned as a natural language answer (with the generated SQL attached) and rendered in the UI — as a table if the data is tabular.

---

## 🔌 API Endpoints

| Method | Endpoint        | Description                                  |
|--------|-----------------|-----------------------------------------------|
| GET    | `/`             | Serves the frontend (`static/index.html`)     |
| GET    | `/api/schema`   | Returns the database schema (tables/columns)  |
| POST   | `/api/chat`     | Accepts `{ "question": "...", "model": "..." }`, returns `{ "answer": "..." }` |

---

## 🗄️ Sample Schema

- **departments** — id, name, budget
- **employees** — id, name, department_id, role, salary, hire_date
- **projects** — id, title, dept_id, status, budget, start_date, end_date
- **project_assignments** — employee_id, project_id, role

---

## 🚧 Roadmap / Ideas

- [ ] Wire the model selector through to `agent.py` for true per-request model switching
- [ ] Multi-database support
- [ ] Streaming responses
- [ ] User authentication for multi-user deployments
- [ ] Query result charting (bar/line/pie)

---

## 📜 License

This project is open for personal and educational use. Adapt freely.

---

## 🙋 About

Built while learning Agentic AI hands-on — exploring how to take LLM agents beyond chat into real, structured, production-style tools.


<p align="center"><img src="https://raw.githubusercontent.com/Neelimapasala/Neelimapasala/output/divider.svg?v=1" width="100%"/></p>

<p align="center">
  <a href="https://github.com/Neelimapasala"><img src="https://raw.githubusercontent.com/Neelimapasala/Neelimapasala/output/repo-footer.svg?v=1" width="100%" alt="Crafted by Neelima Pasala"/></a>
</p>
