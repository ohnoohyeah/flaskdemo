import os
class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'NEVER GIVEUP@peng708'
    MAIL_SERVER=os.environ.get('MAIL_SERVER','mail.sd-tobacco.com.cn')
    MAIL_PORT=int(os.environ.get('MAIL_PORT','25'))
    MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS','true').lower() in ['true','on','1']
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    FLASKY_MAIL_SUBJECT_PREFIX='[FLASKYDEMO]'
    FLASKY_MAIL_SENDER=os.environ.get('FLASKY_MAIL_SENDER')
    FLASKY_ADMIN=os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
    @staticmethod
    def init_app(app):
        pass
    
class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI') or 'mysql://test:test@192.168.239.129/flaskdemo-dev'
class TestingConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI') or 'mysql://test:test@192.168.239.129/flaskdemo-test'

class ProductingConfig(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('SQLALCHEMY_DATABASE_URI') or 'mysql://test:test@192.168.239.129/flaskdemo'
    
config={
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'producting':ProductingConfig,
    'default':ProductingConfig
    }