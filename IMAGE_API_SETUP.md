# Image API Setup Guide - FREE High-Quality Images

This guide will help you set up **3 FREE image APIs** for the highest quality website generation:

## 🌟 Priority Order (Best Quality First)

1. **Unsplash** - Highest quality professional photos
2. **Pixabay** - Great quality, unlimited requests
3. **Pexels** - Already configured, good quality

---

## 1️⃣ Unsplash API (HIGHEST QUALITY) ⭐

### Why Unsplash?
- **Professional-grade photography**
- 4+ million high-resolution photos
- Best for hero images
- **100% FREE** (as of 2025)

### Setup Steps:

1. **Go to Unsplash Developers**
   - Visit: https://unsplash.com/developers

2. **Sign Up / Log In**
   - Create free Unsplash account
   - Or log in if you have one

3. **Register Your Application**
   - Click "Register your application"
   - Fill in:
     - **Application name**: Code Weaver
     - **Description**: AI-powered website generator
     - **Website URL**: http://localhost:3000 (or your domain)
   - Accept API guidelines

4. **Get Your Access Key**
   - After registration, you'll see your **Access Key**
   - Copy it (starts with something like `abc123xyz...`)

5. **Add to .env File**
   ```bash
   UNSPLASH_ACCESS_KEY=your_access_key_here
   ```

### Rate Limit:
- **50 requests/hour** (free tier)
- More than enough for website generation

### Documentation:
- https://unsplash.com/documentation

---

## 2️⃣ Pixabay API (UNLIMITED FREE) 🎨

### Why Pixabay?
- **Unlimited free requests** (no hourly limit!)
- 4.3+ million images
- No attribution required
- Great variety

### Setup Steps:

1. **Go to Pixabay**
   - Visit: https://pixabay.com/api/docs/

2. **Sign Up / Log In**
   - Create free account
   - Or log in

3. **Get Your API Key**
   - On the API docs page, you'll see your **API Key**
   - It's shown right on the page after login
   - Copy it (format: `12345678-abc123def456...`)

4. **Add to .env File**
   ```bash
   PIXABAY_API_KEY=your_api_key_here
   ```

### Rate Limit:
- **UNLIMITED** free requests
- Best for bulk image needs

### Documentation:
- https://pixabay.com/api/docs/

---

## 3️⃣ Pexels API (ALREADY CONFIGURED) ✅

### Already Set Up!
- Your Pexels API key is already in the .env file
- Works as fallback if other APIs are not configured

### Rate Limit:
- **200 requests/hour**

---

## 🚀 Quick Setup (Copy-Paste Ready)

### Step 1: Get All Three API Keys

1. **Unsplash**: https://unsplash.com/developers → Register app → Copy Access Key
2. **Pixabay**: https://pixabay.com/api/docs/ → Sign up → Copy API Key
3. **Pexels**: Already configured ✅

### Step 2: Update .env File

Open `/app/backend/.env` and add your keys:

```bash
# Image API Keys (All FREE)
PEXELS_API_KEY=nz7oJbq5rzpacGTjQrbs4SOvDbTPHX9G8kgGtHsMNOljerMbmT8a9RRD
UNSPLASH_ACCESS_KEY=paste_your_unsplash_key_here
PIXABAY_API_KEY=paste_your_pixabay_key_here
```

### Step 3: Restart Backend

```bash
sudo supervisorctl restart backend
```

### Step 4: Test!

Generate a website and check logs for:
```
✅ Hero image from UNSPLASH: https://...
   Photographer: John Doe
```

---

## 📊 How It Works

The system tries sources in this order:

1. **Unsplash** (best quality) → If found, use it
2. **Pixabay** (unlimited) → If Unsplash fails, try this
3. **Pexels** (good) → Final fallback

### Example Flow:
```
User prompt: "Modern coffee shop"
  ↓
Search Unsplash for "modern coffee shop"
  ↓
✅ Found! Use Unsplash image (highest quality)
  ↓
Display in hero section
```

### If Unsplash is down:
```
User prompt: "Modern coffee shop"
  ↓
Search Unsplash → Failed
  ↓
Search Pixabay for "modern coffee shop"
  ↓
✅ Found! Use Pixabay image
```

---

## ⚡ Benefits of Multi-Source System

### Quality
- Best images from best sources
- Professional-grade photography
- High resolution (1080p+)

### Reliability
- If one API is down, others work
- Never fail to get images
- Automatic fallback

### Variety
- Different sources = different styles
- More diverse image pool
- Better matches for specific queries

### Free
- All three APIs are 100% free
- No hidden costs
- No credit card required

---

## 🔍 What You Need to Provide

Please provide these API keys:

1. **UNSPLASH_ACCESS_KEY** - Get from https://unsplash.com/developers
2. **PIXABAY_API_KEY** - Get from https://pixabay.com/api/docs/

### Time Required: 5 minutes total
- Unsplash: 2 minutes
- Pixabay: 1 minute
- Update .env: 30 seconds
- Restart: 30 seconds

---

## ❓ FAQ

**Q: Do I need all three?**
A: No, but more is better! System works with just one, but having all three gives best results.

**Q: Are they really free?**
A: Yes! All three are 100% free in 2025. Unsplash made their API free, Pixabay has always been unlimited free.

**Q: Do I need a credit card?**
A: No! Just email signup.

**Q: What if I don't add the keys?**
A: System will work with just Pexels (already configured), but you'll get even better images with all three.

**Q: Rate limits?**
A: 
- Unsplash: 50/hour (plenty for website generation)
- Pixabay: Unlimited
- Pexels: 200/hour

**Q: Attribution required?**
A: System automatically adds proper attribution in generated websites.

---

## 🎯 Expected Results

**Without additional APIs** (Pexels only):
- Good quality images
- Works fine

**With Unsplash + Pixabay** (all three):
- ⭐ **Highest quality images**
- Better variety
- More reliable (automatic fallback)
- Professional photography

---

## 📝 Summary

1. Get Unsplash key: https://unsplash.com/developers
2. Get Pixabay key: https://pixabay.com/api/docs/
3. Add both to `/app/backend/.env`
4. Restart backend
5. Enjoy highest quality images! 🎉
