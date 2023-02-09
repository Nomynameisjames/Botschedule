#!/usr/bin/python3
import models
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean, DateTime

Base = declarative_base()

class User(Base):
    """
        class maps out a table in the mysql database creating an object
        representation
    """
    __tablename__='January'
    id = Column(Integer, primary_key=True)
    Days = Column(DateTime)
    Course = Column(String(50))
    Topic = Column(String(50))
    Reminder = Column(DateTime)
    Target = Column(Boolean)
    Created_at = Column(DateTime, default=datetime.utcnow)
    Updated_at = Column(DateTime)
    Average = Column(Integer)

    def __str__(self):
        """
            returns a string representation of the class 
        """
        return f"Date: {self.Days} Course: {self.Course} Topic: {self.Topic}\
                Average: {self.Average} Reminder: {self.Reminder}\
                Created: {self.Created_at}"



class user_id(Base):
    """
        creates a class representation of the user info 
    """
    __tablename__='User_info'
    id = Column(Integer, primary_key=True)
    User_name = Column(String(100))
    Password = Column(String(100))
    Created_at = Column(DateTime, default=datetime.utcnow)
    Updated_at = Column(DateTime)
    
    def __str__(self):
        """
            returns string representation of class objects
        """
        return f"id : {self.id}, username: {self.User_name}"
