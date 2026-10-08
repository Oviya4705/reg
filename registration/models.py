from django.db import models


class Registration(models.Model):

    # Personal Details
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    dob = models.DateField()

    # Other Details
    website = models.URLField()
    state = models.CharField(max_length=100)
    languages = models.TextField()
    gender = models.CharField(max_length=20)
    skills = models.TextField()
    experience = models.IntegerField()

    # File Uploads
    photo = models.ImageField(
        upload_to='photos/',
        blank=True,
        null=True
    )

    resume = models.FileField(
        upload_to='resumes/',
        blank=True,
        null=True
    )

    audio = models.FileField(
        upload_to='audio/',
        blank=True,
        null=True
    )

    video = models.FileField(
        upload_to='videos/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name