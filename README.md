# Corso FastAPI - Esercizio CRUD Base

Un piccolo progetto per imparare a muovere i primi passi con FastAPI, gestendo la validazione dei dati tramite Pydantic e testando le rotte HTTP.

## Cosa fa questo progetto?
Il progetto utilizza un unico file (`main_2.py`) per esporre due endpoint principali:
- **POST `/items/`**: Per creare un nuovo articolo, con validazione automatica dei campi (il prezzo deve essere maggiore di zero) e calcolo opzionale della tassa (`price_with_tax`).
- **PUT `/items/{item_id}`**: Per aggiornare un articolo esistente combinando parametri di percorso (`item_id`), query string opzionali (`q`) e dati nel corpo della richiesta.

## Requisiti e Installazione
Il progetto richiede Python e le seguenti dipendenze principali (elencate nel file `requirements.txt`):
- `fastapi`
- `uvicorn`

Puoi installarle con il comando:
```bash
pip install -r requirements.txt

```

## Come avviare il progetto
Per avviare il progetto, esegui il comando:
```bash
poetry run uvicorn main_2:app --reload
```

## Come testare le API
Una volta avviato il server, puoi aprire il browser e andare su:
- http://127.0.0.1:8000/docs per visualizzare la documentazione delle API.
- http://127.0.0.1:8000/redoc per visualizzare la documentazione delle API in modalità read-only.
