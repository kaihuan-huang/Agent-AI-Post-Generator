## OPEN API 
OPENAI_API_KEY = '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'



## FLASK 
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}