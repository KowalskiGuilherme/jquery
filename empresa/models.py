from django.db import models


class Empresa(models.Model):
    verba = models.FloatField()
    title = models.CharField(max_length=30)
    last_updated = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='empresas')

    def __str__(self):
        return self.title
