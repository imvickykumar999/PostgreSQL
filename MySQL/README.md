## Django MySQL

```py
# /toggle_project/toggle_project/__init__.py
import pymysql
pymysql.install_as_MySQLdb()

# /toggle_project/toggle_project/settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'toggle',     # Ensure this matches the created database
        'USER': 'Vicky',
        'PASSWORD': 'abcd4321H',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

User `Vicky` has:

1. **USAGE** privileges on all databases (a minimal level of access with no specific privileges).
2. **ALL PRIVILEGES** on the `sampleproject` database.

However, `Vicky` does not have privileges on the `toggle` database, which is why you're seeing the "Access denied" error.

### Steps to Fix the Issue
You need to explicitly grant `ALL PRIVILEGES` on the `toggle` database to `Vicky`.

---

### 1. **Log in as a User with Higher Privileges**
You need to use a MySQL user that has the required privileges to grant permissions. Typically, this will be the `root` user.

Log in as the `root` user:
```bash
sudo mysql -u root -p
```

---

### 2. **Grant Privileges for the `toggle` Database**
Run the following SQL command to grant privileges for the `toggle` database to `Vicky`:
```sql
CREATE DATABASE toggle;
GRANT ALL PRIVILEGES ON toggle.* TO 'Vicky'@'127.0.0.1';
FLUSH PRIVILEGES;
```

- The `GRANT` command assigns `ALL PRIVILEGES` on the `toggle` database to the user `Vicky` when connecting from `127.0.0.1`.
- The `FLUSH PRIVILEGES` ensures the changes are applied immediately.

---

### 3. **Verify the Privileges**
After granting privileges, verify that `Vicky` now has access to the `toggle` database:
```sql
SHOW GRANTS FOR 'Vicky'@'127.0.0.1';
```

You should now see:
```plaintext
GRANT ALL PRIVILEGES ON toggle.* TO 'Vicky'@'127.0.0.1';
```

---

### 4. **Test the Connection**
1. Log out from MySQL:
   ```sql
   EXIT;
   ```
2. Log in as the user `Vicky`:
   ```bash
   mysql -u Vicky -p -h 127.0.0.1 -P 3306
   ```
3. Confirm that you can access the `toggle` database:
   ```sql
   SHOW DATABASES;
   USE toggle;
   ```
