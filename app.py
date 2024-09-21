# wsgi.py
from app import app  # Ensure 'app' is the Flask instance in app.py

if __name__ == "__main__":
    app.run()
