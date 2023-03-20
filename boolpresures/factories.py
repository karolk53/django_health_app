import factory
from faker import Factory

faker = Factory.create()

class BloodPressureParametersFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = 'bloodpresures.BloodPressureParameters'

    systolic = factory.LazyAttribute(lambda x: faker.random.randint(80,150))
    diastolic = factory.LazyAttribute(lambda x: faker.random.randint(50,90))