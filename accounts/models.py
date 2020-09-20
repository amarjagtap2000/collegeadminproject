from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


select_category = (
        ('open', 'OPEN'),
        ('obc', 'OBC'),
        ('ews', 'EWS'),
        ('sebc', 'SEBC'),
        ('sc', 'SC'),
        ('st', 'ST'),
        ('sbc', 'SBC'),
    )

select_class = (
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

grade = (
    ('a','A'),
    ('b','B'),
    ('c','C'),
    ('d','D')
)



class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    eid = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    reg_no= models.CharField(max_length=100)
    email = models.EmailField()
    mob = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDER_CATEGORY, max_length=2)
    category = models.CharField(max_length=6, choices=select_category, default='OPEN')
    Class = models.CharField(max_length=6, choices=select_class, default='SY')
    branch =models.CharField(max_length=6, choices=select_branch, default='IT')
    #Last_year_maeksheet =models.ImageField()
    #addmission_Feehon s = models.IntegerField()

    def __str__(self):
        return(self.name)


class Result(models.Model):
    stud_id = models.CharField(max_length=20)
    stud_name = models.ForeignKey(Account, on_delete=models.CASCADE, null=True,blank=True)
    stud_reg_no = models.CharField(max_length=20)
    total_marks = models. CharField(max_length=20)
    obtain_marks= models.CharField(max_length=100)
    status = models.BooleanField()
    grade = models.CharField(max_length=6, choices=grade, default='A')

    def __str__(self):
        return (self.stud_name)




