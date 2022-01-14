from fastapi import FastAPI, status, Depends
from pydantic import BaseModel
from database import get_database
from databases import Database
app = FastAPI()
class PostDB(BaseModel):
    id: int
    title: str
    content: str
    nb_views: int = 0
class PostCreate(BaseModel):
    title: str
    content: str

@app.on_event("startup")
async def startup():
    await database.connect()
    metadata.create_all(sqlalchemy_engine)
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/posts", response_model=PostDB, status_code=status.HTTP_201_CREATED)
async def create_post(
    post: PostCreate, database: Database = Depends(get_database)
) -> PostDB:
    insert_query = posts.insert().values(post.dict())
    post_id = await database.execute(insert_query)
    post_db = await get_post_or_404(post_id, database)
    return post_db