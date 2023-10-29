
import psycopg2

conn = psycopg2.connect(database="PostgreSQL",
                        host="sqlinjection.mysql.pythonanywhere-services.com",
                        user="imvickykumar999",
                        password="**************",
                        port="5432")

cursor = conn.cursor()
cursor.execute("SELECT * FROM DB_table WHERE id = 1")

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