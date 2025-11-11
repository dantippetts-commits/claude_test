# Vercel Deployment Guide

Quick guide to deploy your To-Do List app on Vercel.

## Quick Deploy

### Option 1: Deploy via Vercel Dashboard (Recommended)

1. **Push your code to GitHub:**
```bash
# Initialize git if not done
git init

# Add all files
git add .

# Commit changes
git commit -m "Ready for Vercel deployment"

# Create a new repository on GitHub, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

2. **Deploy on Vercel:**
   - Visit [vercel.com/new](https://vercel.com/new)
   - Sign in with GitHub
   - Click "Import Project"
   - Select your repository
   - Vercel auto-detects settings from `vercel.json`
   - Click "Deploy"

3. **Done!** Your app will be live at `https://your-app-name.vercel.app`

### Option 2: Deploy via Vercel CLI

1. **Install Vercel CLI:**
```bash
npm install -g vercel
```

2. **Login to Vercel:**
```bash
vercel login
```

3. **Deploy:**
```bash
vercel
```

4. **Deploy to production:**
```bash
vercel --prod
```

## Important Considerations

### Database Persistence

The current setup uses SQLite, which has limitations on Vercel:

- **Ephemeral Storage**: Data stored in `/tmp` is temporary
- **Serverless Nature**: Each request may hit a different instance
- **Data Loss**: Data will be lost when the function restarts

### Recommended Database Solutions

For production deployment, consider these alternatives:

#### 1. Vercel Postgres (Easiest)
- Free tier available
- Native Vercel integration
- [Setup Guide](https://vercel.com/docs/storage/vercel-postgres)

**Setup:**
```bash
# Add in Vercel Dashboard → Storage → Create Database → Postgres
```

#### 2. MongoDB Atlas
- Free tier available
- Great for JSON-like data
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)

**Install:**
```bash
pip install pymongo dnspython
```

#### 3. PlanetScale
- MySQL-compatible
- Generous free tier
- [PlanetScale](https://planetscale.com/)

**Install:**
```bash
pip install mysql-connector-python
```

## Testing Before Deploy

Always test locally before deploying:

```bash
# Run locally
python app.py

# Visit http://localhost:5000
```

## Environment Variables

If you add a cloud database, set environment variables in Vercel:

1. Go to your project on Vercel
2. Settings → Environment Variables
3. Add your database connection strings

Example variables:
- `DATABASE_URL`
- `MONGODB_URI`
- `POSTGRES_URL`

## Troubleshooting

### Build Fails
- Check that `requirements.txt` includes all dependencies
- Verify Python version compatibility (3.9+ recommended)

### App Doesn't Load
- Check Vercel function logs in Dashboard
- Verify `vercel.json` routes are correct

### Data Not Persisting
- This is expected with SQLite on Vercel
- Implement a cloud database for persistence

## Custom Domain

To use a custom domain:

1. Go to Project Settings → Domains
2. Add your domain
3. Follow DNS configuration instructions

## Resources

- [Vercel Documentation](https://vercel.com/docs)
- [Vercel Python Runtime](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
- [Vercel CLI Reference](https://vercel.com/docs/cli)
