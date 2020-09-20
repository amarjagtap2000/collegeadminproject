from django.db import models
from django.contrib.auth.models import User



elect_class = (
    ('sy','SY'),
    ('ty','TY'),
    ('b tech','Btech'),
)

select_branch = (
    ('ce','CE'),
    ('it','IT'),
    ('cse','CSE'),
    ('prod','PROD'),
    ('me','ME'),
    ('text','Text'),
    ('ee','EE')
)


GENDER_CATEGORY = (
    ('M','Male'),
    ('F','Female'),
    ('O','Other')
)
# Create your models here.
class Staff(models.Model):

    eid = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=100)
    email = models.EmailField()
    mob = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CATEGORY, max_length=2)



    def __str__(self):
        return(self.firstname)



