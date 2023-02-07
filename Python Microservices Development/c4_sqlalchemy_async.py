from sqlalchemy.ext.asyncio import create_async_engine,AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String, Boolean, JSON
from sqlalchemy.orm import Session
from sqlalchemy.future import select
from sqlalchemy import update

from contextlib import asynccontextmanager
from quart import Quart 

# 初始化數據庫
DATABASE_URL = 'sqlite+aiosqlite:///./test.db'
engine = create_async_engine(
    DATABASE_URL,
    future=True,
    echo=True
)

async_session = sessionmaker(engine,expire_on_commit=False,class_ = AsyncSession)
Base = declarative_base()

# data Model
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String)
    email = Column(String)
    slack_id = Column(String)
    password = Column(String)
    config = Column(String)
    is_activate = Column(Boolean,default=True)
    is_admin = Column(Boolean,default=False)
    
    def json(self):
        return {"id":self.id,"email":self.email,'config':self.config}
    
'''data access layer(DAL)'''
class UserDAL:
    def __init__(self,db_session):
        self.db_session = db_session
    
    async def create_user(self,name,email,slack_id):
        new_user = User(name=name,email=email,slack_id=slack_id)
        self.db_session.add(new_user)
        await self.db_session.flush()
        return new_user.json()
    
    async def get_all_users(self):
        query_result = await self.db_session.execute(select(User).order_by(User.id))
        return {"Users":[user.json() for user in query_result.scalars().all()]}

    async def get_user(self,user_id):
        query = select(User).where(User.id==user_id)
        query_result = await self.db_session.execute(query)
        user = query_result.one()
        return user[0].json()
    


app = Quart(__name__)
@app.before_serving
async def startup():
    # create db tables 
    async with engine.begin() as conn:
        # this resets the database -- remove for a real project 
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
        async with user_dal() as bd:
            await bd.create_user("name","email","slack_id")


        
'''With the DAL set up,we can use a feature provided by Python's own contextlib to create an asynchronous context manager'''
@asynccontextmanager
async def user_dal():
    async with async_session() as session:
        async with session.begin():
            yield UserDAL(session)

@app.get("/users/<int:user_id>")
async def get_user(user_id):
    async with user_dal() as ud :
        return await ud.get_user(user_id)

@app.get('/users')
async def get_all_users():
    async with user_dal() as ud :
        return await ud.get_all_users()
if __name__ =='__main__':
    app.run()
