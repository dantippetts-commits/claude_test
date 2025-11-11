# To-Do List Web Application

A simple and elegant web-based to-do list application built with Python Flask and vanilla JavaScript.

## Features

- **Add Tasks**: Create new to-do items
- **Mark Complete**: Check off tasks as you complete them
- **Edit Tasks**: Update task text inline
- **Delete Tasks**: Remove tasks you no longer need
- **Filter View**: View all, active, or completed tasks
- **Persistent Storage**: Tasks are saved in an SQLite database

## Installation

1. Make sure you have Python 3.7 or higher installed

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running Locally

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Deploying to Vercel

### Prerequisites
- A [Vercel account](https://vercel.com/signup)
- [Git](https://git-scm.com/) installed
- Your project pushed to a GitHub repository

### Deployment Steps

1. **Initialize Git repository (if not already done):**
```bash
git init
git add .
git commit -m "Initial commit"
```

2. **Push to GitHub:**
```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

3. **Deploy on Vercel:**
   - Go to [vercel.com](https://vercel.com) and sign in
   - Click "Add New Project"
   - Import your GitHub repository
   - Vercel will automatically detect the configuration from `vercel.json`
   - Click "Deploy"

4. **Access your deployed app:**
   - Once deployed, Vercel will provide you with a URL (e.g., `your-app.vercel.app`)

### Important Notes for Vercel Deployment

- **Data Persistence**: On Vercel, the SQLite database is stored in `/tmp` which is ephemeral. This means:
  - Data will be lost when the serverless function restarts
  - For production use, consider using a persistent database like:
    - [Vercel Postgres](https://vercel.com/docs/storage/vercel-postgres)
    - [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
    - [PlanetScale](https://planetscale.com/)
    - Any other cloud database service

- **Environment Variables**: Can be configured in Vercel Dashboard → Project Settings → Environment Variables

## Project Structure

```
todo-app/
├── app.py              # Flask backend with API endpoints
├── vercel.json         # Vercel deployment configuration
├── requirements.txt    # Python dependencies
├── .gitignore          # Git ignore rules
├── todo.db             # SQLite database (created automatically, local only)
├── templates/
│   └── index.html      # Main HTML page
└── static/
    ├── style.css       # Styling
    └── script.js       # Frontend JavaScript
```

## API Endpoints

- `GET /api/todos` - Get all todos
- `POST /api/todos` - Create a new todo
- `PUT /api/todos/<id>` - Update a todo (mark complete or edit text)
- `DELETE /api/todos/<id>` - Delete a todo

## Usage

1. Type a task in the input field and click "Add Task" or press Enter
2. Click the checkbox to mark a task as complete/incomplete
3. Click "Edit" to modify a task's text
4. Click "Delete" to remove a task
5. Use the filter buttons to view All, Active, or Completed tasks

## Technologies Used

- **Backend**: Python Flask
- **Database**: SQLite
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **No external frontend frameworks** - keeping it simple!

## License

Free to use and modify as needed.
