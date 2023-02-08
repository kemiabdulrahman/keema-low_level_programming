import random
import csv
import json
import sqlite3
import names
from datetime import datetime, timedelta

# Generate 50 random names and their details
def generate_data():
    data = []
    for i in range(50):
        name = names.get_full_name()
        address = f"{random.randint(1, 100)} Main St, {names.get_last_name()}ville, {random.choice(['NY', 'CA', 'FL', 'TX'])} {str(random.randint(10000, 99999))}"
        phone = f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
        dob = (datetime.now() - timedelta(days=365*random.randint(18,80))).strftime("%Y-%m-%d")
        data.append([name, address, phone, dob])
    return data

# Store the data in a CSV file
def to_csv(data):
    with open("people.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Address", "Phone", "DOB"])
        writer.writerows(data)
    print("Data saved to people.csv")

# Store the data in a JSON file
def to_json(data):
    with open("people.json", "w") as f:
        json.dump(data, f)
    print("Data saved to people.json")

# Store the data in a SQL database
def to_sql(data):
    conn = sqlite3.connect("people.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS people (
            name text,
            address text,
            phone text,
            dob text
        )
    """)
    c.executemany("INSERT INTO people VALUES (?,?,?,?)", data)
    conn.commit()
    conn.close()
    print("Data saved to people.db")

data = generate_data()
to_csv(data)
to_json(data)
to_sql(data)

