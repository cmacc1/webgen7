# server.py
from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, EmailStr
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
import os
from typing import Optional, List
import uvicorn

# Configuration
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = "profile_app"

# Initialize FastAPI app
app = FastAPI(title="Profile Management API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Security
security = HTTPBearer()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# MongoDB connection
client = AsyncIOMotorClient(MONGODB_URL)
db = client[DATABASE_NAME]
users_collection = db.users

# Pydantic Models
class UserBase(BaseModel):
    email: EmailStr
    full_name: str
    username: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: str
    created_at: datetime
    is_active: bool = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[EmailStr] = None

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None

# Utility functions
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_user_by_email(email: str):
    user = await users_collection.find_one({"email": email})
    return user

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except jwt.PyJWTError:
        raise credentials_exception
    
    user = await get_user_by_email(email=token_data.email)
    if user is None:
        raise credentials_exception
    return user

# Routes
@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Profile Management App</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }
            header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 1rem; position: relative; }
            .nav-container { display: flex; justify-content: space-between; align-items: center; max-width: 1200px; margin: 0 auto; }
            .logo { color: white; font-size: 1.5rem; font-weight: bold; }
            .profile-container { position: relative; }
            .profile-btn { background: rgba(255,255,255,0.2); border: none; color: white; padding: 0.5rem 1rem; border-radius: 50px; cursor: pointer; display: flex; align-items: center; gap: 0.5rem; }
            .profile-dropdown { position: absolute; top: 100%; right: 0; background: white; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); min-width: 200px; z-index: 1000; display: none; }
            .profile-dropdown.show { display: block; }
            .dropdown-item { display: block; padding: 0.75rem 1rem; color: #333; text-decoration: none; border-bottom: 1px solid #eee; }
            .dropdown-item:hover { background: #f5f5f5; }
            .dropdown-item:last-child { border-bottom: none; }
            .main-content { max-width: 1200px; margin: 2rem auto; padding: 0 1rem; }
            .hero { text-align: center; padding: 3rem 0; }
            .hero h1 { font-size: 2.5rem; margin-bottom: 1rem; color: #333; }
            .hero p { font-size: 1.2rem; color: #666; margin-bottom: 2rem; }
            .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin: 3rem 0; }
            .feature-card { padding: 2rem; border-radius: 12px; box-shadow: 0 2px 8px rgba(0,0,0,0.1); text-align: center; }
            .feature-card h3 { margin-bottom: 1rem; color: #333; }
            .btn { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 0.75rem 2rem; border: none; border-radius: 25px; cursor: pointer; font-size: 1rem; text-decoration: none; display: inline-block; }
            .btn:hover { transform: translateY(-2px); box-shadow: 0 4px 12px rgba(0,0,0,0.2); }
            .modal { display: none; position: fixed; z-index: 1001; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); }
            .modal-content { background: white; margin: 15% auto; padding: 2rem; width: 400px; border-radius: 12px; }
            .form-group { margin-bottom: 1rem; }
            .form-group label { display: block; margin-bottom: 0.5rem; color: #333; }
            .form-group input { width: 100%; padding: 0.75rem; border: 1px solid #ddd; border-radius: 6px; }
            .close { float: right; font-size: 28px; font-weight: bold; cursor: pointer; }
        </style>
    </head>
    <body>
        <header>
            <div class="nav-container">
                <div class="logo">ProfileApp</div>
                <div class="profile-container">
                    <button class="profile-btn" onclick="toggleProfileDropdown()">
                        👤 Profile
                    </button>
                    <div class="profile-dropdown" id="profileDropdown">
                        <a href="#" class="dropdown-item" onclick="openModal('loginModal')">Sign In</a>
                        <a href="#" class="dropdown-item" onclick="openModal('signupModal')">Sign Up</a>
                        <a href="#" class="dropdown-item" onclick="openModal('profileModal')" style="display: none;" id="profileLink">My Profile</a>
                        <a href="#" class="dropdown-item" onclick="signOut()" style="display: none;" id="signOutLink">Sign Out</a>
                    </div>
                </div>
            </div>
        </header>

        <main class="main-content">
            <section class="hero">
                <h1>Welcome to ProfileApp</h1>
                <p>Manage your profile and connect with others</p>
                <a href="#" class="btn" onclick="openModal('signupModal')">Get Started</a>
            </section>

            <section class="features">
                <div class="feature-card">
                    <h3>Profile Management</h3>
                    <p>Create and customize your personal profile with ease</p>
                </div>
                <div class="feature-card">
                    <h3>Secure Authentication</h3>
                    <p>Your data is protected with industry-standard security</p>
                </div>
                <div class="feature-card">
                    <h3>Easy Navigation</h3>
                    <p>Intuitive interface designed for the best user experience</p>
                </div>
            </section>
        </main>

        <!-- Sign Up Modal -->
        <div id="signupModal" class="modal">
            <div class="modal-content">
                <span class="close" onclick="closeModal('signupModal')">&times;</span>
                <h2>Sign Up</h2>
                <form id="signupForm">
                    <div class="form-group">
                        <label>Full Name:</label>
                        <input type="text" name="full_name" required>
                    </div>
                    <div class="form-group">
                        <label>Username:</label>
                        <input type="text" name="username" required>
                    </div>
                    <div class="form-group">
                        <label>Email:</label>
                        <input type="email" name="email" required>
                    </div>
                    <div class="form-group">
                        <label>Password:</label>
                        <input type="password" name="password" required>
                    </div>
                    <button type="submit" class="btn">Sign Up</button>
                </form>
            </div>
        </div>

        <!-- Login Modal -->
        <div id="loginModal" class="modal">
            <div class="modal-content">
                <span class="close" onclick="closeModal('loginModal')">&times;</span>
                <h2>Sign In</h2>
                <form id="loginForm">
                    <div class="form-group">
                        <label>Email:</label>
                        <input type="email" name="email" required>
                    </div>
                    <div class="form-group">
                        <label>Password:</label>
                        <input type="password" name="password" required>
                    </div>
                    <button type="submit" class="btn">Sign In</button>
                </form>
            </div>
        </div>

        <!-- Profile Modal -->
        <div id="profileModal" class="modal">
            <div class="modal-content">
                <span class="close" onclick="closeModal('profileModal')">&times;</span>
                <h2>My Profile</h2>
                <form id="profileForm">
                    <div class="form-group">
                        <label>Full Name:</label>
                        <input type="text" name="full_name" id="profileFullName">
                    </div>
                    <div class="form-group">
                        <label>Username:</label>
                        <input type="text" name="username" id="profileUsername">
                    </div>
                    <div class="form-group">
                        <label>Email:</label>
                        <input type="email" name="email" id="profileEmail">
                    </div>
                    <button type="submit" class="btn">Update Profile</button>
                </form>
            </div>
        </div>

        <script>
            let currentUser = null;
            let authToken = localStorage.getItem('authToken');

            function toggleProfileDropdown() {
                document.getElementById('profileDropdown').classList.toggle('show');
            }

            function openModal(modalId) {
                document.getElementById(modalId).style.display = 'block';
                document.getElementById('profileDropdown').classList.remove('show');
            }

            function closeModal(modalId) {
                document.getElementById(modalId).style.display = 'none';
            }

            function updateAuthUI(user) {
                if (user) {
                    document.getElementById('profileLink').style.display = 'block';
                    document.getElementById('signOutLink').style.display = 'block';
                    document.querySelector('.profile-btn').innerHTML = `👤 ${user.username}`;
                } else {
                    document.getElementById('profileLink').style.display = 'none';
                    document.getElementById('signOutLink').style.display = 'none';
                    document.querySelector('.profile-btn').innerHTML = '👤 Profile';
                }
            }

            function signOut() {
                localStorage.removeItem('authToken');
                currentUser = null;
                authToken = null;
                updateAuthUI(null);
                document.getElementById('profileDropdown').classList.remove('show');
            }

            // Sign up form handler
            document.getElementById('signupForm').addEventListener('submit', async (e) => {
                e.preventDefault();
                const formData = new FormData(e.target);
                const userData = Object.fromEntries(formData);
                
                try {
                    const response = await fetch('/auth/signup', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(userData)
                    });
                    
                    if (response.ok) {
                        alert('Account created successfully! Please sign in.');
                        closeModal('signupModal');
                        openModal('loginModal');
                    } else {
                        const error = await response.json();
                        alert(error.detail);
                    }
                } catch (error) {
                    alert('An error occurred. Please try again.');
                }
            });

            // Login form handler
            document.getElementById('loginForm').addEventListener('submit', async (e) => {
                e.preventDefault();
                const formData = new FormData(e.target);
                const loginData = Object.fromEntries(formData);
                
                try {
                    const response = await fetch('/auth/login', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify(loginData)
                    });
                    
                    if (response.ok) {
                        const tokenData = await response.json();
                        authToken = tokenData.access_token;
                        localStorage.setItem('authToken', authToken);
                        
                        // Get user profile
                        const profileResponse = await fetch('/users/me', {
                            headers: { 'Authorization': `Bearer ${authToken}` }
                        });
                        
                        if (profileResponse.ok) {
                            currentUser = await profileResponse.json();
                            updateAuthUI(currentUser);
                            closeModal('loginModal');
                        }
                    } else {
                        const error =