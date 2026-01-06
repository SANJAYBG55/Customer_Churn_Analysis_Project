# 🚀 Deployment Guide

## Overview

This guide provides step-by-step instructions for deploying the Customer Churn Analysis Dashboard to various platforms.

**Deployment Options:**
1. **Local Deployment** (Development)
2. **Streamlit Cloud** (Recommended for demos/portfolio)
3. **Heroku** (Production-ready)
4. **Docker** (Containerized deployment)

---

## Option 1: Local Deployment

### Prerequisites
- Python 3.8+
- pip installed
- Project files downloaded

### Setup Steps

1. **Navigate to project directory**
```bash
cd customer_churn_analysis
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Verify data files exist**
```bash
# Windows
dir data\processed\enriched_churn_data.csv

# Mac/Linux
ls data/processed/enriched_churn_data.csv
```

4. **Launch dashboard**
```bash
streamlit run dashboard/churn_dashboard.py
```

5. **Access dashboard**
- Automatically opens in browser at `http://localhost:8501`
- If not, manually navigate to the URL

### Stopping the Server
Press `Ctrl+C` in the terminal

---

## Option 2: Streamlit Cloud (Recommended)

**Best For:** Portfolio showcases, demos, sharing with recruiters

**Advantages:**
- ✅ Free tier available
- ✅ One-click deployment
- ✅ HTTPS enabled
- ✅ Public shareable URL
- ✅ Auto-updates from GitHub

### Prerequisites
- GitHub account
- Streamlit Cloud account (free: [share.streamlit.io](https://share.streamlit.io))
- Project pushed to GitHub repository

### Step 1: Prepare Repository

1. **Create GitHub repository**
```bash
git init
git add .
git commit -m "Initial commit: Customer Churn Analysis"
git branch -M main
git remote add origin https://github.com/yourusername/customer_churn_analysis.git
git push -u origin main
```

2. **Ensure required files in root**
- `requirements.txt`
- `dashboard/churn_dashboard.py`
- `data/processed/enriched_churn_data.csv`

### Step 2: Deploy to Streamlit Cloud

1. **Sign up for Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub account

2. **Create new app**
   - Click "New app"
   - Select your repository
   - Branch: `main`
   - Main file path: `dashboard/churn_dashboard.py`
   - Click "Deploy"

3. **Wait for deployment** (2-5 minutes)
   - Streamlit Cloud installs dependencies
   - Builds and launches app

4. **Access your app**
   - Receives public URL: `https://yourusername-customer-churn-analysis.streamlit.app`
   - Share this URL with recruiters/stakeholders

### Step 3: Configure Settings (Optional)

**Custom Domain:**
- Streamlit Cloud → Settings → Custom domain
- Add your domain (requires DNS configuration)

**Environment Secrets:**
- For API keys or sensitive data
- Settings → Secrets → Add key-value pairs

**Resource Limits:**
- Free tier: 1GB RAM, 1 CPU core
- Sufficient for this project

### Troubleshooting Streamlit Cloud

**Issue: Deployment fails**
- Check `requirements.txt` has all dependencies
- Verify file paths are relative (not absolute)
- Check Streamlit Cloud logs for errors

**Issue: Data file not found**
- Ensure `data/processed/enriched_churn_data.csv` exists in repo
- Verify path is relative: `data/processed/enriched_churn_data.csv`
- Check file is not in `.gitignore`

**Issue: Out of memory**
- Dataset too large for free tier
- Consider data sampling in dashboard code
- Upgrade to Streamlit Cloud Pro

---

## Option 3: Heroku Deployment

**Best For:** Production deployment, enterprise use

**Advantages:**
- ✅ Always-on server
- ✅ Custom domain support
- ✅ Database add-ons available
- ✅ SSL/HTTPS included
- ✅ Scalable

### Prerequisites
- Heroku account (free tier available)
- Heroku CLI installed
- Git installed

### Step 1: Install Heroku CLI

**Windows:**
Download from [heroku.com/cli](https://devcenter.heroku.com/articles/heroku-cli)

**Mac:**
```bash
brew tap heroku/brew && brew install heroku
```

**Linux:**
```bash
curl https://cli-assets.heroku.com/install.sh | sh
```

### Step 2: Prepare Application

1. **Create Procfile** (in project root)
```bash
web: sh setup.sh && streamlit run dashboard/churn_dashboard.py
```

2. **Create setup.sh** (in project root)
```bash
mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your.email@example.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml
```

3. **Make setup.sh executable**
```bash
chmod +x setup.sh
```

4. **Verify requirements.txt exists**
- Should already exist from earlier steps

### Step 3: Deploy to Heroku

1. **Login to Heroku**
```bash
heroku login
```

2. **Create Heroku app**
```bash
heroku create customer-churn-analysis-app
```

3. **Initialize git (if not already)**
```bash
git init
git add .
git commit -m "Prepare for Heroku deployment"
```

4. **Deploy**
```bash
git push heroku main
```

5. **Open app**
```bash
heroku open
```

### Step 4: Monitor and Manage

**View logs:**
```bash
heroku logs --tail
```

**Restart app:**
```bash
heroku restart
```

**Scale dynos:**
```bash
heroku ps:scale web=1
```

### Troubleshooting Heroku

**Issue: Application error**
- Check logs: `heroku logs --tail`
- Verify Procfile and setup.sh exist
- Ensure requirements.txt complete

**Issue: Slug size too large**
- Heroku free tier: 500MB limit
- Remove unnecessary files
- Use `.slugignore` to exclude files

**Issue: App sleeps (free tier)**
- Free dynos sleep after 30 min inactivity
- Upgrade to paid tier for always-on

---

## Option 4: Docker Deployment

**Best For:** Containerized environments, cloud platforms (AWS, Azure, GCP)

**Advantages:**
- ✅ Portable across environments
- ✅ Consistent deployment
- ✅ Easy scaling
- ✅ Isolation

### Prerequisites
- Docker installed ([docker.com](https://www.docker.com/))

### Step 1: Create Dockerfile

**File:** `Dockerfile` (in project root)

```dockerfile
# Use official Python runtime as base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run dashboard
ENTRYPOINT ["streamlit", "run", "dashboard/churn_dashboard.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### Step 2: Create .dockerignore

**File:** `.dockerignore`

```
__pycache__
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.git
.gitignore
README.md
*.md
.DS_Store
```

### Step 3: Build Docker Image

```bash
docker build -t churn-dashboard .
```

### Step 4: Run Container

```bash
docker run -p 8501:8501 churn-dashboard
```

Access at `http://localhost:8501`

### Step 5: Deploy to Cloud (Optional)

**AWS (ECS/Fargate):**
1. Push image to Amazon ECR
2. Create ECS task definition
3. Deploy to Fargate

**Azure (Container Instances):**
```bash
az container create --resource-group myResourceGroup \
  --name churn-dashboard \
  --image churn-dashboard:latest \
  --ports 8501
```

**Google Cloud (Cloud Run):**
```bash
gcloud run deploy churn-dashboard \
  --image churn-dashboard:latest \
  --platform managed \
  --port 8501
```

---

## Comparison Matrix

| Feature | Local | Streamlit Cloud | Heroku | Docker |
|---------|-------|-----------------|--------|--------|
| **Setup Time** | 5 min | 10 min | 20 min | 15 min |
| **Cost (Free Tier)** | Free | Free | Free | Free* |
| **Public URL** | ❌ | ✅ | ✅ | ❌** |
| **Custom Domain** | ❌ | ✅ (Pro) | ✅ | ✅ |
| **HTTPS** | ❌ | ✅ | ✅ | Depends |
| **Auto-scaling** | ❌ | ✅ | ✅ | Depends |
| **Best For** | Development | Portfolio/Demos | Production | Enterprise |

*Docker itself is free, but cloud hosting costs apply  
**Requires additional hosting

---

## Post-Deployment Checklist

### Functionality Testing

✅ **Dashboard loads successfully**
- All pages accessible
- No error messages

✅ **Data loads correctly**
- Metrics display accurate numbers
- Charts render properly

✅ **Filters work**
- Sidebar filters update data
- Customer count updates

✅ **Interactive features functional**
- Page navigation works
- Dropdown selectors operational
- Download button works

### Performance Testing

✅ **Load time acceptable** (<5 seconds)
✅ **Filter updates fast** (<1 second)
✅ **No memory issues**
✅ **Multiple users supported** (if public)

### Security Checklist

✅ **No sensitive data exposed**
✅ **HTTPS enabled** (if public)
✅ **API keys secured** (if any)
✅ **Environment variables set** (if needed)

---

## Maintenance

### Updating Deployed Application

**Streamlit Cloud:**
- Push changes to GitHub
- Streamlit Cloud auto-deploys

**Heroku:**
```bash
git add .
git commit -m "Update dashboard"
git push heroku main
```

**Docker:**
```bash
docker build -t churn-dashboard .
docker run -p 8501:8501 churn-dashboard
```

### Monitoring

**Check Application Health:**
- Visit dashboard URL regularly
- Monitor error logs
- Test key functionality

**Streamlit Cloud Monitoring:**
- Dashboard → Analytics tab
- View usage statistics
- Check error rates

**Heroku Monitoring:**
```bash
heroku logs --tail
heroku ps
```

---

## Troubleshooting Common Issues

### Issue: "File not found" error

**Solution:**
- Use relative paths in code
- Ensure data files in repository
- Check `.gitignore` not excluding data

### Issue: Out of memory

**Solution:**
- Reduce dataset size (sampling)
- Optimize data loading (caching)
- Upgrade hosting tier

### Issue: Slow performance

**Solution:**
- Enable Streamlit caching (`@st.cache_data`)
- Optimize data queries
- Reduce visualization complexity

### Issue: Dashboard won't start

**Solution:**
- Check requirements.txt complete
- Verify Python version compatibility
- Review logs for specific errors

---

## Best Practices

### For Development
- Test locally first
- Use virtual environments
- Version control everything

### For Production
- Enable HTTPS
- Set up monitoring
- Regular backups
- Document configuration

### For Portfolio
- Use Streamlit Cloud (easiest)
- Custom domain (professional)
- Include in resume/LinkedIn
- Add screenshots to README

---

## Additional Resources

**Streamlit Documentation:**
- [docs.streamlit.io](https://docs.streamlit.io)

**Heroku Documentation:**
- [devcenter.heroku.com](https://devcenter.heroku.com)

**Docker Documentation:**
- [docs.docker.com](https://docs.docker.com)

---

## Support

For deployment issues:
- Check platform-specific documentation
- Review error logs
- Search Stack Overflow
- Contact: [your.email@example.com]

---

**Last Updated:** January 2026
