# YaMDb Project

## Überblick
Dieses Repository enthält die Entwicklungsschritte des **YaMDb-API-Projekts** – einer Plattform für Rezensionen zu Werken wie Filmen, Büchern und Musik.

Im Zentrum steht eine REST-API auf Basis von **Django** und **Django REST Framework**, mit der Nutzer:innen:
- Titel und Werke katalogisieren,
- Genres und Kategorien verwalten,
- Rezensionen und Kommentare erstellen,
- Bewertungen (Ratings) für Werke berechnen,
- und sich per rollenbasierter Berechtigung (User/Moderator/Admin) authentifizieren können.

## Repository-Struktur
Das Repository ist in mehrere Projektstände aufgeteilt:

- `YaMDb_v.0.8` – früher Entwicklungsstand.
- `YaMDb_v.09` – erweiterter Stand mit zusätzlicher Infrastruktur/CI-Datei.
- `YaMDb_FInal_Cut` – finaler und vollständigster Stand der API.

Wenn du mit dem Projekt arbeiten möchtest, starte in der Regel mit **`YaMDb_FInal_Cut`**.

## Kernfunktionen (Final Cut)
- JWT-basierte Authentifizierung mit Registrierungs- und Bestätigungsfluss.
- CRUD-Endpunkte für Kategorien, Genres und Titel.
- Rezensionen und Kommentare mit Rechteverwaltung.
- Filterung und Pagination für API-Listen.
- Datenimport über Management-Command (`load_data`) aus CSV-Dateien.
- OpenAPI/Redoc-Dokumentation über statische Spezifikation.

## Schnellstart (lokal)
1. In den finalen Projektordner wechseln:
   ```bash
   cd YaMDb_FInal_Cut/api_yamdb
   ```
2. Virtuelle Umgebung erstellen und aktivieren:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   ```
3. Abhängigkeiten installieren:
   ```bash
   pip install -r ../../YaMDb_FInal_Cut/requirements.txt
   ```
4. Migrationen ausführen:
   ```bash
   python manage.py migrate
   ```
5. Entwicklungsserver starten:
   ```bash
   python manage.py runserver
   ```

## Tests
Die jeweiligen Teilprojekte enthalten eigene Test-Suiten im Ordner `tests/`.

Beispiel für den finalen Stand:
```bash
cd YaMDb_FInal_Cut
pytest
```

## Ziel des Projekts
YaMDb demonstriert den Aufbau einer produktionsnahen REST-API mit Fokus auf:
- saubere Ressourcenmodellierung,
- Zugriffskontrolle und Rollen,
- nachvollziehbare Entwicklungsiterationen,
- und reproduzierbare Projektumgebungen.
