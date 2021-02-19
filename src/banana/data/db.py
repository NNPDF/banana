# -*- coding: utf-8 -*-
"""
Actually using ``String`` it's pointless, since SQLite has only one text type
and it is ``TEXT``, and the maximum length is coherently ignored by SQLite.
Nevertheless the information is stored in the DB, even if the DBMS won't use it,
so we can keep declaring a size for fields where it matters.

Same considerations apply to datetime, with the further gain that SQLite it's
storing as he wish but able to use some dedicated functions.
"""
import pathlib

import sqlalchemy
from sqlalchemy import Column, Integer, Float, String, Text, DateTime
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base


class MyBase:
    uid = Column(Integer, primary_key=True, unique=True)
    hash = Column(String(64), unique=True)
    # TODO: should we use `func.utcnow`?
    # https://stackoverflow.com/a/33532154/8653979
    ctime = Column(DateTime(timezone=True), server_default=func.now())
    mtime = Column(DateTime(timezone=True), onupdate=func.now())


Base = declarative_base(cls=MyBase)


class Theory(Base):
    __tablename__ = "theories"
    ID = Column(Integer)
    PTO = Column(Integer)
    CKM = Column(Text)
    Comments = Column(Text)
    DAMP = Column(Integer)
    EScaleVar = Column(Integer)
    FNS = Column(Text)
    GF = Column(Float)
    HQ = Column(Text)
    IC = Column(Integer)
    MP = Column(Float)
    MW = Column(Float)
    MZ = Column(Float)
    MaxNfAs = Column(Integer)
    MaxNfPdf = Column(Integer)
    ModEv = Column(Text)
    NfFF = Column(Integer)
    Q0 = Column(Float)
    QED = Column(Integer)
    Qedref = Column(Float)
    Qmb = Column(Float)
    Qmc = Column(Float)
    Qmt = Column(Float)
    Qref = Column(Float)
    SIN2TW = Column(Float)
    SxOrd = Column(Text)
    SxRes = Column(Integer)
    TMC = Column(Integer)
    XIF = Column(Float)
    XIR = Column(Float)
    alphaqed = Column(Float)
    alphas = Column(Float)
    global_nx = Column(Integer)
    kDISbThr = Column(Float)
    kDIScThr = Column(Float)
    kDIStThr = Column(Float)
    kbThr = Column(Float)
    kcThr = Column(Float)
    ktThr = Column(Float)
    mb = Column(Float)
    mc = Column(Float)
    mt = Column(Float)


# mixin
class CalcResult:
    external = Column(Text)
    t_hash = Column(String(64))
    o_hash = Column(String(64))
    pdf = Column(Text)


class Cache(CalcResult, Base):
    __tablename__ = "cache"
    result = Column(Text)


class Log(CalcResult, Base):
    __tablename__ = "logs"
    log = Column(Text)


def engine(path):
    # Create an engine that stores data in the local directory's
    # sqlalchemy_example.db file.
    path = pathlib.Path(path).absolute()
    return sqlalchemy.create_engine(f"sqlite:///{str(path)}")


def create_db(base_cls, engine):
    # Create all tables in the engine. This is equivalent to "Create Table"
    # statements in raw SQL.
    base_cls.metadata.create_all(engine)
