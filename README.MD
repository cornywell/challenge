Thematic challenge by Kim Cornwell

Run the following to get this development API up and running:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload


Automatic interactive API documentation:

OpenAPI Documentation at:
http://127.0.0.1:8000/docs

Alternative Redoc Documentation at:
http://127.0.0.1:8000/redoc

Run tests:
Within venv run "pytest"

