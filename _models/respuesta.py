from __init__ import *

class Respuesta(Model):
    usuario = ForeignKeyField(Usuario)
    pregunta = ForeignKeyField(Pregunta)
    respuesta = BooleanField()

    class Meta:
        database = DATABASE

    @classmethod
    def nueva(cls, usuario, pregunta, respuesta):
        cls.create(
            usuario=usuario,
            pregunta=pregunta,
            respuesta=respuesta
        )

    def to_json(self):
        return {
            "respuesta" : self.respuesta
        }
    def get_respuestas(self):
        respuestas = Respuesta.select().where(Respuesta.pregunta == self.id)
        return respuestas

    def __repr__(self):
        return self.pregunta
