
import faker 

def generate_random_email():
    fake = faker.Faker()
    return fake.email()

def generate_random_password(length=10):
    fake = faker.Faker()
    return fake.password(length=length)

def generate_random_ad():
    fake = faker.Faker()
    title = fake.sentence(nb_words=6)
    description = fake.text(max_nb_chars=200)
    price = fake.random_number(digits=5)
    return title, description, price
