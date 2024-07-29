# Implementa la API para acceder y actualizar el q_table_global.pkl. Utiliza un framework como FastAPI o Flask.

from fastapi import FastAPI, File, UploadFile
import pickle

app = FastAPI()

#testeo
@app.get("/")
def read_root():
    return {"Hello": "World"}

# Ruta para descargar la q_table global
@app.get("/download_q_table")
async def download_q_table():
    with open('q_table_global.pkl', 'rb') as f:
        q_table = pickle.load(f)
    return q_table

# Ruta para subir y actualizar la q_table global
@app.post("/upload_q_table")
async def upload_q_table(file: UploadFile = File(...)):
    local_q_table = pickle.load(file.file)
    with open('q_table_global.pkl', 'rb') as f:
        global_q_table = pickle.load(f)
    
    # Actualiza el diccionario global con el local
    for state, actions in local_q_table.items():
        if state in global_q_table:
            global_q_table[state] = [max(g, l) for g, l in zip(global_q_table[state], actions)]
        else:
            global_q_table[state] = actions

    with open('q_table_global.pkl', 'wb') as f:
        pickle.dump(global_q_table, f)
    
    return {"status": "Q-table updated successfully"}

# Iniciar la aplicación
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
