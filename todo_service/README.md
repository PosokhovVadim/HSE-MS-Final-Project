# To-Do Service API


## Endpoints

### 1. `POST /items`
**Description**: Creating a new task.  

#### Request  
- **Body** (JSON):
  ```json
  {
    "title": "Название задачи",
    "description": "Описание задачи",
    "completed": false
  } 
  ```

#### Response  
- **Success** (200 OK):
  ```json
  {
    "id": 1,
    "title": "Название задачи",
    "description": "Описание задачи",
    "completed": false
  }
  ```
- **Error** (500 Internal Server Error):
  ```json
  {
    "message": "Internal server error"
  }
  ```
- **Error** (422 Unprocessable Content):
  ```json
  {
    "message": "title is required"
  }
  ```

---

### 2. `GET /items`
**Description**: Retrieve all tasks.

#### Request  
- **No body is required**.

#### Response  
- **Success** (200 OK):
  ```json
  [
    {
      "id": 1,
      "title": "Название задачи",
      "description": "Описание задачи",
      "completed": false
    },
    ...
  ]
  ```
- **Error** (500 Internal Server Error):
  ```json
  {
    "message": "Internal server error"
  }
  ```

---

### 3. `GET /items/{item_id}`
**Description**: Retrieve a specific task by ID.

#### Request  
- **URL Path**: `/items/1`

#### Response  
- **Success** (200 OK):
  ```json
  {
    "id": 1,
    "title": "Название задачи",
    "description": "Описание задачи",
    "completed": false
  }
  ```
- **Error** (404 Not Found):
  ```json
  {
    "message": "Item not found"
  }
  ```
- **Error** (500 Internal Server Error):
  ```json
  {
    "message": "Internal server error"
  }
  ```

---

### 4. `PUT /items/{item_id}`
**Description**: Update an existing task by ID.

#### Request  
- **URL Path**: `/items/1`
- **Body** (JSON):
  ```json
  {
    "title": "Новое название задачи",
    "description": "Новое описание задачи",
    "completed": true
  } 
  ```

#### Response  
- **Success** (200 OK):
  ```json
  {
    "id": 1,
    "title": "Новое название задачи",
    "description": "Новое описание задачи",
    "completed": true
  }
  ```
- **Error** (404 Not Found):
  ```json
  {
    "message": "Item not found"
  }
  ```
- **Error** (500 Internal Server Error):
  ```json
  {
    "message": "Internal server error"
  }
  ```

---

### 5. `DELETE /items/{item_id}`
**Description**: Delete a task by ID.

#### Request  
- **URL Path**: `/items/1`

#### Response  
- **Success** (200 OK):
  ```json
  {
    "message": "Item successfully deleted"
  }
  ```
- **Error** (404 Not Found):
  ```json
  {
    "message": "Item not found"
  }
  ```
- **Error** (500 Internal Server Error):
  ```json
  {
    "message": "Internal server error"
  }
  ```

