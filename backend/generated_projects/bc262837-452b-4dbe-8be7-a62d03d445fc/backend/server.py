# server.py
from fastapi import FastAPI, HTTPException, Depends, status, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List, Dict, Any
from datetime import datetime, timedelta
import motor.motor_asyncio
import bcrypt
import jwt
import uuid
import json
import asyncio
from bson import ObjectId
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="ConversAI API",
    description="Modern Conversational AI SaaS Platform",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB Configuration
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "conversai_db")
JWT_SECRET = os.getenv("JWT_SECRET", "your-secret-key-change-in-production")

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)
database = client[DATABASE_NAME]

# Collections
users_collection = database.users
conversations_collection = database.conversations
subscriptions_collection = database.subscriptions
api_keys_collection = database.api_keys

# Security
security = HTTPBearer()

# Pydantic Models
class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(..., min_length=8)
    full_name: str
    company: Optional[str] = None

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class User(BaseModel):
    id: str = Field(alias="_id")
    email: str
    full_name: str
    company: Optional[str] = None
    subscription_tier: str = "free"
    api_calls_count: int = 0
    created_at: datetime
    is_active: bool = True

    class Config:
        allow_population_by_field_name = True

class ConversationCreate(BaseModel):
    title: Optional[str] = None
    model: str = "gpt-3.5-turbo"
    system_prompt: Optional[str] = None

class Message(BaseModel):
    role: str = Field(..., regex="^(user|assistant|system)$")
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class Conversation(BaseModel):
    id: str = Field(alias="_id")
    user_id: str
    title: str
    model: str
    system_prompt: Optional[str] = None
    messages: List[Message] = []
    created_at: datetime
    updated_at: datetime

    class Config:
        allow_population_by_field_name = True

class ChatMessage(BaseModel):
    message: str
    conversation_id: Optional[str] = None
    model: Optional[str] = "gpt-3.5-turbo"

class APIKeyCreate(BaseModel):
    name: str
    permissions: List[str] = ["chat", "conversations"]

class APIKey(BaseModel):
    id: str = Field(alias="_id")
    user_id: str
    name: str
    key: str
    permissions: List[str]
    created_at: datetime
    last_used: Optional[datetime] = None
    is_active: bool = True

    class Config:
        allow_population_by_field_name = True

class SubscriptionUpdate(BaseModel):
    tier: str = Field(..., regex="^(free|pro|enterprise)$")

class UsageStats(BaseModel):
    api_calls_today: int
    api_calls_month: int
    conversations_count: int
    subscription_tier: str
    api_limit: int

# Utility Functions
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=24)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET, algorithm="HS256")
    return encoded_jwt

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, JWT_SECRET, algorithms=["HS256"])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    
    user = await users_collection.find_one({"_id": ObjectId(user_id)})
    if user is None:
        raise HTTPException(status_code=401, detail="User not found")
    
    return User(**{**user, "_id": str(user["_id"])})

def generate_api_key():
    return f"sk-{uuid.uuid4().hex}"

# Mock AI Response Function (Replace with actual AI integration)
async def generate_ai_response(message: str, conversation_history: List[Message] = []):
    # Simulate AI processing time
    await asyncio.sleep(1)
    
    # Mock response - Replace with actual AI API call
    responses = [
        "That's an interesting question! Let me think about that...",
        "Based on what you've shared, I'd recommend considering...",
        "I understand your concern. Here's what I suggest...",
        "Great point! From my perspective...",
        "Let me help you with that. The key factors to consider are..."
    ]
    
    import random
    return random.choice(responses) + f" (responding to: '{message[:50]}...')"

# Authentication Routes
@app.post("/api/auth/register", response_model=dict)
async def register(user: UserCreate):
    # Check if user already exists
    existing_user = await users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new user
    hashed_password = hash_password(user.password)
    new_user = {
        "email": user.email,
        "password": hashed_password,
        "full_name": user.full_name,
        "company": user.company,
        "subscription_tier": "free",
        "api_calls_count": 0,
        "created_at": datetime.utcnow(),
        "is_active": True
    }
    
    result = await users_collection.insert_one(new_user)
    access_token = create_access_token(data={"sub": str(result.inserted_id)})
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": User(**{**new_user, "_id": str(result.inserted_id)})
    }

@app.post("/api/auth/login", response_model=dict)
async def login(user: UserLogin):
    db_user = await users_collection.find_one({"email": user.email})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=401, detail="Incorrect email or password")
    
    if not db_user["is_active"]:
        raise HTTPException(status_code=401, detail="Account is deactivated")
    
    access_token = create_access_token(data={"sub": str(db_user["_id"])})
    
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user": User(**{**db_user, "_id": str(db_user["_id"])})
    }

# User Routes
@app.get("/api/user/profile", response_model=User)
async def get_profile(current_user: User = Depends(get_current_user)):
    return current_user

@app.get("/api/user/usage", response_model=UsageStats)
async def get_usage_stats(current_user: User = Depends(get_current_user)):
    # Get today's API calls
    today = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0)
    
    # Get this month's API calls
    month_start = today.replace(day=1)
    
    # Count conversations
    conversations_count = await conversations_collection.count_documents({"user_id": current_user.id})
    
    # API limits based on subscription
    api_limits = {
        "free": 100,
        "pro": 10000,
        "enterprise": 100000
    }
    
    return UsageStats(
        api_calls_today=current_user.api_calls_count,  # Simplified for demo
        api_calls_month=current_user.api_calls_count,
        conversations_count=conversations_count,
        subscription_tier=current_user.subscription_tier,
        api_limit=api_limits.get(current_user.subscription_tier, 100)
    )

# Conversation Routes
@app.post("/api/conversations", response_model=Conversation)
async def create_conversation(
    conversation: ConversationCreate,
    current_user: User = Depends(get_current_user)
):
    new_conversation = {
        "user_id": current_user.id,
        "title": conversation.title or f"Conversation {datetime.utcnow().strftime('%Y-%m-%d %H:%M')}",
        "model": conversation.model,
        "system_prompt": conversation.system_prompt,
        "messages": [],
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }
    
    result = await conversations_collection.insert_one(new_conversation)
    return Conversation(**{**new_conversation, "_id": str(result.inserted_id)})

@app.get("/api/conversations", response_model=List[Conversation])
async def get_conversations(
    limit: int = 20,
    skip: int = 0,
    current_user: User = Depends(get_current_user)
):
    cursor = conversations_collection.find(
        {"user_id": current_user.id}
    ).sort("updated_at", -1).skip(skip).limit(limit)
    
    conversations = []
    async for doc in cursor:
        conversations.append(Conversation(**{**doc, "_id": str(doc["_id"])}))
    
    return conversations

@app.get("/api/conversations/{conversation_id}", response_model=Conversation)
async def get_conversation(
    conversation_id: str,
    current_user: User = Depends(get_current_user)
):
    conversation = await conversations_collection.find_one({
        "_id": ObjectId(conversation_id),
        "user_id": current_user.id
    })
    
    if not conversation:
        raise HTTPException(status_code=404, detail="Conversation not found")
    
    return Conversation(**{**conversation, "_id": str(conversation["_id"])})

@app.delete("/api/conversations/{conversation_id}")
async def delete_conversation(
    conversation_id: str,
    current_user: User = Depends(get_current_user)
):
    result = await conversations_collection.delete_one({
        "_id": ObjectId(conversation_id),
        "user_id": current_user.id
    })
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Conversation not found")
    
    return {"message": "Conversation deleted successfully"}

# Chat Routes
@app.post("/api/chat")
async def chat(
    chat_message: ChatMessage,
    current_user: User = Depends(get_current_user)
):
    # Check API limits
    api_limits = {"free": 100, "pro": 10000, "enterprise": 100000}
    if current_user.api_calls_count >= api_limits.get(current_user.subscription_tier, 100):
        raise HTTPException(status_code=429, detail="API limit exceeded")
    
    # Get or create conversation
    conversation = None
    if chat_message.conversation_id:
        conversation = await conversations_collection.find_one({
            "_id": ObjectId(chat_message.conversation_id),
            "user_id": current_user.id
        })
        if not conversation:
            raise HTTPException(status_code=404, detail="Conversation not found")
    else:
        # Create new conversation
        new_conversation = {
            "user_id": current_user.id,
            "title": f"Chat {datetime.utcnow().strftime('%Y-%m-%d %H:%M')}",
            "model": chat_message.model,
            "system_prompt": None,
            "messages": [],
            "created_at": datetime.utcnow(),
            "updated_at": datetime.utcnow()
        }
        result = await conversations_collection.insert_one(new_conversation)
        conversation = {**new_conversation, "_id": result.inserted_id}
    
    # Add user message
    user_message = Message(role="user", content=chat_message.message)
    
    # Generate AI response
    ai_response = await generate_ai_response(
        chat_message.message, 
        conversation.get("messages", [])
    )
    ai_message = Message(role="assistant", content=ai_response)
    
    # Update conversation
    await conversations_collection.update_one(
        {"_id": conversation["_id"]},
        {
            "$push": {
                "messages": {
                    "$each": [user_message.dict(), ai_message.dict()]
                }
            },
            "$set": {"updated_at": datetime.utcnow()}
        }
    )
    
    # Update user API call count
    await users_collection.update_one(
        {"_id": ObjectId(current_user.id)},
        {"$inc": {"api_calls_count": 1}}
    )
    
    return {
        "conversation_id": str(conversation["_id"]),
        "response": ai_response,
        "message_id": str(uuid.uuid4())
    }

@app.post("/api/chat/stream")
async def chat_stream(
    chat_message: ChatMessage,
    current_user: User = Depends(get_current_user)
):
    async def generate_stream():
        # Mock streaming response
        response = await generate_ai_response(chat_message.message)
        words = response.split()
        
        for i, word in enumerate(words):
            chunk = {
                "delta": {"content": word + " "},
                "finish_reason": None if i < len(words) - 1 else "stop"
            }
            yield f"data: {json.dumps(chunk)}\n\n"
            await asyncio.sleep(0.1)
        
        yield "data: [DONE]\n\n"
    
    return StreamingResponse(
        generate_stream(),
        media_type="text/plain",
        headers={"Cache-Control": "no-cache", "Connection": "keep-alive"}
    )

# API Keys Routes
@app.post("/api/api-keys", response_model=APIKey)
async def create_api_key