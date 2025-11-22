# server.py
from fastapi import FastAPI, HTTPException, Depends, Query, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pymongo import MongoClient
from bson import ObjectId
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime, timedelta
import bcrypt
import jwt
import os
from gridfs import GridFS
import uuid

app = FastAPI(title="YouTube Clone API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
DATABASE_NAME = "youtube_clone"
client = MongoClient(MONGO_URL)
db = client[DATABASE_NAME]
fs = GridFS(db)

# Collections
users_collection = db.users
videos_collection = db.videos
comments_collection = db.comments
playlists_collection = db.playlists
subscriptions_collection = db.subscriptions

# JWT settings
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-here")
ALGORITHM = "HS256"
security = HTTPBearer()

# Pydantic Models
class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    full_name: Optional[str] = None

class UserLogin(BaseModel):
    email: str
    password: str

class User(BaseModel):
    id: str = Field(alias="_id")
    username: str
    email: str
    full_name: Optional[str] = None
    avatar_url: Optional[str] = None
    subscribers_count: int = 0
    created_at: datetime
    
    class Config:
        allow_population_by_field_name = True

class VideoCreate(BaseModel):
    title: str
    description: Optional[str] = None
    tags: List[str] = []
    category: Optional[str] = None

class Video(BaseModel):
    id: str = Field(alias="_id")
    title: str
    description: Optional[str] = None
    thumbnail_url: Optional[str] = None
    video_url: str
    duration: Optional[int] = None  # in seconds
    views: int = 0
    likes: int = 0
    dislikes: int = 0
    tags: List[str] = []
    category: Optional[str] = None
    uploader_id: str
    uploader_name: str
    created_at: datetime
    
    class Config:
        allow_population_by_field_name = True

class CommentCreate(BaseModel):
    video_id: str
    content: str
    parent_id: Optional[str] = None  # for replies

class Comment(BaseModel):
    id: str = Field(alias="_id")
    video_id: str
    user_id: str
    username: str
    content: str
    likes: int = 0
    parent_id: Optional[str] = None
    created_at: datetime
    
    class Config:
        allow_population_by_field_name = True

class PlaylistCreate(BaseModel):
    name: str
    description: Optional[str] = None
    is_public: bool = True

class Playlist(BaseModel):
    id: str = Field(alias="_id")
    name: str
    description: Optional[str] = None
    user_id: str
    video_ids: List[str] = []
    is_public: bool = True
    created_at: datetime
    
    class Config:
        allow_population_by_field_name = True

# Helper functions
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    
    user["_id"] = str(user["_id"])
    return User(**user)

def get_optional_user(credentials: Optional[HTTPAuthorizationCredentials] = Depends(security)):
    if credentials is None:
        return None
    try:
        return get_current_user(credentials)
    except:
        return None

# Auth Routes
@app.post("/auth/register", response_model=dict)
async def register(user_data: UserCreate):
    # Check if user already exists
    if users_collection.find_one({"email": user_data.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    
    if users_collection.find_one({"username": user_data.username}):
        raise HTTPException(status_code=400, detail="Username already taken")
    
    # Hash password
    hashed_password = bcrypt.hashpw(user_data.password.encode('utf-8'), bcrypt.gensalt())
    
    # Create user
    user_doc = {
        "username": user_data.username,
        "email": user_data.email,
        "password": hashed_password,
        "full_name": user_data.full_name,
        "avatar_url": None,
        "subscribers_count": 0,
        "created_at": datetime.utcnow()
    }
    
    result = users_collection.insert_one(user_doc)
    
    # Create access token
    access_token = create_access_token(
        data={"sub": str(result.inserted_id)},
        expires_delta=timedelta(days=30)
    )
    
    return {"access_token": access_token, "token_type": "bearer", "user_id": str(result.inserted_id)}

@app.post("/auth/login", response_model=dict)
async def login(login_data: UserLogin):
    user = users_collection.find_one({"email": login_data.email})
    
    if not user or not bcrypt.checkpw(login_data.password.encode('utf-8'), user["password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(
        data={"sub": str(user["_id"])},
        expires_delta=timedelta(days=30)
    )
    
    return {"access_token": access_token, "token_type": "bearer", "user_id": str(user["_id"])}

@app.get("/auth/me", response_model=User)
async def get_current_user_info(current_user: User = Depends(get_current_user)):
    return current_user

# User Routes
@app.get("/users/{user_id}", response_model=User)
async def get_user(user_id: str):
    try:
        user = users_collection.find_one({"_id": ObjectId(user_id)})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        user["_id"] = str(user["_id"])
        # Don't return password
        user.pop("password", None)
        return User(**user)
    except:
        raise HTTPException(status_code=404, detail="User not found")

@app.get("/users/{user_id}/videos", response_model=List[Video])
async def get_user_videos(user_id: str, skip: int = 0, limit: int = 20):
    videos = list(videos_collection.find({"uploader_id": user_id})
                  .sort("created_at", -1)
                  .skip(skip)
                  .limit(limit))
    
    for video in videos:
        video["_id"] = str(video["_id"])
    
    return [Video(**video) for video in videos]

# Video Routes
@app.post("/videos", response_model=Video)
async def create_video(
    video_data: VideoCreate,
    current_user: User = Depends(get_current_user)
):
    video_doc = {
        "title": video_data.title,
        "description": video_data.description,
        "thumbnail_url": None,
        "video_url": f"/videos/{uuid.uuid4()}.mp4",  # Placeholder
        "duration": 0,
        "views": 0,
        "likes": 0,
        "dislikes": 0,
        "tags": video_data.tags,
        "category": video_data.category,
        "uploader_id": current_user.id,
        "uploader_name": current_user.username,
        "created_at": datetime.utcnow()
    }
    
    result = videos_collection.insert_one(video_doc)
    video_doc["_id"] = str(result.inserted_id)
    
    return Video(**video_doc)

@app.get("/videos", response_model=List[Video])
async def get_videos(
    skip: int = 0,
    limit: int = 20,
    search: Optional[str] = None,
    category: Optional[str] = None
):
    query = {}
    
    if search:
        query["$or"] = [
            {"title": {"$regex": search, "$options": "i"}},
            {"description": {"$regex": search, "$options": "i"}},
            {"tags": {"$in": [search]}}
        ]
    
    if category:
        query["category"] = category
    
    videos = list(videos_collection.find(query)
                  .sort("created_at", -1)
                  .skip(skip)
                  .limit(limit))
    
    for video in videos:
        video["_id"] = str(video["_id"])
    
    return [Video(**video) for video in videos]

@app.get("/videos/{video_id}", response_model=Video)
async def get_video(video_id: str):
    try:
        video = videos_collection.find_one({"_id": ObjectId(video_id)})
        if not video:
            raise HTTPException(status_code=404, detail="Video not found")
        
        # Increment view count
        videos_collection.update_one(
            {"_id": ObjectId(video_id)},
            {"$inc": {"views": 1}}
        )
        
        video["_id"] = str(video["_id"])
        video["views"] += 1  # Update local copy
        
        return Video(**video)
    except:
        raise HTTPException(status_code=404, detail="Video not found")

@app.post("/videos/{video_id}/like")
async def like_video(video_id: str, current_user: User = Depends(get_current_user)):
    try:
        videos_collection.update_one(
            {"_id": ObjectId(video_id)},
            {"$inc": {"likes": 1}}
        )
        return {"message": "Video liked"}
    except:
        raise HTTPException(status_code=404, detail="Video not found")

@app.post("/videos/{video_id}/dislike")
async def dislike_video(video_id: str, current_user: User = Depends(get_current_user)):
    try:
        videos_collection.update_one(
            {"_id": ObjectId(video_id)},
            {"$inc": {"dislikes": 1}}
        )
        return {"message": "Video disliked"}
    except:
        raise HTTPException(status_code=404, detail="Video not found")

# Comment Routes
@app.post("/comments", response_model=Comment)
async def create_comment(
    comment_data: CommentCreate,
    current_user: User = Depends(get_current_user)
):
    # Verify video exists
    video = videos_collection.find_one({"_id": ObjectId(comment_data.video_id)})
    if not video:
        raise HTTPException(status_code=404, detail="Video not found")
    
    comment_doc = {
        "video_id": comment_data.video_id,
        "user_id": current_user.id,
        "username": current_user.username,
        "content": comment_data.content,
        "likes": 0,
        "parent_id": comment_data.parent_id,
        "created_at": datetime.utcnow()
    }
    
    result = comments_collection.insert_one(comment_doc)
    comment_doc["_id"] = str(result.inserted_id)
    
    return Comment(**comment_doc)

@app.get("/videos/{video_id}/comments", response_model=List[Comment])
async def get_video_comments(video_id: str, skip: int = 0, limit: int = 50):
    comments = list(comments_collection.find({"video_id": video_id, "parent_id": None})
                    .sort("created_at", -1)
                    .skip(skip)
                    .limit(limit))
    
    for comment in comments:
        comment["_id"] = str(comment["_id"])
    
    return [Comment(**comment) for comment in comments]

# Subscription Routes
@app.post("/users/{user_id}/subscribe")
async def subscribe_to_user(user_id: str, current_user: User = Depends(get_current_user)):
    if user_id == current_user.id:
        raise HTTPException(status_code=400, detail="Cannot subscribe to yourself")
    
    # Check if user exists
    target_user = users_collection.find_one({"_id": ObjectId(user_id)})
    if not target_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Check if already subscribed
    existing = subscriptions_collection.find_one({
        "subscriber_id": current_user.id,
        "channel_id": user_id
    })
    
    if existing:
        raise HTTPException(status_code=400, detail="Already subscribed")
    
    # Create subscription
    subscriptions_collection.insert_one({
        "subscriber_id": current_user.id,
        "channel_id": user_id,
        "created_at": datetime.utcnow()
    })
    
    # Update subscriber count
    users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$inc": {"subscribers_count": 1}}
    )
    
    return {"message": "Subscribed successfully"}

@app.delete("/users/{user_id}/subscribe")
async def unsubscribe_from_user(user_id: str, current_user: User = Depends(get_current_user)):
    result = subscriptions_collection.delete_one({
        "subscriber_id": current_user.id,
        "channel_id": user_id
    })
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Subscription not found")
    
    # Update subscriber count
    users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$inc": {"subscribers_count": -1}}
    )
    
    return {"message": "Unsubscribed successfully"}

@app.get("/users/{user_id}/subscriptions", response_model=List[User])
async