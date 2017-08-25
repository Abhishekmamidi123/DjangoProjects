# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProTwo.settings')
# import django
# django.setup()
#
# import random
# from appTwo.models import User
# from faker import Faker
#
# fakegen = Faker()
#
# def addUser(N=5):
#     for i in range(N):
#         fake_name = fakegen.name().split()
#         fake_first_name = fake_name[0]
#         fake_last_name = fake_name[1]
#         fake_email = fakegen.email()
#
#         user = User.objects.get_or_create(FirstName=fake_first_name,
#                                           LastName=fake_last_name,
#                                           Email=fake_email)[0]
#
# if __name__ == '__main__':
#     print "populating script"
#     addUser(20)
#     print "populating complete"
import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
# Import settings
django.setup()

import random
from appTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    '''
    Create N Entries of Dates Accessed
    '''

    for entry in range(N):

        # Create Fake Data for entry
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        # Create new User Entry
        user = User.objects.get_or_create(FirstName=fake_first_name,
                                          LastName=fake_last_name,
                                          Email=fake_email)[0]


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(20)
    print('Populating Complete')
