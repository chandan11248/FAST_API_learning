# Insurance Premium Prediction Project Documentation

## 1. What We Have Built
We have developed a full-stack Machine Learning application designed to predict insurance premium categories for users based on their personal and demographic data. The project bridges the gap between a data science model and a deployed end-user application.

### Core Components:
- **ML Backend API**: A robust RESTful API built with **FastAPI** that serves a pre-trained machine learning model. It accepts user data, performs real-time feature engineering (e.g., calculating BMI, categorizing cities), and returns predictions with confidence scores.
- **Interactive Frontend**: A user-friendly web interface built with **Streamlit** that allows users to easily input their details (age, income, city, etc.) and view the prediction results instantly.
- **Containerization**: A **Dockerized** environment ensuring the application is portable, consistent, and easy to deploy across different systems.

### Key Features:
- **Real-time Prediction**: Instant categorization of insurance premiums (e.g., Low, Medium, High).
- **Data Validation**: Strict input validation using **Pydantic** ensuring data integrity before it reaches the model.
- **Smart Feature Engineering**: Automatic calculation of derived features like `BMI`, `Lifestyle Risk`, `Age Group`, and `City Tier` within the API logic.
- **Responsive UI**: A simple, intuitive interface that handles API errors gracefully.

---

## 2. What We Have Learned
This project served as a comprehensive exercise in modern AI engineering and software development best practices. Key learning outcomes include:

### Technical Skills:
- **FastAPI Framework**: Learned to build high-performance APIs, handle async requests, and use Pydantic for powerful data validation and serialization.
- **Model Deployment**: Gained experience in loading serialized ML models (`pickle` format) and serving them via a web server (Uvicorn).
- **Frontend-Backend Integration**: Understood the architecture of decoupled applications, where a frontend (Streamlit) consumes a separate backend API via HTTP requests.
- **Docker & DevOps**: Learned how to write a `Dockerfile` to package Python applications, manage dependencies, and expose ports for containerized execution.
- **Feature Engineering Logic**: Implemented business logic (e.g., categorizing cities into tiers, determining lifestyle risk) directly into the application layer to simplify the model's input requirements.

### Concepts & Best Practices:
- **Separation of Concerns**: Keeping the ML inference logic separate from the user interface.
- **Type Safety**: Using Python type hints and Pydantic models to reduce runtime errors.
- **Environment Management**: Handling configurations and secret management for robust deployments.

---

## 3. Project Structure & Technologies

### Directory Structure
```
project/
├── app.py              # Main FastAPI backend application
├── frontend.py         # Streamlit frontend application
├── Dockerfile          # Container configuration
├── requirements.txt    # Python dependencies
├── model.pkl           # Pre-trained ML model (serialized)
├── model.ipynb         # Model training notebook
├── insurance.csv       # Training dataset
└── .dockerignore       # Docker build exclusions
```

### Technology Stack
- **Language**: Python 3.11
- **Web Framework**: FastAPI, Uvicorn
- **Frontend**: Streamlit
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn
- **Validation**: Pydantic
- **Containerization**: Docker

## 4. How to Run
1. **Build the Docker Container:**
   ```bash
   docker build -t insurance-app .
   ```
2. **Run the Application:**
   ```bash
   docker run -p 8000:8000 insurance-app
   ```
3. **Access the App:**
   - Backend Docs: `http://localhost:8000/docs`
   - Frontend: `streamlit run frontend.py` (requires local env) or containerize frontend separately.
