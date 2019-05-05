import os
class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'NEVER GIVEUP@peng708'
    @staticmethod
    def init_app(app):
        pass
config={}