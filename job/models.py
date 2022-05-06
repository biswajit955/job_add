from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile





class Company(models.Model):
    company_name = models.CharField(max_length=100,help_text="enter within 100 charecter")
    logo = models.FileField(upload_to='logo')
    address = models.CharField(max_length=100,help_text="enter within 100 charecter")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.company_name
    
class Post(models.Model):
    title = models.CharField(max_length=100,help_text="enter within 100 charecter")
    Location = models.CharField(max_length=20, blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    job_function = models.CharField(max_length=100,help_text="enter within 100 charecter")
    key_skills = models.CharField(max_length=100,help_text="enter within 100 charecter")
    vacancies = models.IntegerField()
    job_description =  models.TextField()
    experience = models.CharField(max_length=100,help_text="enter within 100 charecter")
    salary = models.IntegerField()
    educational_qualification = models.CharField(max_length=100,help_text="enter within 100 charecter")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100,help_text="enter within 100 charecter")

    def __str__(self):
        return self.title

    # this is for show demo form admin site (if you use this than genarate a button for demo )
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk' : self.pk})