from django.db import models
from django.utils import timezone

# Create your models here.

class Hh_vacancy(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    salary_from = models.CharField(max_length=20,blank=True,null=True)
    salary_to = models.CharField(max_length=20,blank=True,null=True)
    currency = models.CharField(max_length=20,blank=True,null=True)
    gross = models.CharField(max_length=20,blank=True,null=True)
    name = models.CharField(max_length=20,blank=True,null=True)
    area_name = models.CharField(max_length=20,blank=True,null=True)
    responsibility = models.TextField(blank=True,null=True)
    requirement = models.TextField(blank=True,null=True)
    vacancy_id = models.IntegerField(blank=True,null=True)
    employer_name = models.CharField(max_length=30,blank=True,null=True)
    employer_id = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.name + str(self.vacancy_id)

class Vacancy(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    vacancy_id = models.IntegerField(blank=True,null=True)
    salary_from = models.CharField(max_length=20,blank=True,null=True)
    salary_to = models.CharField(max_length=20,blank=True,null=True)
    name = models.CharField(max_length=30,blank=True,null=True)
    responsibility = models.TextField(blank=True,null=True)
    requirement = models.TextField(blank=True,null=True)
    experience = models.CharField(max_length=20,blank=True,null=True)

    def __str__(self):
        return self.name + str(self.vacancy_id)

class Responsibility(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    vacancy_id = models.IntegerField(blank=True,null=True)
    name_list = models.TextField(blank=True,null=True)
    associated = models.TextField(blank=True,null=True)
    description = models.TextField()

    def __str__(self):
        return self.vacancy_id

class Vendors_technologies(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=30,blank=True,null=True)
    full_name = models.CharField(max_length=50,blank=True,null=True)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.full_name

class Vendors_technologies_link(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=30,blank=True,null=True)
    name_vendor_tehn = models.ForeignKey(Vendors_technologies, on_delete=models.CASCADE , related_name='link')

    def __str__(self):
        return self.name


class Requirement(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

class Сompanies(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Basic(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
