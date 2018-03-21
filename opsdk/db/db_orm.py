# -*- coding: utf-8 -*-
# author:xiaoming
from sqlalchemy import create_engine,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String,DateTime
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy import UniqueConstraint
from conf.setting import db_conf
engine = create_engine(db_conf['mysql'], encoding='utf-8',echo=False)
Base = declarative_base()
class User(Base):
    '''user表的类'''
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False)
    password = Column(String(64), nullable=False)
    tenant_name = Column(String(64), nullable=False)
    domain_name = Column(String(64), nullable=False)
    __table_args__=(UniqueConstraint('username','tenant_name','domain_name'),)
class Endpoint(Base):
    '''endpoint表的类'''
    __tablename__='Endpoint'
    id=Column(Integer,primary_key=True)
    ip=Column(String(32),nullable=False)
    auth_url=Column(String(64),nullable=False)
    region = Column(String(64), nullable=False)
    user_id = Column(Integer,ForeignKey('user.id'))#外键
    user=relationship('User',backref='endpoint') #orm反向查询
    __table_args__ = (UniqueConstraint('ip','auth_url'),)
    def __repr__(self):
        return '<ip %r>' % self.ip
class Openstack_vm(Base):
    '''创建虚机表'''
    __tablename__='openstack_vm'
    id=Column(Integer,primary_key=True)
    name=Column(String(64),nullable=False)
    vm_id=Column(String(64),nullable=False)
    create_time=(DateTime)
    ex_time=(DateTime)
    def __repr__(self):
        return '<name %r>' % self.name
Base.metadata.create_all(engine)

