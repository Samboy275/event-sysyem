import os


class Config:
    SECRET_KEY= os.environ.get("SECRET_KEY")




class DevelopmentConfig(Config):
    DEBUG=True


config = {
    'development' : DevelopmentConfig
}
