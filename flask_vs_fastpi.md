# Flask vs FastAPI: 

# overview

This guide is crafted to help  clearly understand the differences and similarities between **Flask** and **FastAPI**, including how to perform CRUD operations, work with APIs, and use Pydantic for validation.

---

## 1. What is Flask?

**Flask** is a lightweight Python web framework built on **WSGI (Web Server Gateway Interface)**. It is synchronous and simple to get started with, often used for small APIs and quick prototypes.

### Key Features:

- Simple and flexible
- Synchronous request handling
- Manual data validation
- Requires extensions for documentation

---

## 2. What is FastAPI?

**FastAPI** is a modern Python web framework based on **ASGI (Asynchronous Server Gateway Interface)**. It is asynchronous by default and uses **Pydantic** for data validation and serialization.

### Key Features:

- Fast and asynchronous
- Built-in Pydantic validation
- Automatic API docs (Swagger, ReDoc)
- Great for modern web applications and microservices

---

## 3. Installation Guide

### Installing Flask:

```bash
pip install flask
```

> Flask uses the built-in development server, no extra tools needed.

### Installing FastAPI and Uvicorn:

```bash
pip install fastapi uvicorn
```

> `uvicorn` is the ASGI server used to run FastAPI apps.

To start a FastAPI server:

```bash
uvicorn main:app --reload
```

---

## 4. What is an API?

**API (Application Programming Interface)** allows software to communicate over a network. A **Web API** enables this communication using HTTP protocols.

### Real-World Example:

When you open a weather app, it calls a web API like:

```
GET /weather?city=London
```

And the server returns JSON:

```json
{
  "city": "London",
  "temperature": "28°C"
}
```

---

## 5. What are HTTP API Methods?

HTTP Methods define what action you want the server to perform:

| Method | Action         | Description                     |
| ------ | -------------- | ------------------------------- |
| GET    | Read           | Get data from the server        |
| POST   | Create         | Send new data to the server     |
| PUT    | Update         | Modify existing data completely |
| PATCH  | Partial Update | Modify part of the data         |
| DELETE | Delete         | Remove data from the server     |

---

## 6. What is CRUD?

**CRUD** stands for:

- **Create** → Add new data (POST)
- **Read** → Get existing data (GET)
- **Update** → Modify existing data (PUT/PATCH)
- **Delete** → Remove existing data (DELETE)

### Example:

- Add new user → `POST /users`
- Get user info → `GET /users/1`
- Update user info → `PUT /users/1`
- Delete user → `DELETE /users/1`

---

## 7. Flask CRUD Example 

```python
from flask import Flask, request, jsonify

app = Flask(__name__)
data = []

@app.route('/items', methods=['POST'])
def create_item():
    item = request.json
    data.append(item)
    return jsonify({"msg": "Item added"}), 201

@app.route('/items', methods=['GET'])
def read_items():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 8. FastAPI CRUD Example 

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Data model
class Message(BaseModel):
    text: str

# In-memory store
saved_message = ""

# POST method
@app.post("/save")
def save_message(msg: Message):
    global saved_message
    saved_message = msg.text
    return {"message": "Message saved!"}

# GET method
@app.get("/read")
def read_message():
    return {"saved_message": saved_message}
```

To run:

```bash
uvicorn main:app --reload
```

---

## 9. What is Pydantic?

**Pydantic** is a Python library used in FastAPI to validate and serialize data using Python type hints.

### Key Concepts:

- Create models by inheriting from `BaseModel`
- FastAPI uses these models to automatically validate JSON input

### Example:

```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    quantity: int
```

If a request sends:

```json
{
  "name": 123,
  "quantity": "five"
}
```

FastAPI automatically returns:

```json
{
  "detail": [
    {"msg": "str type expected"},
    {"msg": "value is not a valid integer"}
  ]
}
```

---

## 10. How JSON and Postman Work with APIs

### What is JSON?

JSON (JavaScript Object Notation) is the format APIs use to send and receive data.

### Example:

```json
{
  "name": "Laptop",
  "quantity": 5
}
```

### What is Postman?

Postman is a GUI tool to test your APIs:

- Set method: GET, POST, PUT, DELETE
- Set URL: [http://127.0.0.1:8000/items](http://127.0.0.1:8000/items)
- Set Body: JSON payload (for POST/PUT)
- View server responses

### Example Request in Postman:

- **Method:** POST
- **URL:** `http://127.0.0.1:8000/items`
- **Body:** Raw JSON

```json
{
  "name": "Phone",
  "quantity": 2
}
```

- **Expected Response:**

```json
{
  "msg": "Item added"
}
```

---

## 11. API Docs in FastAPI

FastAPI automatically generates:

- **Swagger UI** at `http://127.0.0.1:8000/docs`
- **ReDoc** at `http://127.0.0.1:8000/redoc`

These provide a user-friendly interface to test your APIs without needing Postman.

---

## ✅ Summary: Flask vs FastAPI

| Feature         | Flask (WSGI)           | FastAPI (ASGI)               |
| --------------- | ---------------------- | ---------------------------- |
| Speed           | Slower (sync only)     | Faster (async supported)     |
| Data Validation | Manual                 | Automatic via Pydantic       |
| API Docs        | Manual setup           | Auto-generated               |
| Learning Curve  | Easier for simple use  | Modern, clean with typing    |
| Use Case        | Quick APIs, prototypes | Scalable APIs, microservices |

---
## 12. questios

1. What is the difference between Flask and FastAPI?

2. What does API stand for?

3. Why should login use POST, not GET?

4. What is Content-Type used for?

5. How do you pass query parameters in a URL?

6. What is a JSON body?

7. How do you validate data in FastAPI?

8. How do you connect MongoDB to Flask?

9. How is FastAPI’s performance better than Flask?

10. .How do you send headers in Postman?

11. What HTTP method is used to update a record?

12. Which module is used for async MongoDB in FastAPI?

13. What status code is returned when a resource is created?

14. What tool can you use to test REST APIs?

15. What’s the use of .env in Python projects?

---

