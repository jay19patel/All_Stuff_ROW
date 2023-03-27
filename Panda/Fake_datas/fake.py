from faker import Faker
import random
import csv

# create fake data for 100 students
fake = Faker()
students = []
for i in range(50):
    name = fake.name()
    email= fake.email()
    phone =fake.phone_number()
    bio = random.randint(50, 100)
    maths = random.randint(50, 100)
    physics = random.randint(50, 100)
    chemistry = random.randint(50, 100)
    students.append([name, email, phone, bio,maths,physics,chemistry])
    
# write the data to a CSV file
with open("rowdata.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "email", "phone", "bio","maths","physics","chemistry"])
    writer.writerows(students)



# GENERATE FAKE DATAS 