# 🚀 FastAPI Learning Project

A comprehensive FastAPI learning repository demonstrating modern Python web development, RESTful API design, data validation with Pydantic, and machine learning model deployment.

---

## 📚 Table of Contents

- [Overview](#overview)
- [Projects Included](#projects-included)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [Learning Outcomes](#learning-outcomes)
- [Getting Started](#getting-started)
- [Project Details](#project-details)
  - [1. Patient Management API](#1-patient-management-api)
  - [2. Insurance Premium Prediction](#2-insurance-premium-prediction)
  - [3. Pydantic Validation Examples](#3-pydantic-validation-examples)
- [API Documentation](#api-documentation)
- [Application Flow](#application-flow)
- [Best Practices Demonstrated](#best-practices-demonstrated)
- [Future Enhancements](#future-enhancements)

---

## 🎯 Overview

This repository serves as a **hands-on learning resource** for building modern web APIs using **FastAPI**. It showcases three main projects that progressively demonstrate core concepts from basic CRUD operations to ML model deployment with advanced validation patterns.

### What You'll Learn:
- ✅ Building RESTful APIs with FastAPI
- ✅ Data validation and serialization using Pydantic
- ✅ CRUD operations with JSON file storage
- ✅ Machine Learning model deployment
- ✅ Frontend-Backend integration (Streamlit + FastAPI)
- ✅ Docker containerization
- ✅ Advanced Pydantic features (validators, computed fields, nested models)

---

## 📦 Projects Included

### 1. **Patient Management System** (`1.py`)
A complete CRUD API for managing patient records with BMI calculation and health verdict generation.

### 2. **Insurance Premium Predictor** (`project/`)
A full-stack ML application predicting insurance premium categories based on user demographics and lifestyle.

### 3. **Pydantic Validation Library** (`pydantic/`)
A collection of examples demonstrating advanced Pydantic validation techniques.

---

## 📁 Project Structure

```
FastAPI/
│
├── 1.py                          # Patient Management API (CRUD operations)
├── 1.ipynb                       # Jupyter notebook with API learning notes
├── patients.json                 # Patient data storage
├── patients.py                   # Patient data (alternative format)
│
├── project/                      # Insurance Premium Prediction Project
│   ├── app.py                   # FastAPI backend with ML model
│   ├── frontend.py              # Streamlit frontend UI
│   ├── model.pkl                # Pre-trained ML model (scikit-learn)
│   ├── model.ipynb              # Model training notebook
│   ├── insurance.csv            # Training dataset
│   ├── requirements.txt         # Python dependencies
│   ├── Dockerfile               # Container configuration
│   ├── .dockerignore            # Docker build exclusions
│   └── PROJECT_REPORT.md        # Detailed project documentation
│
├── pydantic/                     # Pydantic Learning Examples
│   ├── computed_field.py        # Dynamic field computation
│   ├── field_validator.py       # Custom field validation
│   ├── model_validator.py       # Model-level validation
│   ├── nested.py                # Nested model structures
│   ├── pydantic_check.py        # Additional validation patterns
│   └── .md                      # Pydantic documentation
│
└── myvenv/                       # Python virtual environment
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| **Python 3.13** | Core programming language |
| **FastAPI** | High-performance web framework |
| **Pydantic** | Data validation and serialization |
| **Uvicorn** | ASGI server for running FastAPI |
| **Streamlit** | Frontend UI framework |
| **Pandas** | Data manipulation and preprocessing |
| **Scikit-learn** | Machine learning model training |
| **Docker** | Application containerization |
| **Jupyter** | Interactive notebooks for exploration |

---

## 🎓 Learning Outcomes

Through this project, you will gain expertise in:

### 1. **FastAPI Fundamentals**
- Creating RESTful endpoints (`GET`, `POST`, `PUT`, `DELETE`)
- Path and query parameters with validation
- Request/response handling
- HTTP status codes and error handling
- Automatic API documentation (Swagger UI)

### 2. **Pydantic Mastery**
- **BaseModel**: Creating data models with type hints
- **Field Validation**: Custom validators and constraints
- **Computed Fields**: Dynamic field generation (`@computed_field`)
- **Model Validators**: Cross-field validation logic
- **Nested Models**: Complex data structures
- **Type Safety**: Using `Annotated`, `Literal`, `Optional`

### 3. **Machine Learning Deployment**
- Loading serialized ML models (`pickle`)
- Feature engineering in production
- Real-time inference via API
- Confidence scores and probability distributions

### 4. **Full-Stack Development**
- Frontend-Backend separation
- API consumption from Streamlit
- Error handling across layers
- Environment configuration

### 5. **DevOps & Containerization**
- Writing Dockerfiles
- Managing dependencies
- Port mapping and networking
- Production-ready deployments

---

## 🚀 Getting Started

### Prerequisites
```bash
# Python 3.11+ installed
python --version

# Virtual environment (recommended)
python -m venv myvenv
source myvenv/bin/activate  # On Windows: myvenv\Scripts\activate
```

### Installation

#### **Option 1: Local Setup**
```bash
# Clone or navigate to the project directory
cd FastAPI

# Install dependencies
pip install fastapi uvicorn pydantic pandas scikit-learn streamlit

# For the insurance project specifically:
cd project
pip install -r requirements.txt
```

#### **Option 2: Docker Setup** (Insurance Project)
```bash
cd project

# Build the Docker image
docker build -t insurance-premium-predictor .

# Run the container
docker run -p 8000:8000 insurance-premium-predictor
```

---

## 📖 Project Details

---

## 1. Patient Management API

**File:** `1.py`  
**Purpose:** Learn CRUD operations, data validation, and JSON file storage

### Features:
- ✅ **Create** patients with validated data
- ✅ **Read** all patients or specific patient by ID
- ✅ **Update** patient information (partial updates supported)
- ✅ **Delete** patients from the system
- ✅ **Sort** patients by height, weight, or BMI
- ✅ **Auto-calculate** BMI and health verdict

### Key Endpoints:

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Welcome message |
| `GET` | `/view` | View all patients |
| `GET` | `/patient/{patient_id}` | Get specific patient details |
| `GET` | `/sort?sort_by=bmi&order=desc` | Sort patients by field |
| `POST` | `/create` | Create a new patient |
| `PUT` | `/edit/{patient_id}` | Update patient information |
| `DELETE` | `/delete/{patient_id}` | Delete a patient |

### Data Model:
```python
class Patient(BaseModel):
    id: str                    # Patient ID (e.g., "P001")
    name: str                  # Patient name
    city: str                  # City of residence
    age: int                   # Age (1-119)
    gender: Literal['male', 'female', 'others']
    height: float              # Height in meters
    weight: float              # Weight in kilograms
    
    # Auto-computed fields
    bmi: float                 # Body Mass Index
    verdict: str               # Health verdict based on BMI
```

### Running the API:
```bash
# Start the server
uvicorn 1:app --reload

# Access the API
# - Interactive docs: http://127.0.0.1:8000/docs
# - Alternative docs: http://127.0.0.1:8000/redoc
```

### Application Flow:
```
User Request → FastAPI Endpoint → Pydantic Validation → 
Load JSON Data → Business Logic → Computed Fields → 
Save to JSON → JSON Response
```

---

## 2. Insurance Premium Prediction

**Location:** `project/`  
**Purpose:** Deploy a machine learning model as a production-ready API

### Architecture:

```
┌─────────────────┐      HTTP POST       ┌──────────────────┐
│                 │  ───────────────────> │                  │
│  Streamlit UI   │                       │  FastAPI Backend │
│  (frontend.py)  │  <─────────────────── │    (app.py)      │
│                 │      JSON Response    │                  │
└─────────────────┘                       └──────────────────┘
                                                    │
                                                    │ Load Model
                                                    ▼
                                          ┌──────────────────┐
                                          │  ML Model (PKL)  │
                                          │  Scikit-learn    │
                                          └──────────────────┘
```

### Features:
- 🎯 **ML Model Inference**: Predicts insurance premium category
- 📊 **Confidence Scores**: Returns prediction probabilities
- 🔍 **Feature Engineering**: Auto-calculates BMI, lifestyle risk, age group, city tier
- ✅ **Data Validation**: Strict input validation using Pydantic
- 🌐 **Interactive UI**: User-friendly Streamlit interface
- 🐳 **Containerized**: Ready for Docker deployment

### Input Features:
```python
{
    "age": 30,              # Age of user (1-119)
    "weight": 70.0,         # Weight in kg
    "height": 1.75,         # Height in meters
    "income_lpa": 12.0,     # Annual income (Lakhs per annum)
    "smoker": false,        # Smoking status
    "city": "Mumbai",       # City of residence
    "occupation": "private_job"  # Occupation type
}
```

### Auto-Generated Features:
| Feature | Calculation | Purpose |
|---------|-------------|---------|
| **BMI** | weight / (height²) | Health indicator |
| **Lifestyle Risk** | Based on BMI + smoking | Risk categorization (low/medium/high) |
| **Age Group** | Age-based categorization | young/adult/middle_aged/senior |
| **City Tier** | City classification | Tier 1/2/3 based on city list |

### Prediction Output:
```json
{
    "predicted_category": "Medium",
    "confidence": 0.7543,
    "class_probabilities": {
        "Low": 0.1234,
        "Medium": 0.7543,
        "High": 0.1223
    }
}
```

### Running the Application:

#### **Backend (FastAPI):**
```bash
cd project
uvicorn app:app --reload --host 0.0.0.0 --port 8000

# API will be available at: http://localhost:8000
# Documentation: http://localhost:8000/docs
```

#### **Frontend (Streamlit):**
```bash
cd project
streamlit run frontend.py

# UI will open at: http://localhost:8501
```

#### **Docker:**
```bash
cd project
docker build -t insurance-app .
docker run -p 8000:8000 insurance-app
```

### Application Flow:
```
User Input (Streamlit) → POST Request → FastAPI Endpoint → 
Pydantic Validation → Feature Engineering → 
ML Model Prediction → Probability Calculation → 
JSON Response → Streamlit Display
```

---

## 3. Pydantic Validation Examples

**Location:** `pydantic/`  
**Purpose:** Learn advanced Pydantic patterns for robust data validation

### Examples Included:

#### **1. Computed Fields** (`computed_field.py`)
Automatically calculate derived fields from existing data.

```python
@computed_field
@property
def bmi(self) -> float:
    return round(self.weight / (self.height ** 2), 2)
```

**Use Case:** BMI calculation, full name generation, age from birthdate

---

#### **2. Field Validators** (`field_validator.py`)
Custom validation logic for individual fields.

```python
@field_validator('email')
@classmethod
def email_validator(cls, value):
    allowed_domains = ["company.com", "org.com"]
    domain = value.split("@")[-1]
    if domain not in allowed_domains:
        raise ValueError("Not a valid domain")
    return value
```

**Use Case:** Email domain restrictions, data normalization, custom constraints

---

#### **3. Model Validators** (`model_validator.py`)
Cross-field validation requiring access to multiple fields.

```python
@model_validator(mode='after')
def validate_emergency_contact(cls, model):
    if model.age > 60 and 'emergency' not in model.contact_details:
        raise ValueError('Patients older than 60 must have emergency contact')
    return model
```

**Use Case:** Business rules, conditional validation, data consistency checks

---

#### **4. Nested Models** (`nested.py`)
Organize complex data structures with nested Pydantic models.

```python
class Address(BaseModel):
    city: str
    state: str
    pin: str

class Patient(BaseModel):
    name: str
    age: int
    address: Address  # Nested model
```

**Use Case:** Complex JSON structures, API request/response modeling

---

### Running Pydantic Examples:
```bash
cd pydantic

# Run individual examples
python computed_field.py
python field_validator.py
python model_validator.py
python nested.py
```

---

## 📚 API Documentation

FastAPI automatically generates interactive API documentation:

### **Swagger UI** (Interactive):
```
http://localhost:8000/docs
```
- Test endpoints directly from the browser
- View request/response schemas
- See validation rules

### **ReDoc** (Alternative):
```
http://localhost:8000/redoc
```
- Cleaner, more readable format
- Better for documentation review

---

## 🔄 Application Flow

### **Patient Management API Flow:**
```
┌────────────┐
│   Client   │
└─────┬──────┘
      │
      ▼
┌─────────────────────┐
│  HTTP Request       │
│  (GET/POST/PUT/DEL) │
└─────┬───────────────┘
      │
      ▼
┌─────────────────────┐
│  FastAPI Endpoint   │
│  (Route Handler)    │
└─────┬───────────────┘
      │
      ▼
┌─────────────────────┐
│ Pydantic Validation │
│ - Type checking     │
│ - Field validation  │
│ - Computed fields   │
└─────┬───────────────┘
      │
      ▼
┌─────────────────────┐
│  Business Logic     │
│  - Load JSON        │
│  - Process data     │
│  - Calculate BMI    │
└─────┬───────────────┘
      │
      ▼
┌─────────────────────┐
│  Save to JSON       │
│  (persistence)      │
└─────┬───────────────┘
      │
      ▼
┌─────────────────────┐
│  JSON Response      │
│  (with status code) │
└─────────────────────┘
```

### **Insurance Prediction Flow:**
```
┌─────────────────┐
│  User Input     │
│  (Streamlit UI) │
└────────┬────────┘
         │
         ▼
┌─────────────────────────┐
│  POST /predict          │
│  {age, weight, city...} │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Pydantic Model         │
│  - Validate input       │
│  - Compute BMI          │
│  - Compute lifestyle    │
│  - Compute age_group    │
│  - Compute city_tier    │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Create DataFrame       │
│  [bmi, age_group,       │
│   lifestyle_risk,       │
│   city_tier, income,    │
│   occupation]           │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  ML Model Prediction    │
│  - model.predict()      │
│  - model.predict_proba()│
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Format Response        │
│  {predicted_category,   │
│   confidence,           │
│   class_probabilities}  │
└────────┬────────────────┘
         │
         ▼
┌─────────────────────────┐
│  Display in Streamlit   │
│  (User sees result)     │
└─────────────────────────┘
```

---

## ✨ Best Practices Demonstrated

### 1. **Type Safety**
```python
from typing import Annotated, Literal, Optional

age: Annotated[int, Field(..., gt=0, lt=120)]
occupation: Literal['retired', 'freelancer', 'student']
```

### 2. **Input Validation**
- Age constraints (0-120)
- Height validation (0-2.5m)
- Email format validation
- Domain-specific validation

### 3. **Error Handling**
```python
if patient_id not in data:
    raise HTTPException(status_code=404, detail='Patient not found')
```

### 4. **Computed Fields**
```python
@computed_field
@property
def bmi(self) -> float:
    return self.weight / (self.height ** 2)
```

### 5. **Data Normalization**
```python
@field_validator('city')
@classmethod
def normalize_city(cls, v: str) -> str:
    return v.strip().title()
```

### 6. **Separation of Concerns**
- API logic in `app.py`
- UI logic in `frontend.py`
- Data models using Pydantic
- ML model as separate artifact

### 7. **Environment Configuration**
```python
API_URL = os.getenv("API_URL", "http://127.0.0.1:8000/predict")
```

### 8. **Documentation**
- Inline code comments
- Pydantic field descriptions
- Automatic API documentation
- Project documentation files

---

## 🔐 HTTP Status Codes Used

| Code | Usage | Description |
|------|-------|-------------|
| **200 OK** | Successful GET, PUT | Request succeeded |
| **201 Created** | Successful POST | Resource created successfully |
| **400 Bad Request** | Invalid input | Validation error or malformed request |
| **404 Not Found** | Resource missing | Patient/endpoint not found |
| **500 Internal Server Error** | Server error | Unexpected server-side error |

---

## 🚧 Future Enhancements

### **Patient Management API:**
- [ ] Add database integration (PostgreSQL/MongoDB)
- [ ] Implement authentication & authorization
- [ ] Add pagination for large datasets
- [ ] Include medical history tracking
- [ ] Add appointment scheduling

### **Insurance Prediction:**
- [ ] Model retraining pipeline
- [ ] A/B testing for model versions
- [ ] More sophisticated feature engineering
- [ ] Integration with payment gateways
- [ ] User authentication and history tracking

### **General:**
- [ ] Unit tests (pytest)
- [ ] Integration tests
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] Logging and monitoring (ELK stack)
- [ ] Rate limiting and caching
- [ ] API versioning

---

## 📝 Learning Resources

### **Official Documentation:**
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Streamlit Documentation](https://docs.streamlit.io/)

### **Tutorials Covered:**
1. ✅ FastAPI basics and routing
2. ✅ Pydantic models and validation
3. ✅ CRUD operations with JSON storage
4. ✅ ML model deployment
5. ✅ Frontend-backend integration
6. ✅ Docker containerization

---

## 🤝 Contributing

This is a learning project! Feel free to:
- Fork the repository
- Experiment with the code
- Add new features
- Improve documentation
- Share your learnings

---

## 📄 License

This project is created for educational purposes. Feel free to use and modify as needed for your learning journey.

---

## 🙋 Support

If you're using this project for learning:
1. Start with `1.py` to understand CRUD basics
2. Explore `pydantic/` examples to master validation
3. Move to `project/` for full-stack ML deployment
4. Experiment by modifying and extending the code

---

## 🎉 Acknowledgments

This project demonstrates practical applications of:
- FastAPI framework capabilities
- Pydantic validation patterns
- RESTful API design principles
- ML model deployment strategies
- Modern Python development practices

---

**Happy Learning! 🚀**

*Built with ❤️ using FastAPI, Pydantic, and Python*
