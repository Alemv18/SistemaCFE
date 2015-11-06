from __init__ import *

class Pregunta(Model):
    competencia = ForeignKeyField(Competencia)
    pregunta = CharField(max_length=500)

    class Meta:
        database = DATABASE

    @classmethod
    def nueva(cls, competencia, pregunta):
        cls.create(
                competencia=competencia,
                pregunta=pregunta
        )
    def to_json(self):
        return {
            "pregunta" : self.pregunta
        }
    def get_pregunta(self):
       preguntas = Pregunta.select().where(Pregunta.pregunta == self.id)
        return preguntas

   