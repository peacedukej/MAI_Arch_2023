from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, UniqueConstraint, Index, Text, TIMESTAMP, func
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column

from .database import Base
from datetime import datetime

class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True)
    login = Column(String, nullable=False, unique=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    password = Column(String, nullable=False)

class GroupChat(Base):
    __tablename__ = "group_chats"
    chat_id = Column(Integer, primary_key=True)
    chat_name = Column(String, nullable=False)

class GroupChatMembers(Base):
    __tablename__ = "group_chat_members"
    chat_id = Column(Integer, ForeignKey('group_chats.chat_id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)

    user = relationship("User", backref="GroupChatMembers")
    chat = relationship("GroupChat", backref="GroupChatMembers")
    
    
class GroupChatMessages(Base):
    __tablename__ = "group_chat_messages"
    message_id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, ForeignKey('group_chats.chat_id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    message_text = Column(Text, nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False)

    user = relationship("User", backref="GroupChatMessages")
    chat = relationship("GroupChat", backref="GroupChatMessages")
    

class PTPChat(Base):
    __tablename__ = "ptp_chats"
    chat_id = Column(Integer, primary_key=True)

class PTPChatMessages(Base):
    __tablename__ = "ptp_chat_messages"
    message_id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, ForeignKey('ptp_chats.chat_id'))
    sender_id = Column(Integer, ForeignKey('users.user_id'))
    receiver_id = Column(Integer, ForeignKey('users.user_id'))
    message_text = Column(Text, nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False)

    sender = relationship("User", foreign_keys=[sender_id])
    receiver = relationship("User", foreign_keys=[receiver_id])
    ptp_chat = relationship("PTPChat", backref="PTPChatMessages")
    

class PTPChatMembers(Base):
    __tablename__ = "ptp_chat_members"
    chat_id = Column(Integer, ForeignKey('ptp_chats.chat_id'), primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), primary_key=True)
    
    user = relationship("User", backref="PTPChatMembers")
    chat = relationship("PTPChat", backref="PTPChatMembers")