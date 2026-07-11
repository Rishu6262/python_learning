from faker import Faker
import random
import pandas as pd

data = []
fake = Faker("en_IN")

print(f"{'ID':<6} {'Name':<25} {'Email':<30} {'Phone':<15} {'Company':<25} {'Date':<12} {'Fake Aadhaar':<15} {'Salary'}")
print("-"* 100)

for i in range (100):
  for i in range(100):
    data.append({
        "stu_ID": random.randint(1000, 9999),
        "Name": fake.name(),
        "Email": fake.email(),
        "Phone": fake.phone_number(),
        "Company": fake.company(),
        "Joining_Date": fake.date_between(start_date='-3y', end_date='today'),
        "Fake_Aadhaar": "".join(str(random.randint(0, 9)) for _ in range(12)),
        "Salary": random.randint(25000, 200000)
    })
df = pd.DataFrame(data)
print(df.head())
df.to_csv("student_dataset.csv", index=False)

print("CSV Saved Successfully!")
