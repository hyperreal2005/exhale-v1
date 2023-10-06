from flask import Flask 
from flask_socketio import SocketIO




def create_app():
    app=Flask(__name__, static_url_path='/static')
    app.config['SECRET_KEY']='C4C'
    socketio = SocketIO(app)
    @socketio.on('message')
    def handle_message(message):
        socketio.emit('message',message)
    

    


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app



