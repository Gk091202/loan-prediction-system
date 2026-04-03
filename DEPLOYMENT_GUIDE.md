# Vercel Deployment Guide for Loan Prediction System

## 📝 Prerequisites

1. **GitHub Account** - Create one at https://github.com
2. **Vercel Account** - Create one at https://vercel.com (free)
3. **Git** - Install from https://git-scm.com

---

## 🚀 Step-by-Step Deployment

### STEP 1: Create GitHub Repository

Follow these steps to create and set up your GitHub repo:

1. Go to https://github.com/new
2. **Repository name**: `loan-prediction-system`
3. **Description**: "A beginner-friendly Loan Prediction Web App using Flask and Machine Learning"
4. Select: **Public** (so others can see it)
5. ✓ Check "Add a README file"
6. Click **Create repository**

You'll see your repo URL like: `https://github.com/YOUR-USERNAME/loan-prediction-system`

---

### STEP 2: Initialize Git Locally

Open terminal in your project folder:

```bash
cd /Users/gauravkoli/Movies/loan-prediction-system

# Initialize git
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Loan Prediction System with Flask and ML"

# Add remote repository (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/loan-prediction-system.git

# Rename branch to main (if needed)
git branch -M main

# Push to GitHub
git push -u origin main
```

When prompted, enter:

- **Username**: Your GitHub username
- **Password**: Your GitHub personal access token (create at https://github.com/settings/tokens)

---

### STEP 3: Configure Vercel Deployment

1. Go to https://vercel.com/new
2. **Import Git Repository**
3. Search for and select: `loan-prediction-system`
4. Click **Import**

#### Environment Variables (Optional but Recommended)

In the Vercel dashboard:

- Click your project name
- Go to **Settings** → **Environment Variables**
- Add: `FLASK_ENV = production`
- Click **Save**

---

### STEP 4: Deploy

Vercel will automatically start building:

1. Wait for build to complete (usually 1-2 minutes)
2. You'll see: **"Congratulations! Your project is deployed"**
3. Your live URL: `https://your-project-name.vercel.app`

✅ Your app is now live on the internet!

---

## 🔄 Update & Redeploy

Every time you push to GitHub, Vercel automatically redeploys:

```bash
# Make changes to files
git add .
git commit -m "Your commit message"
git push origin main
```

Vercel will automatically build and deploy! (No manual steps needed)

---

## 📊 Project Structure for Vercel

```
loan-prediction-system/
├── app.py                    # Main Flask app
├── train_model.py            # Model training script
├── requirements.txt          # Python dependencies ✓ NEW
├── vercel.json              # Vercel configuration ✓ NEW
├── .gitignore               # Git ignore file ✓ NEW
├── loan_data.csv            # Training data
├── model.pkl                # Trained model
├── encoders.pkl             # Encoders
├── le_target.pkl            # Target encoder
├── templates/
│   └── index.html           # HTML form
├── static/
│   └── style.css            # CSS styling
└── README.md                # Documentation
```

---

## 🐛 Troubleshooting Vercel Deployment

### Error: "No module named 'flask'"

- Make sure `requirements.txt` is in project root
- Check that all dependencies are listed

### Error: "model.pkl not found"

**Solution**: The model files need to be committed to GitHub too. Run locally:

```bash
python train_model.py
git add model.pkl encoders.pkl le_target.pkl
git commit -m "Add trained model files"
git push
```

### Slow loading or timeout

- First deployment may take longer
- Check Vercel build logs for errors
- Vercel dashboard → Your project → Deployments → View Build Logs

### Form not working

- Check browser console (F12)
- Check Vercel logs: Vercel dashboard → Logs
- Verify environment is set to production

---

## 📱 Share Your Live Project

Once deployed, share this link with anyone:

```
https://your-project-name.vercel.app
```

They can use it without needing Python, Flask, or anything installed!

---

## 💾 Useful Commands Reference

```bash
# Clone your project on another computer
git clone https://github.com/YOUR-USERNAME/loan-prediction-system.git

# Update after making changes
git status                    # See what changed
git add .                     # Stage all changes
git commit -m "message"       # Commit changes
git push origin main          # Push to GitHub (auto-redeploys on Vercel!)

# Remove sensitive files (if accidentally committed)
git rm --cached model.pkl
git commit -m "Remove model file"
git push
```

---

## 📝 Steps Summary

| Step | What to Do                                 |
| ---- | ------------------------------------------ |
| 1    | Create GitHub repo at github.com/new       |
| 2    | Initialize Git: `git init`                 |
| 3    | Commit and push: `git push -u origin main` |
| 4    | Connect to Vercel at vercel.com/new        |
| 5    | Vercel auto-deploys! 🎉                    |
| 6    | Get live URL and share!                    |

---

## 🎓 For Your College Project

**Show your professor:**

- ✅ GitHub repository (code visible to all)
- ✅ Live Vercel deployment (working app online)
- ✅ All code with comments
- ✅ Working prediction system

This makes an impressive portfolio project! 🚀

---

## ❓ Need Help?

- **GitHub Issues**: https://github.com/YOUR-USERNAME/loan-prediction-system/issues
- **Vercel Docs**: https://vercel.com/docs
- **Flask Docs**: https://flask.palletsprojects.com

---

**Ready to deploy? Follow Step 1 above!** 🚀
