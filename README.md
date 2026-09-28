# CampusNotes - Django Full-Stack Project

## 1. Open the project
Extract this ZIP and open the `college_notes_app` folder in VS Code.

## 2. Open VS Code Terminal

Windows:
```powershell
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

If `py` does not work, use:
```powershell
python -m venv venv
venv\Scripts\activate
```

## 3. Create database tables

```powershell
python manage.py makemigrations
python manage.py migrate
```

## 4. Create admin account

```powershell
python manage.py createsuperuser
```

Enter a username, email (optional), and password.

## 5. Start the website

```powershell
python manage.py runserver
```

Open the address shown in the terminal, normally:
http://127.0.0.1:8000/

## 6. Test
- Home: /
- Sign up: /signup/
- Login: /login/
- Upload: /upload/
- My notes: /my-notes/
- Bookmarks: /bookmarks/
- Admin: /admin/

## Important
- Uploaded files are stored in the `media/` folder.
- The database is `db.sqlite3` and is created after `migrate`.
- This is a development/college-project setup. Before public deployment, change SECRET_KEY, DEBUG, ALLOWED_HOSTS and configure secure file storage.
