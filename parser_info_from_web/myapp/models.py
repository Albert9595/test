from django.db import models


class JobVacancy(models.Model):
    name_vacancy = models.CharField(max_length = 50)
    description = models.CharField(max_length = 50)
    wage = models.CharField(max_length = 50)
    skills = models.CharField(max_length = 50)
    name_job = models.CharField(max_length = 50)
    adress = models.CharField(max_length = 50)
    url = models.CharField(max_length = 50)

    
    def __str__(self):
        return self.wage  
        