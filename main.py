from fastapi import FastAPI

app = FastAPI()

donnees = {
    'lieux': [
        'Paris',
        'Lyon',
        'Marseille',
        'Montpellier',
        'Toulon',
        'Lilles',
        'Nantes']
}

@app.get("/lieux")
async def get_lieux():
    # renvoyer nos données et 200 code OK
    return {'donnees': donnees}