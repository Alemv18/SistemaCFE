import requests
import json

url = "http://localhost:5000/"

def crearUsuario():
	print("test crear usuario: ")
	global url
	test_url = url + "api/usuarios/nuevo"
	datos = dict(
	    		rpe='79020',
		    	email="alejandra@gmail.com"
	    		)

	r = requests.post(test_url, data=datos)
	print(r.status_code)
	if (r.status_code == 200):
		print("Exitoso!")
		print(r.content.decode("utf-8"))
	else:
		print("Fracaso!")
		print(r.content.decode("utf-8"))




def login():
	print("Comprobar que se pueda hacer un log in: ")
	global url
	test_url = url + "api/sesiones/login"
	datos = dict(
	    		rpe='79020',
		    	email = 'alejandra@gmail.com'
	    		)
    # r = requests.post(test_url, data=datos)
	print(r.status_code)
	if (r.status_code == 200):
		print("Exitoso!")
		print(r.content.decode("utf-8"))
	else:
		print("Fracaso!")
		print(r.content.decode("utf-8"))


if __name__ == '__main__':
	crearUsuario()
	login()


