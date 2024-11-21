from django.db import models


# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes', null=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes', null=True)
    created_date = models.DateTimeField(auto_now_add=True)

class Perfil(models.Model):

    class Sexo:
        masc = 'M'
        fem = 'F'
        outr = 'O'
        CHOICES = (
            (masc, 'Masculino'),
            (fem, 'Feminino'),
            (outr, 'Outro'),
        )


    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos', null=True)
    data_nascimento = models.DateField(null=True)
    sexo = models.CharField(max_length=1, null=True, choices=Sexo.CHOICES)
    cidade = models.CharField(max_length=100, null=True)
    estado = models.CharField(max_length=100, null=True)
    pais = models.CharField(max_length=100, null=True)
    ocupacao = models.CharField(max_length=100, null=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=False, unique=True)