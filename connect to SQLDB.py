import pyodbc 

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ARUPRECI\SQLEXPRESS;'
                      'Database=questionsDB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM dbo.data')


for i in cursor:
    print(i)
    
print(Level)  
