Absolutely! Here's a **FastAPI cheat sheet/demo** showing how to use all the **common parameter types** with clear examples for:

✅ `path`  
✅ `query`  
✅ `body`  
✅ `header`  
✅ `form`  
✅ `cookie`

---

### 🚀 FastAPI Cheat Sheet: Parameters Demo

```python
from fastapi import FastAPI, Path, Query, Body, Header, Form, Cookie
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

# 🎯 Body Model
class Item(BaseModel):
    name: str
    price: float
    in_stock: Optional[bool] = True

# ✅ Path Parameter
@app.get("/items/{item_id}")
def read_item(
    item_id: int = Path(..., title="The ID of the item", ge=1)
):
    return {"path_param": item_id}

# ✅ Query Parameters
@app.get("/search/")
def search_items(
    name: Optional[str] = Query(None, min_length=2),
    limit: int = Query(10, gt=0)
):
    return {"query_param_name": name, "query_param_limit": limit}

# ✅ Body Parameters
@app.post("/items/")
def create_item(
    item: Item = Body(...)
):
    return {"body_param": item}

# ✅ Header Parameters
@app.get("/header/")
def get_custom_header(
    user_agent: Optional[str] = Header(None)
):
    return {"header_param_user_agent": user_agent}

# ✅ Form Parameters
@app.post("/login/")
def login(
    username: str = Form(...),
    password: str = Form(...)
):
    return {"form_param_username": username}

# ✅ Cookie Parameters
@app.get("/cookie/")
def read_cookie(
    session_id: Optional[str] = Cookie(None)
):
    return {"cookie_param_session_id": session_id}
```

---

### 📦 Test Each One (Example Requests)

#### Path
`GET /items/5` → `{"path_param": 5}`

#### Query
`GET /search/?name=book&limit=2` → `{"query_param_name": "book", "query_param_limit": 2}`

#### Body
```json
POST /items/
{
  "name": "Chair",
  "price": 49.99
}
```

#### Header
Send header: `User-Agent: Mozilla`  
→ `{"header_param_user_agent": "Mozilla"}`

#### Form
Send `x-www-form-urlencoded`:
- username: alice
- password: secret

→ `{"form_param_username": "alice"}`

#### Cookie
Send cookie: `session_id=xyz123`  
→ `{"cookie_param_session_id": "xyz123"}`

---

### 🧠 Pro Tips

- Use `Path()`, `Query()`, `Header()`, etc., to **customize and validate** input.
- `Body(...)` is useful with Pydantic models.
- `Form()` is for HTML forms.
- `Cookie()` is for session-related data.

---

Want me to turn this into a real working FastAPI project you can run and test in your browser or Postman?
