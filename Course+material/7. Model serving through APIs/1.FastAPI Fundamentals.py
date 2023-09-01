
# 1. Library imports
import uvicorn
from fastapi import FastAPI

# 2. Créez l'objet app
app = FastAPI()

# 3. Index de la route, s'ouvre automatiquement sur http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, stranger'}

# 4. Route avec un seul paramètre, renvoie le paramètre dans un message
# Situé à: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'message': f'Hello, {name}'}


@app.post('/students')
def savestudents(name: str, lastname: str):
    return f"Etudiant {name} {lastname} enregistré"





# 5. Exécutez l'API avec uvicorn
# Fonctionnera sur http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)