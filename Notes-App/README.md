# Notes App

A simple and elegant note-taking web application built with **FastAPI** and **MongoDB**.

## Features

- Create, read, update, and delete notes
- Mark notes as important
- Clean and responsive web interface
- MongoDB integration for data persistence
- RESTful API endpoints
- Static file serving (CSS styling)

## Project Structure

```
Notes-App/
├── index.py                 # Main FastAPI application entry point
├── config/
│   └── db.py               # MongoDB connection configuration
├── models/
│   └── note.py             # Pydantic data models
├── routes/
│   ├── note.py             # Note API routes
│   └── about.py            # About page route
├── schema/
│   └── note.py             # Database schema definitions
├── templates/
│   ├── index.html          # Home page template
│   ├── edit.html           # Edit note template
│   └── about.html          # About page template
├── static/
│   └── style.css           # CSS styling
└── env/                    # Python virtual environment
```

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn
- PyMongo
- Pydantic

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd Notes-App
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv env
   env\Scripts\activate  # On Windows
   source env/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn pymongo python-dotenv pydantic
   ```

4. **Configure MongoDB connection:**
   - Edit `config/db.py` and update the `MONGO_URI` with your MongoDB connection string

## Running the Application

Start the development server:

```bash
uvicorn index:app --reload
```

The application will be available at:
- **Web Interface:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs
- **Alternative API Docs:** http://localhost:8000/redoc

## API Endpoints

- `GET /` - View all notes (homepage)
- `POST /add` - Create a new note
- `GET /edit/{note_id}` - Edit a note
- `PUT /update/{note_id}` - Update a note
- `DELETE /delete/{note_id}` - Delete a note
- `GET /about` - About page

## Note Schema

```json
{
  "title": "string",
  "desc": "string",
  "important": "boolean (optional)"
}
```

## Technologies Used

- **Framework:** FastAPI
- **Database:** MongoDB
- **ORM:** PyMongo
- **Validation:** Pydantic
- **Server:** Uvicorn
- **Frontend:** HTML/CSS

## License

This project is open source and available under the MIT License.

## Author

Created by Rafay Ali
