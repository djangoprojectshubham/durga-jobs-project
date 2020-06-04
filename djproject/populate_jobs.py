import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djproject.settings')

import django
django.setup()

from testApp.models import *
from faker import Faker
from random import *
fake=Faker()



def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftittle=fake.choice('Project Manager','Team Leader','Software Engineer')
        feligibility=fake.choice('B.Tech','M.Tech','MCA','Phd')
        faddress=fake.address()
        femail=fake.email()

        hydjobs_record=hydjobs.objects.get_or_create(date=fdate,company=fcompany,tittle=ftittle,eligibility=feligibility,address=faddress,email=femail)
populate(25)
