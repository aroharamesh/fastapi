# Dependency Injections in FastAPI


# What is dependency injection?
# automatically instantiate objects and the ones they depend on. 

# Creating and using a function dependency
# Creating and using a parameterized dependency with a class
# Using dependencies at a path, router, and global level
#-----------------------------------------------------

# from fastapi import FastAPI, Header
# app = FastAPI()
# @app.get("/")
# async def header(user_agent: str = Header(...)):
#     return {"user_agent": user_agent}

#-----------------------------------------------------
# Creating and using a function dependency

# from fastapi import FastAPI, Header, Depends, Query
# from typing import Tuple
# app = FastAPI()
# # async def pagination(skip: int = 0, limit: int = 10) -> Tuple[int, int]:
# #     return (skip, limit) #(1, 2)
# async def pagination(
#     skip: int = Query(0, ge=0),
#     limit: int = Query(10, ge=0),
# ) -> Tuple[int, int]:
#     capped_limit = min(100, limit)
#     return (skip, capped_limit)
# @app.get("/items")
# async def list_items(p: Tuple[int, int] = Depends(pagination)):
#     skip, limit = p
#     return {"skip": skip, "limit": limit}
# @app.get("/things")
# async def list_things(p: Tuple[int, int] = Depends(pagination)):
#     skip, limit = p
#     return {"skip": skip, "limit": limit}

# Object Destructuring 

# person = {"name": "ramesh", "company": "Aroha"}

# name, company = person
# person.name
# person.company 

#-----------------------------------------------------
# Get an object or raise a 404 error

# async def get_post_or_404(id: int) -> Post:
#     try:
#         return db.posts[id]
#     except KeyError:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


# @app.get("/posts/{id}")
# async def get(post: Post = Depends(get_post_or_404)):
#     return post
# @app.patch("/posts/{id}")
# async def update(post_update: PostUpdate, post: Post = Depends(get_post_or_404)):
#     updated_post = post.copy(update=post_update.dict())
#     db.posts[post.id] = updated_post
#     return updated_post
# @app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete(post: Post = Depends(get_post_or_404)):
#     db.posts.pop(post.id)



#-----------------------------------------------------
# Creating and using a parameterized dependency with a class

# Work on the below code to understand

# from fastapi import FastAPI, Header, Depends, Query
# from typing import Tuple
# app = FastAPI()
# class Pagination:
#     def __init__(self, maximum_limit: int = 100):
#         self.maximum_limit = maximum_limit
#     async def __call__(
#         self,
#         skip: int = Query(0, ge=0),
#         limit: int = Query(10, ge=0),
#     ) -> Tuple[int, int]:
#         capped_limit = min(self.maximum_limit, limit)
#         return (skip, capped_limit)

# @app.get("/")
# async def test_class_call():
#     testpaginate = Pagination()
#     test = testpaginate(200, 300)
#     return test
# paginate = Pagination()


#-----------------------------------------------------
# Example of init and call

# class Foo:
#     def __init__(self, a, b, c):
#         # ----

# x = Foo(1 ,2, 3) # __init__


# class Foo:
#     def __call__(self, a, b, c):
#         # ----

# x = Foo() 
# x(1, 2, 3) # __call__

# __init__ method is used when the class is called to initialize the instance, 
# while the __call__ method is called when the instance is called 

#-----------------------------------------------------
# Use class methods as dependencies

# from fastapi import FastAPI, Header, Depends, Query
# from typing import Tuple
# app = FastAPI()
# class Pagination:
#     def __init__(self, maximum_limit: int = 100):
#         self.maximum_limit = maximum_limit
#     async def skip_limit(
#         self,
#         skip: int = Query(0, ge=0),
#         limit: int = Query(10, ge=0),
#     ) -> Tuple[int, int]:
#         capped_limit = min(self.maximum_limit, limit)
#         return (skip, capped_limit)
#     async def page_size(
#         self,
#         page: int = Query(1, ge=1),
#         size: int = Query(10, ge=0),
#     ) -> Tuple[int, int]:
#         capped_size = min(self.maximum_limit, size)
#         return (page, capped_size)


# pagination = Pagination(maximum_limit=50)
# @app.get("/items")
# async def list_items(p: Tuple[int, int] = Depends(pagination.skip_limit)):
#     skip, limit = p
#     return {"skip": skip, "limit": limit}
# @app.get("/things")
# async def list_things(p: Tuple[int, int] = Depends(pagination.page_size)):
#     page, size = p
#     return {"page": page, "size": size}


#-----------------------------------------------------

# Using dependencies at a path, router, and global level

def secret_header(secret_header: Optional[str] = Header(None)) -> None:
    if not secret_header or secret_header != "SECRET_VALUE":
        raise HTTPException(status.HTTP_403_FORBIDDEN)

# Use a dependency on a path decorator
@app.get("/protected-route", dependencies=[Depends(secret_header)])
async def protected_route():
    return {"hello": "world"}

#-----------------------------------------------------
# Use a dependency on a whole router

router = APIRouter(dependencies=[Depends(secret_header)])
@router.get("/route1")
async def router_route1():
    return {"route": "route1"}
@router.get("/route2")
async def router_route2():
    return {"route": "route2"}
app = FastAPI()
app.include_router(router, prefix="/router")

#-----------------------------------------------------

router = APIRouter()
@router.get("/route1")
async def router_route1():
    return {"route": "route1"}
@router.get("/route2")
async def router_route2():
    return {"route": "route2"}
app = FastAPI()
app.include_router(router, prefix="/router", dependencies=[Depends(secret_header)])

#-----------------------------------------------------
# Use a dependency on a whole application


app = FastAPI(dependencies=[Depends(secret_header)])
@app.get("/route1")
async def route1():
    return {"route": "route1"}
@app.get("/route2")
async def route2():
    return {"route": "route2"}