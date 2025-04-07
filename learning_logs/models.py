from django.db import models

# Create your models here.

class Topic(models.Model):
    """Assunto que o usuário está aprendendo."""
    text = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Devolve uma string representando o modelo."""
        return self.text
