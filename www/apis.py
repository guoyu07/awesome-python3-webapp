# apis.py

# coding:utf-8

__author__ = 'zhangchi'

import json, logging, inspect, functools

class APIError(Exception):
	"""docstring for APIError"""
	def __init__(self, error, data = '', message = ''):
		super(APIError, self).__init__(message)
		self.message = message
		self.data = data
		self.error = error

class APIValueError(APIError):
	"""docstring for APIValueError"""
	def __init__(self, field, message = ''):
		super(APIValueError, self).__init__('value:notfound', field, message)
	
class APIResourceNotFoundError(APIError):
	"""docstring for APIResourceNotFoundError"""
	def __init__(self, field, message = ''):
		super(APIResourceNotFoundError, self).__init__('value:notfound', field, message)
		# self.arg = arg
		

class APIPermissionError(APIError):
	"""docstring for APIPermissionError"""
	def __init__(self, message = ''):
		super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)
		# self.arg = arg