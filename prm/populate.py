import os 
# CONFIGURE THE SETTINGS FOR THE PROJECT
os.environ.setdefault('DJANGO_SETTINGS_MODULE', "prm.settings")

import django
django.setup() # configure settings
import random
from prm_firstapp.models import Salary
from faker import Faker

# create instance of faker

fakegen = Faker()
employees = ['A', 'B', 'C']

def add_employee():
    # pick one of the emloyees randomly
    s = Salary.objects.get_or_create(empid= random.choice(employees))[0] # tuple is returned. 
    print (s)
    #s.save()
    return s


def populate(N=5):
    # N is changeable
    for entry in range (N):
        # get employee id
        #emp = add_employee()
        emp = random.choice(employees)


        # create fake data for that entry
        fake_A = fakegen.random_int()
        print (fake_A)
        fake_B = fakegen.random_int()
        fake_C = fakegen.random_int()
        fakeDate = fakegen.date()
        # create a web page entry
        webpg = Salary.objects.get_or_create(empid = emp, beltA = fake_A, beltB = fake_B, beltC= fake_C, makingDate = fakeDate)[0]
        print (webpg)
if __name__ == '__main__':
    print('populating the database')
    populate(5)
    print ("populating complete")
          