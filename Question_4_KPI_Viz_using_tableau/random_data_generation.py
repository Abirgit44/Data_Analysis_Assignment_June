import pandas as pd  #importing all the necessary libraries to generate the data
import numpy as np
from faker import Faker
import random

#now we have to initialize faker for generating random names and other details
fake = Faker('en_IN')

#setting seed for reproducibility
random.seed(42)
np.random.seed(42)

#Number of records
num_records = 1000

#now generation of data
data = {
        'Employee ID': [fake.unique.uuid4() for _ in range(num_records)],
        'Name': [fake.name() for _ in range(num_records)],
        'Department': [random.choice(['IT', 'HR', 'Sales', 'Finance', 'Marketing', 'Operations', 'Customer Support']) for _ in range(num_records)],
        'City': [random.choice(['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata', 'Hyderabad', 'Pune']) for _ in range(num_records)],
        'Employment Date': [fake.date_between(start_date='-10y', end_date='today') for _ in range(num_records)],
        'Salary': [round(random.uniform(30000, 120000), 2) for _ in range(num_records)],
        'Gender': [random.choice(['Male', 'Female']) for _ in range(num_records)],
        'Age': [random.randint(22, 60) for _ in range(num_records)],
        'Performance Score': [random.randint(1, 10) for _ in range(num_records)],
        'Projects Completed': [random.randint(0, 20) for _ in range(num_records)],
        'Overtime Hours': [random.randint(0, 50) for _ in range(num_records)]
}


#creating a dataframe
df = pd.DataFrame(data)

#display
print(df.head())


#Saving to CSV
df.to_csv('employee_data.csv', index=False)
