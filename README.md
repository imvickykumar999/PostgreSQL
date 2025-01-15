To use PostgreSQL as the database in your Django project instead of the default SQLite, follow these steps:

---

### **1. Install the PostgreSQL Driver**
Install the `psycopg2` library, which allows Django to connect to PostgreSQL:
```bash
pip install psycopg2-binary
```

---

### **2. Update the `DATABASES` Configuration in `settings.py`**
Open your Django project's `settings.py` file and modify the `DATABASES` configuration as follows:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',  # Replace with your PostgreSQL database name
        'USER': 'your_postgres_username',  # Replace with your PostgreSQL username
        'PASSWORD': 'your_postgres_password',  # Replace with your PostgreSQL password
        'HOST': '127.0.0.1',  # Use 'localhost' or your database server's IP
        'PORT': '5432',  # Default PostgreSQL port
    }
}
```

---

### **3. Create the PostgreSQL Database**
Before running your Django project, ensure the PostgreSQL database is created:
1. Open the `psql` shell:
   ```bash
   psql -U postgres
   ```
2. Create the database:
   ```sql
   CREATE DATABASE your_database_name;
   ```
3. Grant privileges to your user:
   ```sql
   GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_postgres_username;
   ```

---

### **4. Apply Migrations**
Run Django migrations to set up the database schema in PostgreSQL:
```bash
python manage.py makemigrations
python manage.py migrate
```

---

### **5. Test the Configuration**
Run the Django development server to ensure everything is working:
```bash
python manage.py runserver
```

If everything is configured correctly, Django will now use PostgreSQL instead of SQLite.

---

### **6. Optional: Install pgAdmin (GUI Tool)**
If you prefer a GUI to manage your PostgreSQL database, you can install pgAdmin:
- Download from [pgAdmin's official website](https://www.pgadmin.org/).
- Use it to manage your PostgreSQL database visually.
