# Managing Pydantic Data Models in FastAPI



# Defining models and their field types with Pydantic
# Creating model variations with class inheritance
# Adding custom data validation with Pydantic
# Working with Pydantic objects


# Defining models and their field types with Pydantic

# Standard field types


# from pydantic import BaseModel
# class Person(BaseModel):
#     first_name: str
#     last_name: str
#     age: int



# from datetime import date
# from enum import Enum
# from typing import List
# from pydantic import BaseModel, ValidationError
# class Gender(str, Enum):
#     MALE = "MALE"
#     FEMALE = "FEMALE"
#     NON_BINARY = "NON_BINARY"

# class Person(BaseModel):
#     first_name: str
#     last_name: str
#     gender: Gender
#     birthdate: date
#     interests: List[str] # ['Reading', 'Trekking', 'Watching Movies']

# # Invalid gender
# try:
#     Person(
#         first_name="John",
#         last_name="Doe",
#         gender="INVALID_VALUE",
#         birthdate="1991-01-01",
#         interests=["travel", "sports"],
#     )
# except ValidationError as e:
#     print(str(e))



# # Invalid birthdate
# try:
#     Person(
#         first_name="John",
#         last_name="Doe",
#         gender=Gender.MALE,
#         birthdate="1991-13-42",
#         interests=["travel", "sports"],
#     )
# except ValidationError as e:
#     print(str(e))


# # Valid
# person = Person(
#     first_name="John",
#     last_name="Doe",
#     gender=Gender.MALE,
#     birthdate="1991-01-01",
#     interests=["travel", "sports"],
# )


# # --------------------------------------------------

# # Relationships with models

# # One - One relationship

# class Address(BaseModel):
#     street_address: str
#     postal_code: str
#     city: str
#     country: str
# class Person(BaseModel):
#     first_name: str
#     last_name: str
#     gender: Gender
#     birthdate: date
#     interests: List[str]
#     address: Address


# try:
#     Person(
#         first_name="John",
#         last_name="Doe",
#         gender="INVALID_VALUE",
#         birthdate="1991-01-01",
#         interests=["travel", "sports"],
#         address={
#             "street_address": "12 Squirell Street",
#             "postal_code": "424242",
#             "city": "Woodtown",
#             # Missing country
#         }
#     )
# except ValidationError as e:
#     print(str(e))

# # --------------------------------------------------
# Optional fields and default values

# from typing import Optional
# from pydantic import BaseModel
# class UserProfile(BaseModel):
#     nickname: str
#     location: Optional[str] = None
#     subscribed_newsletter: bool = True
# user = UserProfile(nickname="jdoe")
# print(user)  # nickname='jdoe' location=None subscribed_newsletter=True

# user = UserProfile(nickname="jdoe", subscribed_newsletter=False)
# print(user)  # nickname='jdoe' location=None subscribed_newsletter=False


# # --------------------------------------------------

# from datetime import datetime
# from time import sleep
# from pydantic import BaseModel
# class Model(BaseModel):
#     # Don't do this.
#     # This example shows you why it doesn't work.
#     d: datetime = datetime.now()

# o1 = Model()
# print(o1.d)
 
# time.sleep(1)  # Wait for a second
 
# o2 = Model()
# print(o2.d)
 
# print(o1.d < o2.d)  # False

# # --------------------------------------------------
# Field validation

# from typing import Optional
# from pydantic import BaseModel, Field, ValidationError
# class Person(BaseModel):
#     first_name: str = Field(..., min_length=3)
#     last_name: str = Field(..., min_length=3)
#     age: Optional[int] = Field(None, ge=0, le=120)

# # --------------------------------------------------
# Dynamic default values
# list()

# from datetime import datetime
# from typing import List
# from pydantic import BaseModel, Field
# def list_factory():
#     return ["a", "b", "c"]
# class Model(BaseModel):
#     l: List[str] = Field(default_factory=list_factory)
#     d: datetime = Field(default_factory=datetime.now)
#     l2: List[str] = Field(default_factory=list)

# # --------------------------------------------------
# Validating email addresses and URLs with Pydantic types

# pip install email-validator

# from pydantic import BaseModel, EmailStr, HttpUrl, ValidationError
# class User(BaseModel):
#     email: EmailStr
#     website: HttpUrl
# try:
#     user = User(email="ramesh@aroha.co.in", website="http://www.aroha.co.in")
#     print(user)
# except ValidationError as e:
#     print(str(e))    

# # --------------------------------------------------
# Creating model variations with class inheritance

# from pydantic import BaseModel
# class PostCreate(BaseModel):
#     title: str
#     content: str
# class PostPublic(BaseModel):
#     id: int
#     title: str
#     content: str
# class PostDB(BaseModel):
#     id: int
#     title: str
#     content: str
#     nb_views: int = 0



# from pydantic import BaseModel
# class PostBase(BaseModel):
#     title: str
#     content: str
# class PostCreate(PostBase):
#     pass
# class PostPublic(PostBase):
#     id: int
# class PostDB(PostBase):
#     id: int
#     nb_views: int = 0


# class PostBase(BaseModel):
#     title: str
#     content: str
#     def excerpt(self) -> str:
#         return f"{self.content[:140]}..."


# # --------------------------------------------------

# Adding custom data validation with Pydantic

# Applying validation at a field level

# from datetime import date
# from pydantic import BaseModel, validator
# class Person(BaseModel):
#     first_name: str
#     last_name: str
#     birthdate: date
#     @validator("birthdate")
#     def valid_birthdate(cls, v: date):
#         delta = date.today() - v
#         age = delta.days / 365
#         if age > 120:
#             raise ValueError("You seem a bit too old!")
#         return v

# Create a person object to see this validation - Assignment

# # --------------------------------------------------
# Applying validation at an object level

# from pydantic import BaseModel, EmailStr, ValidationError, root_validator
# class UserRegistration(BaseModel):
#     email: EmailStr
#     password: str
#     password_confirmation: str
#     @root_validator()
#     def passwords_match(cls, values):
#         password = values.get("password")
#         password_confirmation = values.get("password_confirmation")
#         if password != password_confirmation:
#             raise ValueError("Passwords don't match")
#         return values

# Create a person object to see this validation - Assignment

# # --------------------------------------------------
# Applying validation before Pydantic parsing

# from typing import List
# from pydantic import BaseModel, validator
# class Model(BaseModel):
#     values: List[int]
#     @validator("values", pre=True)
#     def split_string_values(cls, v):
#         if isinstance(v, str):
#             return v.split(",")
#         return v
# m = Model(values="1,2,3")
# print(m.values)  # [1, 2, 3]


# # --------------------------------------------------
# Working with Pydantic objects

# Converting an object into a dictionary

person = Person(
    first_name="John",
    last_name="Doe",
    gender=Gender.MALE,
    birthdate="1991-01-01",
    interests=["travel", "sports"],
    address={
        "street_address": "12 Squirell Street",
        "postal_code": "424242",
        "city": "Woodtown",
        "country": "US",
    },
)
person_dict = person.dict()
print(person_dict["first_name"])  # "John"
print(person_dict["address"]["street_address"])  # "12 Squirell Street"


person_include = person.dict(include={"first_name", "last_name"})
print(person_include)  # {"first_name": "John", "last_name": "Doe"}
person_exclude = person.dict(exclude={"birthdate", "interests"})
print(person_exclude)


person_nested_include = person.dict(
    include={
        "first_name": ...,
        "last_name": ...,
        "address": {"city", "country"},
    }
)
# {"first_name": "John", "last_name": "Doe", "address": {"city": "Woodtown", "country": "US"}}
print(person_nested_include)


class Person(BaseModel):
    first_name: str
    last_name: str
    gender: Gender
    birthdate: date
    interests: List[str]
    address: Address
    def name_dict(self):
        return self.dict(include={"first_name", "last_name"})


# # --------------------------------------------------
# Creating an instance from a sub-class object

class PostBase(BaseModel):
    title: str
    content: str
class PostCreate(PostBase):
    pass
class PostPublic(PostBase):
    id: int
class PostDB(PostBase):
    id: int
    nb_views: int = 0


@app.post("/posts", status_code=status.HTTP_201_CREATED, response_model=PostPublic)
async def create(post_create: PostCreate):
    new_id = max(db.posts.keys() or (0,)) + 1
    post = PostDB(id=new_id, **post_create.dict()) # *(args) -> (1, 2, 3 ) ////// **(kwargs) -> (id=1, name='ramesh')
    db.posts[new_id] = post
    return post


# # --------------------------------------------------
# Updating an instance with a partial one

class PostBase(BaseModel):
    title: str
    content: str
class PostPartialUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None


@app.patch("/posts/{id}", response_model=PostPublic)
async def partial_update(id: int, post_update: PostPartialUpdate):
    try:
        post_db = db.posts[id] # 3 : (title='test')
        updated_fields = post_update.dict(exclude_unset=True) # omits content becuase content is not available
        updated_post = post_db.copy(update=updated_fields) # copy of object is taken and update the title field
        db.posts[id] = updated_post # update the content
        return updated_post
    except KeyError:
        raise HTTPException(status.HTTP_404_NOT_FOUND)




