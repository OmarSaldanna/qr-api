import os
from qr import crear_qr
from flask import Flask, request, jsonify

# GET request /qr: json {
# 	"content": "info a meter en el qr"
# }

# answer: json {
# 	"path": "ruta del qr, retornada por la función de crear qr"
# }

# instanciar la api
app = Flask(__name__)

# definir la ruta
@app.route('/', methods=['GET'])
def generate_qr():
	# obtener el json de la request
    data = request.json
    # después del contenido
    content = data.get('content')
    # si no hay contenido
    if not content:
    	# mandar un error
        return jsonify({'error': 'parámetro de content no recibido'})
    # ahora crear el qr
    path = crear_qr(content)
    # y mandarlo como respuesta
    return jsonify({'path': path})


# finalmente ejecutar la app
if __name__ == '__main__':
	# ejecutar la app
	app.run(host=os.environ['HOST'], port=int(os.environ['PORT']))