from faker import Faker

fake = Faker()
fake_ru = Faker('ru_RU')


def generate_name():
    return fake_ru.first_name()


def generate_email():
    return f'nikolay_zhuravlev_26fs{fake.numerify("###")}@{fake.domain_name()}'


def generate_password(length=6):
    return fake.password(length=length)
