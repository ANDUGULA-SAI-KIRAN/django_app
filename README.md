# django

# 🚀 Django Command Reference Guide

## 1. Project Initialization
| Command | Usage | Description |
| :--- | :--- | :--- |
| `django-admin startproject <name> .` | Once per project | Creates management folder. The `.` prevents nested folders. |
| `python manage.py startapp <app_name>` | For every feature | Creates a new app (e.g., `blog`, `users`). |

---

## 2. Database & Migrations


| Command | Description |
| :--- | :--- |
| `python manage.py makemigrations` | Scans `models.py` and creates a "plan" file for DB changes. |
| `python manage.py migrate` | Executes the plan and updates the actual database tables. |
| `python manage.py showmigrations` | Lists all migrations and their status (Applied/Unapplied). |

---

## 3. Server & Development
| Command | Description |
| :--- | :--- |
| `python manage.py runserver` | Starts the local dev server at `http://127.0.0.1:8000`. |
| `python manage.py shell` | Opens a Python terminal with access to your project data. |
| `python manage.py check` | Scans your project for errors without running the server. |

---

## 4. User Management
| Command | Description |
| :--- | :--- |
| `python manage.py createsuperuser` | Creates an admin account to access `/admin`. |
| `python manage.py changepassword <user>`| Resets the password for a specific user. |

---

## 5. Deployment & Production
| Command | Description |
| :--- | :--- |
| `python manage.py collectstatic` | Gathers CSS/JS/Images into one folder for the web server. |
| `python manage.py check --deploy` | Checks settings for security risks before going live. |

---

## 💡 Quick Tips
* **Use `uv`:** If your environment isn't active, use `uv run python manage.py <command>`.
* **Pathing:** Always run `manage.py` commands from the folder containing the `manage.py` file.