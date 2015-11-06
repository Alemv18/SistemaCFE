from flask import (Blueprint, request) 
import sys
# from models import sesiones
sys.path.insert(0, '~/Users/alemv18/Desktop/Flask-sistema_cfe-master')
import json
import datetime

sesiones = Blueprint('sesiones', __name__ )


@sesiones.route('/iniciar_sesion', methods=['POST'])
def sesion_entrar():
	try:
		email = request.form['email']
		rpe = request.form['rpe']	
		usuario = Usuario.select().where((Usuario.email == email) & (usuario.rpe == rpe))
		if usuario is not None:
			return "Ok!", 200
		else: 
			return "Error!", 404
	except:
			return "Error",404


@sesiones.route('/cerrar_sesion')
def sesion_salir():
	return redirect(url_for('login'))
		
	

