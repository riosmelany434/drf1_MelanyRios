from django.db import models

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Curso(models.Model):
    nombrecurso = models.CharField(max_length=100)
    annio = models.IntegerField()  

    def __str__(self):
        return f"{self.nombrecurso} ({self.annio})"

class Matricula(models.Model):
    codigo = models.CharField(max_length=50)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True, blank=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True, blank=True)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Matrícula: {self.codigo}"