from django.db import models


class Categoria(models.Model):
<<<<<<< HEAD
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao
=======
      descricao = models.CharField(max_length=100)
       
      def __str__(self):
        return f"{self.id} - {self.descricao}"
>>>>>>> 211d0b8df34754ddad74c8c911ec662da4c2b3f4
