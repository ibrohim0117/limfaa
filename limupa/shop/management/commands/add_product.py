import random
from django.core.management.base import BaseCommand
from limupa.shop.models import Product, Detailed, ProductImage, GeneralProductCategory, ProductCategory
from random import choice
from django.utils.text import slugify
from faker import Faker
from time import time


class Command(BaseCommand):
    def handle(self, *args, **options):
<<<<<<< HEAD
        fake = Faker()
        start_time = time()
        for i in range(1, 100):
            title = fake.text(100)
            p = Product.objects.create(
                title=title,
                slug=slugify(title),
                description=fake.text(15),
                category=ProductCategory.objects.all().order_by('?').first(),
                company=Company.objects.all().order_by('?').first()
=======
        for i in range(2):
            general_category = GeneralProductCategory.objects.create(
                title='Laptop'+str(i)
            )
        for j in range(4):
            product_category = ProductCategory.objects.create(
                title='Zoom'+str(j)
            )
        product_all = Product.objects.all()
        for _ in range(1000):
            title = self.faker.sentence(6)

            product = Product.objects.create(
                title=title,
                slug=slugify(title),
                description=self.faker.text()
>>>>>>> origin/main
            )
            image = ProductImage.objects.create(
                product_id=p,
                image='shop/zevs.jpeg',
                is_general=True
            )
<<<<<<< HEAD


            print(f'post {i} has been created')
        end_time = time()
        print('Finished!!!')
        milliseconds = end_time - start_time
        print(f'Time elapsed: {milliseconds} milliseconds')


# class Command(BaseCommand):
#     faker = Faker()
#
#     def handle(self, *args, **options):
#         product_all = Product.objects.all()
#         for _ in range(1000):
#             title = self.faker.sentence(6)
#
#             product = Product.objects.create(
#                 title=title,
#                 slug=slugify(title),
#                 description=self.faker.text(),
#                 category=ProductCategory.objects.all().order_by('?').first(),
#                 company=Company.objects.all().first()
#             )
#             details = Detailed.objects.create(
#                 price=random.randint(200, 10000),
#                 quantity=random.randint(1, 1000),
#                 detail=random.shuffle([15.3, 14.0, 12.0, 16.0]),
#                 color=random.shuffle(Detailed.ProductColor.values),
#                 size=random.shuffle(Detailed.SizeChoices.values)
#             )
#             product_image = ProductImage.objects.create(
#                 is_general=True,
#                 image='zbad5tfbbe5newoz03dw.jpeg'
#             )
#             for i in range(3):
#                 product_image = ProductImage.objects.create(
#                     image='2-laptop-and-monitor.jpg'
#                 )
=======
            product_image = ProductImage.objects.create(
                is_general=True,
                image='zbad5tfbbe5newoz03dw.jpeg'
            )
            for i in range(3):
                product_image = ProductImage.objects.create(
                    image='2-laptop-and-monitor.jpg'
                )
            product.categories.set([choice(product_all) for _ in range(3)])
            product.company.set([choice(product_all) for _ in range(3)])
>>>>>>> origin/main
