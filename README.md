# 🎲 Fake Student & Employee Dataset Generator using Python

## 📌 Project Overview

This project generates a **realistic fake dataset** using Python. It creates synthetic records containing names, email addresses, phone numbers, company names, joining dates, fake Aadhaar-like numbers, and salaries. The generated data is stored in a CSV file, making it useful for learning, testing, and practicing data analysis or machine learning without exposing any real personal information.

> **Note:** This project generates **fake data only**. The Aadhaar-like numbers are randomly generated 12-digit values and are **not real Aadhaar numbers**.

---

# 📂 Project Structure

```
Fake_Dataset_Generator/
│
├── dataset_generator.py
├── student_dataset.csv
├── README.md
└── requirements.txt
```

---

# 🚀 Features

* Generate 100 or more fake records
* Indian names using Faker (`en_IN`)
* Random Employee/Student IDs
* Fake Email Addresses
* Fake Phone Numbers
* Fake Company Names
* Random Joining Dates
* Fake Aadhaar-like Numbers
* Random Salary (₹25,000 – ₹2,00,000)
* Export dataset to CSV
* Easy to customize

---

# 🛠 Technologies Used

* Python 3.x
* Faker
* Pandas
* Random

---

# 📦 Required Libraries

Install the required libraries before running the project.

```bash
pip install faker pandas
```

---

# 📖 Libraries Explanation

## Faker

Faker is used to generate realistic fake information.

Examples:

* Name
* Email
* Phone Number
* Company
* Address
* Date
* City
* Country

Example:

```python
fake.name()
fake.email()
fake.phone_number()
```

---

## Random

The `random` module generates random numerical values.

Used for:

* Student ID
* Salary
* Fake Aadhaar Number

Example:

```python
random.randint(1000, 9999)
```

---

## Pandas

Pandas converts Python dictionaries into a DataFrame and exports them to CSV.

Example:

```python
df = pd.DataFrame(data)
df.to_csv("student_dataset.csv", index=False)
```

---

# 📊 Dataset Columns

| Column       | Description                           |
| ------------ | ------------------------------------- |
| stu_ID       | Random ID                             |
| Name         | Fake Indian Name                      |
| Email        | Fake Email Address                    |
| Phone        | Fake Mobile Number                    |
| Company      | Fake Company Name                     |
| Joining_Date | Random Joining Date                   |
| Fake_Aadhaar | Random 12-digit Number (Testing Only) |
| Salary       | Random Salary in INR                  |

---

# ▶️ How to Run

### Step 1

Clone the repository.

```bash
git clone https://github.com/Rishu6262/python_learning.git
```

### Step 2

Open the project folder.

```bash
cd python_learning
```

### Step 3

Install dependencies.

```bash
pip install faker pandas
```

### Step 4

Run the Python script.

```bash
python dataset_generator.py
```

---

# 📄 Output

After execution, a CSV file will be generated.

```
student_dataset.csv
```

Example:

| stu_ID | Name         | Email                                     | Phone          | Company          | Joining_Date | Fake_Aadhaar | Salary |
| -----: | ------------ | ----------------------------------------- | -------------- | ---------------- | ------------ | ------------ | -----: |
|   1234 | Rahul Sharma | [rahul@gmail.com](mailto:rahul@gmail.com) | +91 9876543210 | ABC Pvt Ltd      | 2024-01-20   | 583920174615 |  75000 |
|   5678 | Priya Verma  | [priya@gmail.com](mailto:priya@gmail.com) | +91 9123456789 | XYZ Technologies | 2023-06-18   | 903412678145 |  95000 |

---

# ⚙️ Customization

Increase the number of generated records:

```python
for i in range(1000):
```

Change salary range:

```python
random.randint(30000, 500000)
```

Generate US data:

```python
fake = Faker("en_US")
```

Generate UK data:

```python
fake = Faker("en_GB")
```

---

# 📈 Applications

This project can be used for:

* Python Practice
* Pandas Practice
* CSV File Generation
* Machine Learning Datasets
* Data Cleaning
* Data Visualization
* Power BI Practice
* SQL Practice
* Database Testing
* API Testing
* Software Testing
* Automation Projects

---

# 💡 Future Improvements

* Generate addresses
* Generate city and state
* Add gender
* Add date of birth
* Add department
* Add job title
* Add age
* Export to Excel
* Export to JSON
* Add Streamlit user interface
* Connect with SQLite or MySQL

---

# 📚 Learning Outcomes

After completing this project, you will understand:

* Python loops
* Python dictionaries
* Random module
* Faker library
* Pandas DataFrame
* CSV file handling
* Data generation
* Dataset creation
* File exporting

---

# 📜 License

This project is released for educational and learning purposes.

The generated dataset contains **synthetic (fake) data only** and should not be treated as real personal information.

---

## Conclusion

The **Fake Student & Employee Dataset Generator** is a simple Python project that creates realistic fake data using the **Faker**, **Random**, and **Pandas** libraries. It generates synthetic records such as names, emails, phone numbers, company names, salaries, and joining dates, then stores them in a CSV file. This project helps beginners practice Python programming, data handling, and CSV file operations. The generated dataset can be used for data analysis, machine learning, SQL, and software testing without using real personal information. Overall, it is a useful project for learning and can be easily extended with additional features in the future.

---

# 👨‍💻 Author

**Rishu Gurjar**

GitHub: https://github.com/Rishu6262

---

Linkedin : https://www.linkedin.com/in/rishu-gurjar-58072a333/

Python • Data Analysis • Machine Learning • AI

---

