from flask import Flask
from flask_restplus import Api, Resource

from server.instance import Server

app = Server.app, Server.api

teorema_bd = [
    {'id': 0, 'tittle': 'catetoOposto'},
    {'id': 1, 'tittle': 'catetoAdjacente'}
]

@app.route('/teorema')
class teoremaList(Resource):
    def get(self, ):
        return teorema_bd
