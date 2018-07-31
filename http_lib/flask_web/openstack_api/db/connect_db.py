# -*- coding: utf-8 -*-
# author:xiaoming
from sqlalchemy import create_engine,String,Integer,Column,UniqueConstraint
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
Base=declarative_base()
class Op_Connect(Base):
    __tablename__='connect'
    id=Column(Integer,primary_key=True)
    ip=Column(String(20),nullable=False)
    port=Column(String(20),nullable=False)
    domain=Column(String(64),nullable=False)
    project=Column(String(64),nullable=False)
    username=Column(String(64),nullable=False)
    password=Column(String(64),nullable=False)
    __table_args__ = (UniqueConstraint('ip','port'),)
# engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/test')
#连接数据库
engine = create_engine('mysql+pymysql://root:password@172.24.2.10:3306/op_connect',encoding='utf-8',echo=True)
Base.metadata.create_all(engine)#创建表结构