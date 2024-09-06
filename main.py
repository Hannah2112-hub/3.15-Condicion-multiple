class Estudiante:
    def __init__(self, calificacion, asistencia):
        self.calificacion = calificacion
        self.asistencia = asistencia

    def evaluar_calificacion(self):
        if self.calificacion > 9.0 and self.asistencia == 1:
            return "La calificación es A Excelente con Mención Honorífica."
        elif self.calificacion > 9.0 and self.asistencia != 1:
            return "La calificación es A Excelente."
        elif self.calificacion > 8.0 and self.asistencia == 1:
            return "La calificación es B Muy bien con Mención."
        elif self.calificacion > 8.0 and self.asistencia != 1:
            return "La calificación es B Muy bien."
        elif self.calificacion == 7.5:
            return "La calificación es C Bien."
        else:
            return "La calificación es R Reprobado. Lo siento mucho."

calificacion = float(input("Dame una calificación: \n"))
asistencia = int(input("Dame la asistencia: 1 sí asistió o 0 si no asistió.\n"))

estudiante = Estudiante(calificacion, asistencia)

print(estudiante.evaluar_calificacion())
