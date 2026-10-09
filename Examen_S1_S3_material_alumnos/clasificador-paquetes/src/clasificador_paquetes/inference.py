import csv
from pathlib import Path
import joblib
from .contracts import Entrada, Salida


def leer_csv(ruta: Path) -> list[Entrada]:
    # TODO
    entradas = []

    with open(ruta, mode="r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            entrada = Entrada(**fila)
            entradas.append(entrada)
    if not entradas:
        raise ValueError("CSV sin filas datos.")

    return entradas #lista entradas


def preprocesar(entrada: Entrada) -> list[float]:
    # TODO
    return[
        round(entrada.peso_kg, 1), #redondeamos a un decimal
        entrada.distancia_km
    ]


def cargar_modelo(ruta: Path):
    # TODO
    model = joblib.load(ruta)
    return model

def predecir(entrada: Entrada, modelo) -> Salida:
    # TODO
    caracteristicas = preprocesar(entrada)
    matriz = [caracteristicas]#matriz 2d
    categoria = modelo.predict(matriz)[0]
    probabilidades = modelo.predict_proba(matriz)[0]
    confianza = float(max(probabilidades))

    return Salida(
        id_paquete=entrada.id_paquete,
        categoria=categoria,
        confianza=confianza
    )

def guardar_csv(resultados: list[Salida], ruta: Path) -> None:
    # TODO
    fieldnames=["id_paquete", "categoria", "confianza"]
    with open(ruta, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(fieldnames)#lo de with open y writerow, buscado en internet

        for resultado in resultados:
            escritor.writerow([
                resultado.id_paquete,
                resultado.categoria,
                resultado.confianza,
            ])


def ejecutar(entrada: Path, modelo: Path, salida: Path) -> None:
    # TODO
    paquetes = leer_csv(entrada)
    modelo = cargar_modelo(modelo)

    resultados=[]

    for paquete in paquetes:
        prediccion = predecir(paquete, modelo)
        resultados.append(prediccion)

    guardar_csv(resultados, salida)#guardo en la lista resultados
    
if __name__ == "__main__":
    ejecutar(
        Path("data/raw/paquetes.csv"),
        Path("models/modelo.joblib"),
        Path("resultados.csv"),
    )
