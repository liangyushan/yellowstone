from flask_restful import Api

errors={
    'FBI':{
        'message':'FBI warning',
        'status':403,
    },
    'Not found':{
        'message':'lost',
        'status':404,
    }
}

api = Api(errors=errors,catch_all_404s=True)

def init_api(app):
    api.init_app(app)