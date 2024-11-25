import pymysql
import csv

# MySQL connection details
host = 'localhost'       # e.g., 'localhost' or an IP address
user = 'root'         # e.g., 'root'
password = 'M@123'     # your MySQL password
database = 'portfolioproject'     # your database name
table = 'CovidDeaths'      # your table name

# Path to the CSV file
csv_file_path = 'F:/Great Learning/Great Learning_New_Updated/SQL/DataAnalysis_Projects/Alex playlist01/CovidDeaths.csv'

# Connect to the MySQL server
connection = pymysql.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

try:
    with connection.cursor() as cursor:
        # Open the CSV file
        with open(csv_file_path, mode='r', encoding='utf-8-sig') as file:
            csv_data = csv.reader(file)
            header = next(csv_data)  # Skip the header row

            # Prepare the INSERT INTO SQL query 
            placeholders = ', '.join(['%s'] * len(header))  # Placeholder for each column
            columns = ', '.join(header)  # CSV column headers match the table columns
            sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

            # Insert data row by row
            for row in csv_data:
                cursor.execute(sql, row)

        # Commit the transaction
        connection.commit()
        print(f"Data uploaded successfully into {table}!")

except pymysql.MySQLError as e:
    print(f"Error: {e}")

finally:
    connection.close()
