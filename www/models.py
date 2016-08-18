# models.py

# coding:utf-8

__author__ = 'zhangchi'

import time, uuid

from orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
	return '%015d%s000' % (int(time.time()*1000), uuid.uuid4().hex)

class User(Model):
	"""docstring for User"""
	# def __init__(self, arg):
	# 	super(User, self).__init__()
	# 	self.arg = arg

	_table_ = 'users'

	id = StringField(primary_key = True, default = next_id, ddl = 'varchar(50)')
	email = StringField(ddl = 'varchar(50)')
	passwd = StringField(ddl = 'varchar(50)')
	admin = BooleanField()
	name = StringField(ddl = 'varchar(50)')
	image = StringField(ddl = 'varchar(500)')
	created_at = FloatField(default = time.time)

class Blog(Model):
	"""docstring for Blog"""
	# def __init__(self, arg):
	# 	super(Blog, self).__init__()
	# 	self.arg = arg

	_table_ = 'blog'

	id = StringField(primary_key = True, default = next_id, ddl = 'varchar(50)')
	user_id = StringField(ddl = 'varchar(50)')
	user_name = StringField(ddl = 'varchar(50)')
	user_image = StringField(ddl = 'varchar(500)')
	name = StringField(ddl = 'varchar(50)')
	summary = StringField(ddl = 'varchar(200)')
	content = TextField()
	created_at = FloatField(default = time.time)

class Comment(Model):
	"""docstring for Comment"""
	# def __init__(self, arg):
	# 	super(Comment, self).__init__()
	# 	self.arg = arg
	_table_ = 'blog'
	id = StringField(primary_key = True, default = next_id, ddl = 'varchar(50)')
	blog_id = StringField(ddl = 'varchar(50)')
	user_id = StringField(ddl = 'varchar(50)')
	user_name = StringField(ddl = 'varchar(50)')
	user_image = StringField(ddl = 'varchar(500)')
	content = TextField()
	created_at = FloatField(default = time.time)

		
		
		