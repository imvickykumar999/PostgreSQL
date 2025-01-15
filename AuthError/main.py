
# pip install psycopg2-binary
import psycopg2

conn = psycopg2.connect(database="vicks",
                        host="127.0.0.1",
                        user="vicky",
                        password="1234",
                        port="5432")

cursor = conn.cursor()
cursor.execute("SELECT * FROM mytable")
    #  WHERE id = 1")

#code
print(cursor.fetchone())

#output
(1, 'A-CLASS', '2018', 'Subcompact executive hatchback')

#code
print(cursor.fetchall())

#output
'''
[(1, 'A-CLASS', '2018', 'Subcompact executive hatchback'),
 (2, 'C-CLASS', '2021', 'D-segment/compact executive sedan'),
 (3, 'CLA', '2019', 'Subcompact executive fastback sedan'),
 (4, 'CLS', '2018', 'E-segment/executive fastback sedan'),
 (5, 'E-CLASS', '2017', 'E-segment/executive sedan'),
 (6, 'EQE', '2022', 'All-electric E-segment fastback'),
 (7, 'EQS', '2021', 'All-electric full-size luxury liftback'),
 (8, 'S-CLASS', '2020', 'F-segment/full-size luxury sedan.'),
 (9, 'G-CLASS', '2018', 'Mid-size luxury SUV, known as the G-Wagen'),
 (10, 'GLE', '2019', 'Mid-size luxury crossover SUV')]
'''

#code
print(cursor.fetchmany(size=3))

#output
'''
[(1, 'A-CLASS', '2018', 'Subcompact executive hatchback'),
 (2, 'C-CLASS', '2021', 'D-segment/compact executive sedan'),
 (3, 'CLA', '2019', 'Subcompact executive fastback sedan')]
'''

###################### Error Solved ##########################

'''
The error indicates that the PostgreSQL user `vicky` is not allowed to log in. This might be because:

1. The `vicky` role does not exist in the PostgreSQL database.
2. The `vicky` role exists but lacks the required login privileges.

---

### **Steps to Fix the Issue**

#### 1. **Log in as the Superuser**
   Log in using the default `postgres` superuser:
   ```cmd
   psql -U postgres
   ```

---

#### 2. **Check if the Role Exists**
   Run the following SQL command to check if the `vicky` role exists:
   ```sql
   \du
   ```
   This will list all roles in PostgreSQL. Look for `vicky` in the list.

---

#### 3. **Create or Update the Role**
   - If the `vicky` role does not exist, create it and give it login privileges:
     ```sql
     CREATE ROLE vicky WITH LOGIN PASSWORD 'your_password';
     ```
   - If the role exists but lacks login privileges, update it:
     ```sql
     ALTER ROLE vicky WITH LOGIN;
     ```
   - Grant privileges to the `vicky` role for the `vicks` database:
     ```sql
     GRANT ALL PRIVILEGES ON DATABASE vicks TO vicky;
     ```

---

#### 4. **Verify Database Ownership**
   Make sure the `vicky` role has ownership or access to the `vicks` database:
   ```sql
   ALTER DATABASE vicks OWNER TO vicky;
   ```

---

#### 5. **Test the Connection**
   Exit `psql`:
   ```sql
   \q
   ```
   Retry running your Python script:
   ```cmd
   python main.py
   ```

---

If the issue persists, let me know, and I'll guide you through further troubleshooting.
'''
