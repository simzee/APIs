# config.py

class Config(object):
	"""
	Common configurations
	"""

	# Put any configurations here that are common across all environments

class DevelopmentConfig(Config):
	"""
	Development configurations
	"""

	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://word:sentence@172.16.2.27:5432/blog_api_db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
	"""
	Production configurations
	"""

	DEBUG = False


app_config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig
}
