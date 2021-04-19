from flask import Flask, request, render_template, Response
from flask_cors import CORS, cross_origin
from wsgiref import simple_server

app = Flask(__name__)
CORS(app)


@app.route('/training', methods=['POST'])
@cross_origin()
def training_route_client():

    try:
        return Response("Training Successfull")
    except ValueError:
        return Response("Error Occured! %s" % ValueError)
    except KeyError:
        return Response("Error Occured! %s" % KeyError)
    except Exception as e:
        return Response("Error Occured! %s" % e)

if __name__ == '__main__':
    # app.run()
    host = '0.0.0.0'
    port = 5000
    httpd = simple_server.make_server(host, port, app)
    httpd.serve_forever()