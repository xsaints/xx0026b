import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xx0026_main.settings')

import django
django.setup()


import random
from xx0026_app001.models import AccessRecord, Webpage, Topic
from faker import Faker


fake_gen= Faker()
topics= ['Search', 'Social', 'Marketplace', 'News', 'Games']


def add_topic():
	t= Topic.objects.get_or_create(top_name= random.choice(topics))[0]
	t.save()
	return t


def populate(N=5):
	for entry in range(N):
		top= add_topic()

		fake_url= fake_gen.url()
		fake_date= fake_gen.date()
		fake_name= fake_gen.company()


		webpg= Webpage.objects.get_or_create(xtopic= top, name= fake_name, url= fake_url)[0]


		acc_rec= AccessRecord.objects.get_or_create(name= webpg, date= fake_date)[0]


if __name__ == '__main__':
	populate(10)