import requests

def obtener_distancia_tiempo_combustible(ciudad_origen, ciudad_destino):
    api_token = "FwIwn918Su0avjSLC16PaadfS1g7vtlX"
    url = f"https://www.mapquestapi.com/directions/v2/route?key={api_token}&from={ciudad_origen}&to={ciudad_destino}"

    response = requests.get(url)
    data = response.json()

    if data['info']['statuscode'] == 0:
        distancia = data['route']['distance']
        tiempo = data['route']['time']
        combustible = data['route']['fuelUsed']
        
        distancia_km = distancia * 1.60934  # Convertir millas a kilómetros
        tiempo_horas = tiempo / 3600  # Convertir segundos a horas
        combustible_litros = combustible * 3.78541  # Convertir galones a litros

        print(f"Distancia entre {ciudad_origen} y {ciudad_destino}: {distancia_km:.2f} km")
        print(f"Duración del viaje: {int(tiempo_horas)} horas, {(tiempo_horas % 1) * 60:.0f} minutos, {(tiempo_horas % 1) * 3600 % 60:.0f} segundos")
        print(f"Combustible requerido: {combustible_litros:.2f} litros")
        print("Narrativa del viaje:")
        print(f"Viaje desde {ciudad_origen} hasta {ciudad_destino}.")

    else:
        print("No se pudo obtener la información de la ruta.")

def main():
    while True:
        ciudad_origen = input("Ingrese la ciudad de origen (o 'q' para salir): ")
        if ciudad_origen.lower() == 'q':
            break
        ciudad_destino = input("Ingrese la ciudad de destino: ")
        obtener_distancia_tiempo_combustible(ciudad_origen, ciudad_destino)

if __name__ == "__main__":
    main()
