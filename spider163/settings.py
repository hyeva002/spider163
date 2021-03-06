# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from spider163.utils import config
from sqlalchemy_utils.functions import database_exists


def configure_orm():
    global engine
    global Session
    engine_args = {}
    try :
        if database_exists(config.get_db()) == False:
            create_engine(config.get_mysql()['uri'], echo=False).execute("create database IF NOT EXISTS  {} DEFAULT CHARACTER SET utf8".format(config.get_mysql()['db']))
        engine = create_engine(config.get_db(), **engine_args)
        Session = scoped_session(
            sessionmaker(autocommit=False, autoflush=False, bind=engine))
    except:
        pass

