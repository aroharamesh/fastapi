
# ------------------------------------------
# from fastapi import FastAPI
# app = FastAPI()

# @app.get("/")
# def hello_world():
#     return {"Hello": "World"}


# ------------------------------------------

# Handling request parameters

# pip install httpie


# Path parameters

# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/users/{id}")
# async def get_use(id: int):
#     return {"id" : id}

# Using the command line
# http http://localhost:8000/users/5


# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/users/{type}/{id}")
# async def get_use(type: str, id: int):
#     return {"id" : id, "type": type}

# ------------------------------------------

# Limiting allowed values

# from enum import Enum
# from fastapi import FastAPI
# app = FastAPI()

# class UserType(str, Enum):
#     STANDARD = "standard"
#     ADMIN = "admin"

# @app.get("/users/{type}/{id}")
# async def get_use(type: UserType, id: int):
#     return {"id" : id, "type": type}

# ------------------------------------------

# Advanced validation
# gt
# ge
# lt
# le

# from fastapi import FastAPI, Path
# app = FastAPI()
# @app.get("/users/{id}")
# async def get_user(id: int = Path(..., ge=1)):
#     return {"id": id}


# from fastapi import FastAPI, Path
# app = FastAPI()
# @app.get("/license-plates/{license}")
# async def get_licencse_plate(license: str = Path(..., min_length= 3, max_length=5)):
#     return {"license": license}


# Assignment - Valid input for the below program
# 192.168.1.1
# ramesh@aroha.co.in
# from fastapi import FastAPI, Path
# app = FastAPI()
# @app.get("/license-plates/{license}")
# async def get_license_plate(license: str = Path(..., regex=r"^\w{2}-\d{3}-\w{2}$")):
#     return {"license": license}


# ------------------------------------------

# Query Parameters

# from fastapi import FastAPI, Path
# app = FastAPI()
# @app.get("/users")
# async def get_user(page: int =1, size: int = 10):
#     return {"page": page, "size": size}


# Validations on query parameters
# from fastapi import FastAPI, Path, Query
# app = FastAPI()
# @app.get("/users")
# async def get_user(page: int = Query(1, gt=0), size: int = Query(10, le=100)):
#     return {"page": page, "size": size}


# ------------------------------------------
# The request body

# from fastapi import FastAPI, Body
# app = FastAPI()
# @app.post("/users")
# async def create_user(name: str = Body(...), year: int = Body(...)):
#     return {"name": name, "year": year}


# pydantic models
# from fastapi import FastAPI
# from pydantic import BaseModel
# app = FastAPI()

# class User(BaseModel):
#     name: str
#     year: int

# @app.post("/users")
# async def create_user(user: User):
#     return user


# Multiple objects

# from fastapi import FastAPI
# from pydantic import BaseModel
# app = FastAPI()

# class User(BaseModel):
#     name: str
#     year: int

# class Company(BaseModel):
#     name: str

# @app.post("/users")
# async def create_user(user: User, company: Company):
#     return {"user": user, "company": company}


# Singular body values

# from fastapi import FastAPI, Body
# from pydantic import BaseModel
# app = FastAPI()

# class User(BaseModel):
#     name: str
#     year: int


# @app.post("/users")
# async def create_user(user: User, priority: int = Body(..., gt=1, le=3)):
#     return {"user": user, "priority": priority}


# ------------------------------------------

# Form data and file uploads

# pip install python-multipart

# Form data

# from fastapi import FastAPI, Form
# app = FastAPI()

# @app.post("/users")
# async def create_user(name: str = Form(...), year: int = Form(...)):
#     return {"name": name, "year":year}


# File uploads

# from fastapi import FastAPI, File
# app = FastAPI()
# @app.post("/files")
# async def upload_file(file: bytes = File(...)):
#     return {"file_size": len(file)}


# file-like interface

# from fastapi import FastAPI, File, UploadFile
# app = FastAPI()
# @app.post("/files")
# async def upload_file(file: UploadFile = File(...)):
#     return {"file_name": file.filename, "content_type": file.content_type}


# multiple files 

# from fastapi import FastAPI, File, UploadFile
# from typing import List
# app = FastAPI()
# @app.post("/files")
# async def upload_multiple_files(files: List[UploadFile] = File(...)):
#     return [
#         {"file_name": file.filename, "content_type": file.content_type}
#         for file in files
#     ]


# ------------------------------------------
# Headers and cookies

# from fastapi import FastAPI, Header
# app = FastAPI()

# @app.get("/")
# async def get_header(hello: str = Header(...)):
#     return {"hello": hello}



# Request from which client (postman/chrome/mobile etc.,)
# from fastapi import FastAPI, Header
# app = FastAPI()

# @app.get("/")
# async def get_header(user_agent: str = Header(...)):
#     return {"user_agent": user_agent}



# cookies in the Header

# from fastapi import FastAPI, Cookie
# from typing import Optional
# app = FastAPI()

# @app.get("/")
# async def get_cookie(hello: Optional[str] = Cookie('ramehs')):
#     return {"hello": hello}

# ------------------------------------------

# The request object

# from fastapi import FastAPI, Request
# app = FastAPI()
# @app.get("/ramesh/{id}")
# async def get_request_object(request:Request):
#     return {"path": request.url.path}


# ------------------------------------------

# Customizing the response


# The status code
# https://httpstatuses.com

# 201 Created
# from fastapi import FastAPI, status
# from pydantic import BaseModel
# class Post(BaseModel):
#     title: str

# app = FastAPI()

# @app.post("/posts", status_code = status.HTTP_201_CREATED)
# async def create_post(post: Post):
#     return post

#---

# from fastapi import FastAPI, status
# from pydantic import BaseModel
# class Post(BaseModel):
#     title: str
#     nb_views: int
# posts = {
#     1: Post(title = "Hello", nb_views = 100),
# }

# app = FastAPI()

# @app.delete("/posts/{id}", status_code =  status.HTTP_204_NO_CONTENT)
# async def delete_post(id: int):
#     posts.pop(id, None)
#     return None



# The response model

# from fastapi import FastAPI, status
# from pydantic import BaseModel
# class Post(BaseModel):
#     title: str
#     nb_views: int

# posts = {
#     1: Post(title = "Hello", nb_views = 100),
# }
# app = FastAPI()
# @app.get("/posts/{id}")
# async def get_post(id: int):
#     return posts[id]

#---
# from fastapi import FastAPI, status
# from pydantic import BaseModel
# class Post(BaseModel):
#     title: str
#     nb_views: int

# class PublicPost(BaseModel):
#     title: str

# posts = {
#     1: Post(title = "Hello", nb_views = 100),
# }

# app = FastAPI()
# @app.get("/posts/{id}", response_model = PublicPost)
# async def get_post(id: int):
#     return posts[id]
# ------------------------------------------

# The response parameter

# from fastapi import FastAPI, Response
# app = FastAPI()
# @app.get("/")
# async def custom_header(response: Response):
#     varA = "Ramesh"
#     response.headers["Custom-Header"] =  varA
#     return {"hello": "world"}


# Setting cookies


# from fastapi import FastAPI, Response
# app = FastAPI()
# @app.get("/")
# async def custom_cookie(response: Response):
#     response.set_cookie("cookie-name", "cookie-value", max_age=86400)
#     return {"hello": "world"}

# ------------------------------------------
# Setting the status code dynamically

# from fastapi import FastAPI, status, Response
# from pydantic import BaseModel
# class Post(BaseModel):
#     title: str
#     nb_views: int

# posts = {
#     1: Post(title = "Hello", nb_views = 100),
# }

# app = FastAPI()
# @app.put("/posts/{id}")
# async def update_or_create_post(id: int, post: Post, response: Response):
#     if id not in posts:
#         response.status_code = status.HTTP_201_CREATED
#     posts[id] = post
#     return posts[id]



# ------------------------------------------

# Raising HTTP Errors

# from fastapi import FastAPI, Body, status, HTTPException

# app = FastAPI()
# @app.post("/password")
# async def check_password(password: str = Body(...), password_confirm: str = Body(...)):
#     if password != password_confirm:
#         raise HTTPException(
#             status.HTTP_400_BAD_REQUEST,
#             detail = "Passsword don't match",
#         )
#     return {"message": "password match"}



# ------------------------------------------

# Building a custom response

# HTMLResponse: This can be used to return an HTML response.
# PlainTextResponse: This can be used to return raw text.
# RedirectResponse: This can be used to make a redirection.
# StreamingResponse: This can be used to stream a flow of bytes.
# FileResponse: This can be used to automatically build a proper file response given the path of a file on the local disk.


# from fastapi import FastAPI, status
# from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse
# app = FastAPI()
# @app.get("/html", response_class=HTMLResponse)
# async def get_html():
#     return """
#         <html>
#             <head>
#                 <title>Hello world!</title>
#             </head>
#             <body>
#                 <h1>Hello world!</h1>
#             </body>
#         </html>
#     """
# @app.get("/text", response_class=PlainTextResponse)
# async def text():
#     return "Hello world!"
# @app.get("/redirect")
# async def redirect():
#     return RedirectResponse("/text", status_code=status.HTTP_301_MOVED_PERMANENTLY)



# Serving a file
# from os import path
# from fastapi import FastAPI, status
# from fastapi.responses import FileResponse
# app = FastAPI()
# @app.get("/cat")
# async def get_cat():
#     root_directory = path.dirname(path.dirname(__file__))
#     picture_path = path.join(root_directory, "assets", "1.png")
#     return FileResponse(picture_path)



# Custom responses


from fastapi import FastAPI, status, Response
app = FastAPI()
@app.get("/xml")
async def get_xml():
    content = """<?xml version="1.0" encoding="UTF-8"?>
        <Hello>World</Hello>
    """
    return Response(content=content, media_type="application/xml")