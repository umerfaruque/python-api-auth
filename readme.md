# Activate envirnment
.\myenv\Scripts\activate

# Install Dependency
pip install fastapi uvicorn[standard] python-multipart python-jose[cryptography] passlib[bcrypt]

# Run the application 
uvicorn main:app --reload