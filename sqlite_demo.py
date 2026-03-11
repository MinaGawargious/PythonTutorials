# SQLLite is useful when we need database functionality but don't want to spin up a database like MYSQL or PostGres. SQLLite is good for small-medium apps where database lives on disk, or testing/prototyping an app before porting it over. DB can be simple file or in-memory DB that lives in RAM
import sqlite3

# connection = sqlite3.connect("employee.db")
connection = sqlite3.connect(":memory:") # connection object that represents our database. Pass in :memory: for in-memory DB. Create file if it doesn't exist. If it does, just connect. Memory gives us fresh clean database each run

cursor = connection.cursor() # Cursor lets us execute commands

# Run once. If run again, we get sqlite3.OperationalError: table employees already exists
cursor.execute("""CREATE TABLE employees (
                first text,
                last text,
                pay integer
                )""") # 5 different data types: null, integer, real, text, and blob (stored exactly as input)

cursor.execute("INSERT INTO employees VALUES ('Mina', 'Gawargious', 100000)")
cursor.execute("INSERT INTO employees VALUES ('Mary', 'Gawargious', 100000)")
# connection.commit()

cursor.execute("SELECT * FROM employees WHERE last='Gawargious'")
print(cursor.fetchall()) # fetchmany(n) or fetchall()

connection.commit() # saves/commits current transaction

from employee import Employee
emp1 = Employee("John", "Doe", 80000)
emp2 = Employee("Jane", "Doe", 90000)

# String formatting is bad practice with databases. This is vulnerable to SQL injection attacks
cursor.execute(f"INSERT INTO employees VALUES ('{emp1.first}', '{emp1.last}', {emp1.pay})")
cursor.execute(f"INSERT INTO employees VALUES (?, ?, ?)", (emp2.first, emp2.last, emp2.pay))# Use ? as a DB API placeholder. No quotes needed either as it can tell based on values. Pass in tuple of values (even if we have 1 value)
connection.commit()

cursor.execute(f"INSERT INTO employees VALUES (:first, :last, :pay)", {"first": emp2.first, "last": emp2.last, "pay": emp2.pay})
connection.commit()

cursor.execute("SELECT * FROM employees WHERE last=?", ("Doe",)) # commma needed to indicate tuple
print("select with ?:", cursor.fetchall())

cursor.execute("SELECT * FROM employees WHERE last=:last", {"last": "Doe"})
print("select with dict:", cursor.fetchall())

def insert_emp(emp):
    # In SQLLite, connection objects can be used as context managers to automatically commit upon teardown/exit of with statement. If there's an exception, changes are rolled back
    with connection:
        cursor.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def get_emps_by_name(lastname):
    # SELECT statements don't need to be comitted, so no need to be within context manager
    cursor.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return cursor.fetchall()

def update_pay(emp, pay):
    with connection:
        cursor.execute("""UPDATE employees SET pay = :pay WHERE first = :first AND last = :last""", {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with connection:
        cursor.execute("DELETE from employees WHERE first = :first AND last = :last", {'first': emp.first, 'last': emp.last})
        
emp3 = Employee("Jill", "Doe", 100000)
insert_emp(emp3)
emps = get_emps_by_name("Doe")
print(emps)

update_pay(emp3, "120000")
emps = get_emps_by_name("Doe")
print(emps)

remove_emp(emp3)
emps = get_emps_by_name("Doe")
print(emps)
        
connection.close()