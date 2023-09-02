# EN
## YaMDb project.
### Description
The YaMDb project is a platform for creating reviews of various works: books, movies, etc. (API included)

### How to launch a project:

Clone the repository and go to it on the command line:

```
git clone <Repository link>
```

```
cd api_yamdb
```

Create and activate a virtual environment:

```
python -m vev venv
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Install dependencies:
``
pip install -r requirements.txt
``

Perform migrations:

```
python manage.py makemigrations
python manage.py migrate
```

Launch a project:

```
cd api_yamdb/
python manage.py runserver
```

Importing text data:

```
python manage.py load_data
```

# DE
## YaMDb-Projekt.
### Beschreibung
Das YaMDb-Projekt ist eine Plattform für die Erstellung von Rezensionen zu einer Vielzahl von Werken: Büchern, Filmen usw. (Es gibt API drin)

### Wie führe ich ein Projekt aus:

Klonen des Repositorys und navigieren Sie in der Befehlszeile zu dem Repository:

```
git clone <Repository-Referenz>
```

```
cd api_yamdb
```

Virtuelle Umgebung erstellen und aktivieren:

```
python -m vev venv
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Abhängigkeiten festlegen:
```
pip install -r requirements.txt
```

Migrationen durchführen:

```
python manage.py makemigrations
python manage.py migrate
```

Projekt starten:

```
cd api_yamdb/
python manage.py runserver
```

Importieren von Textdaten:

```
python manage.py load_data
```
