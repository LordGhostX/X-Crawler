from django.db import models


class Publication(models.Model):
    author = models.CharField(max_length=30, default="Unknown Author")
    pub_title = models.CharField(max_length=200)
    pub_summary = models.CharField(max_length=200)
    pub_url = models.CharField(max_length=200)
    pub_picture = models.ImageField(blank=True)

    def __str__(self):
        return self.pub_title + self.author


class Lecturer(models.Model):
    name = models.ForeignKey(Publication, on_delete=models.CASCADE)
    email = models.EmailField()
    date_of_birth = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    fields = models.CharField(max_length=200)
    works = models.CharField(max_length=200)
    pictures = models.ImageField()

    def __str__(self):
        return self.name
