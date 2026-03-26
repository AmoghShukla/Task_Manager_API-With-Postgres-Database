# 📝 Task Manager API

A RESTful API for managing tasks, built with **FastAPI** and **PostgreSQL**. Supports full CRUD operations on tasks, database migrations via **Alembic**, and is ready to run locally with a simple setup.

---

## 🚀 Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| Database | PostgreSQL |
| ORM | SQLAlchemy |
| Migrations | Alembic |
| Validation | Pydantic |
| Server | Uvicorn |
| DB Driver | psycopg2-binary |

---

## 📁 Project Structure

```
Task_Manager_API/
├── alembic/                        # Alembic migration setup
│   ├── versions/                   # Auto-generated migration files
│   ├── env.py                      # Alembic environment config
│   ├── README
│   └── script.py.mako              # Migration script template
├── src/
│   ├── core/
│   │   └── logger.py               # App-level logger setup
│   ├── database/
│   │   ├── __init__.py
│   │   ├── base.py                 # SQLAlchemy declarative Base
│   │   └── engine.py               # DB engine & session factory
│   ├── logs/
│   │   └── app.log                 # Application log output
│   ├── models/
│   │   └── task_model.py           # Task SQLAlchemy ORM model
│   ├── repository/
│   │   └── Task_repo.py            # DB query logic (data access layer)
│   ├── routers/
│   │   └── task_routes.py          # FastAPI route definitions
│   ├── schema/
│   │   └── Task_Schema.py          # Pydantic request/response schemas
│   ├── services/
│   │   └── task_service.py         # Business logic layer
│   └── utils/
│       └── Task_logger.py          # Task-specific logging utilities
├── main.py                         # App entry point
├── config.py                       # Environment settings (pydantic-settings)
├── alembic.ini                     # Alembic configuration
├── requirements.txt
├── .env                            # Environment variables (not committed)
└── .gitignore
```

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AmoghShukla/Task_Manager_API-With-Postgres-Database.git
cd Task_Manager_API-With-Postgres-Database
```

### 2. Create & Activate a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://<username>:<password>@localhost:5432/<database_name>
```

**Example:**

```env
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/Task_Manager_DB
```

> ⚠️ Never commit your `.env` file. It is already listed in `.gitignore`.

### 5. Create the PostgreSQL Database

Make sure PostgreSQL is running, then create the database:

```sql
CREATE DATABASE Task_Manager_DB;
```

### 6. Run Database Migrations

```bash
alembic upgrade head
```

### 7. Start the Server

```bash
uvicorn main:app --reload
```

The API will be live at: **http://127.0.0.1:8000**

---

## 📖 API Documentation

FastAPI auto-generates interactive docs:

| UI | URL |
|---|---|
| Swagger UI | http://127.0.0.1:8000/docs |
| ReDoc | http://127.0.0.1:8000/redoc |

---

## 🔌 API Endpoints

### Base

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check — confirms API is running |

### Tasks

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/tasks` | Retrieve all tasks |
| `GET` | `/tasks/{id}` | Retrieve a single task by ID |
| `POST` | `/tasks` | Create a new task |
| `PUT` | `/tasks/{id}` | Update an existing task |
| `DELETE` | `/tasks/{id}` | Delete a task |

---

## 🗄️ Database Migrations (Alembic)

| Command | Description |
|---|---|
| `alembic upgrade head` | Apply all migrations |
| `alembic revision --autogenerate -m "message"` | Generate a new migration |
| `alembic downgrade -1` | Roll back the last migration |

---

## 📦 Dependencies

```
fastapi
uvicorn
sqlalchemy
psycopg2-binary
pydantic
python-dotenv
```

Install all with:

```bash
pip install -r requirements.txt
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
