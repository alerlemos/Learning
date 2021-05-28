import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

# Fake population script
import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):

        # Create the fake data for that entry
        fakename = fakegen.name().split()
        fake_first_name = fakename[0]
        fake_last_name = fakename[1]
        fake_email = fakegen.email()

        # Create the new User entry
        usr = User.objects.get_or_create(first_name = fake_first_name, last_name = fake_last_name, email = fake_email)[0]



if __name__ == '__main__':
    print("Populating: runing script!")
    populate(20)
    print("Populating complete!")