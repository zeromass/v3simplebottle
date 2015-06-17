__author__ = 'spousty'


from bottle import route

@route('/')
def index(name):
    return "hello OpenShift Guru"