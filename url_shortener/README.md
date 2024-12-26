# URL Shortener API


## Endpoints

### 1. `POST /shorten`
**Description**: Shortens a provided URL.  

#### Request  
- **Body** (JSON):
  ```json
  {
    "url": "https://edu.hse.ru/mod/assign/view.php?id=1493841"
  }
  ```

#### Response  
- **Success** (200 OK):
  ```json
  {
    "short_url": "769b447b"
  }
  ```
- **Error** (500 Internal Server Error):
  ```json
  {
    "message": "Internal server error"
  }
  ```
- **Error** (400 Bad Request):
  ```json
  {
    "message": "url is required"
  }
  ```

---

### 2. `GET /{short_id}`
**Description**: Redirects to the original URL(getting an original URL).  

#### Request  
- **URL Path**: `/769b447b`

#### Response  
- **Success** (200 OK):
  ```json
  {
    "url": "https://edu.hse.ru/mod/assign/view.php?id=1493841"
  }
  ```
- **Error** (500 Internal Server Error):
  ```json
  {
    "message": "Internal server error"
  }
  ```

---

### 3. `GET /stats/{short_id}`
**Description**: Return info in JSON for the given shortened URL.  

#### Request  
- **URL Path**: `/stats/769b447b`

#### Response  
- **Success** (200 OK):
  ```json
  {
    "original_url": "https://edu.hse.ru/mod/assign/view.php?id=1493841",
    "short_id": "769b447b"
  }
  ```
- **Error** (500 Internal Server Error):
  ```json
  {
    "message": "Internal server error"
  }
  ```