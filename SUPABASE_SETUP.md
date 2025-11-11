# Supabase Setup Guide

This guide will help you set up Supabase as the database for your To-Do List application.

## What is Supabase?

Supabase is an open-source Firebase alternative that provides:
- PostgreSQL database (persistent, reliable)
- Real-time subscriptions
- Authentication
- Storage
- Auto-generated APIs

## Step 1: Create a Supabase Project

1. Go to [supabase.com](https://supabase.com) and sign up for a free account

2. Click **"New Project"**

3. Fill in the project details:
   - **Name**: `todo-app` (or your preferred name)
   - **Database Password**: Create a strong password (save this!)
   - **Region**: Choose the closest region to your users
   - **Plan**: Free tier is perfect for this app

4. Click **"Create new project"** and wait 1-2 minutes for setup

## Step 2: Create the Todos Table

1. In your Supabase dashboard, click **"Table Editor"** in the left sidebar

2. Click **"Create a new table"**

3. Configure the table:
   - **Name**: `todos`
   - **Enable Row Level Security (RLS)**: Uncheck for now (enable later for production)

4. Add the following columns:

   | Name | Type | Default Value | Additional Settings |
   |------|------|---------------|---------------------|
   | `id` | int8 | Auto-generated | Primary, Auto-increment |
   | `task` | text | - | Required (not nullable) |
   | `completed` | bool | false | - |
   | `created_at` | timestamptz | now() | - |

5. Click **"Save"**

### Alternative: Use SQL Editor

Instead of the UI, you can run this SQL in the **SQL Editor**:

```sql
CREATE TABLE todos (
  id BIGSERIAL PRIMARY KEY,
  task TEXT NOT NULL,
  completed BOOLEAN DEFAULT FALSE,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
```

## Step 3: Get Your Supabase Credentials

1. In your Supabase dashboard, click **"Settings"** (gear icon) in the left sidebar

2. Click **"API"** under Project Settings

3. Copy these values:
   - **Project URL** (looks like: `https://xxxxx.supabase.co`)
   - **anon public key** (under "Project API keys")

## Step 4: Configure Your Application

### For Local Development:

1. Create a `.env` file in your project root:

```bash
cp .env.example .env
```

2. Edit `.env` and add your credentials:

```env
SUPABASE_URL=https://your-project-id.supabase.co
SUPABASE_KEY=your-anon-public-key-here
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
python app.py
```

The app will now use Supabase instead of SQLite!

### For Vercel Deployment:

1. Go to your Vercel project dashboard

2. Navigate to **Settings** → **Environment Variables**

3. Add these variables:
   - **Name**: `SUPABASE_URL` | **Value**: Your Supabase URL
   - **Name**: `SUPABASE_KEY` | **Value**: Your Supabase anon key

4. Redeploy your application

## Step 5: Test Your Setup

1. Open your application in the browser

2. Add a few test todos

3. Go to your Supabase dashboard → **Table Editor** → **todos**

4. You should see your todos appear in real-time!

## Optional: Enable Row Level Security (RLS)

For production apps, you should enable RLS to secure your data:

1. In Supabase, go to **Authentication** → **Policies**

2. For the `todos` table, create policies like:

```sql
-- Allow all operations for now (public access)
CREATE POLICY "Enable all access for todos" ON todos
FOR ALL USING (true);
```

For more advanced security, refer to [Supabase RLS documentation](https://supabase.com/docs/guides/auth/row-level-security).

## Troubleshooting

### "Failed to create todo" error
- Check that your Supabase credentials are correct in `.env` or Vercel environment variables
- Verify the `todos` table exists in your Supabase dashboard
- Check the browser console for detailed error messages

### Data not appearing
- Confirm you're connected to Supabase (check the app logs)
- Verify table name is exactly `todos` (case-sensitive)
- Check column names match: `id`, `task`, `completed`, `created_at`

### Local SQLite still being used
- Make sure `.env` file exists in the project root
- Verify environment variables are set correctly
- Restart the Flask server after adding `.env`

## Benefits of Using Supabase

- **Persistent Data**: No data loss on serverless restarts
- **Real-time**: Can add live updates in the future
- **Scalable**: Handles thousands of users
- **Backups**: Automatic database backups
- **Free Tier**: 500MB database, 2GB bandwidth/month

## Migration from SQLite

If you have existing todos in SQLite, you can manually export them:

1. Export from SQLite:
```python
import sqlite3
conn = sqlite3.connect('todo.db')
todos = conn.execute('SELECT task, completed FROM todos').fetchall()
```

2. Import to Supabase using the Python client or SQL Editor

## Resources

- [Supabase Documentation](https://supabase.com/docs)
- [Supabase Python Client](https://supabase.com/docs/reference/python/introduction)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
