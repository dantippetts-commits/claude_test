import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Application configuration"""

    # Supabase configuration
    SUPABASE_URL = os.getenv('SUPABASE_URL')
    SUPABASE_KEY = os.getenv('SUPABASE_KEY')

    # Fallback to SQLite if Supabase not configured
    USE_SUPABASE = bool(SUPABASE_URL and SUPABASE_KEY)

    # SQLite configuration (fallback)
    SQLITE_DATABASE = os.path.join('/tmp', 'todo.db') if os.environ.get('VERCEL') else 'todo.db'
