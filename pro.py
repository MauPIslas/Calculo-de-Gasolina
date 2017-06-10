import requests
class Combustible:
    def distancia(self,o,d,rendimiento):
        a=requests.get(params={"origins": o, "destinations":d}, url="https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&key=   '"#La key se obtiene enhttps://developers.google.com/maps/web-services/?hl=es-419 al registrar un proyecto"'    ").json()
        print "\n\nLa distancia entre los destinos es: ",a["rows"][0]["elements"][0]["distance"]["text"]
        print "El tiempo estimado de viaje es: ",a["rows"][0]["elements"][0]["duration"]["text"]
        km=a["rows"][0]["elements"][0]["distance"]["text"]
        km=km.split(" ")
        self.km=float(km[0])
        self.combustible= self.km/rendimiento
        magna=self.combustible*16.47
        premium=self.combustible*18.21
        print "\n\nEl combustible necesario para llegar a "+ str(d)+" es de "+str(self.combustible)+"\n\n"
        print "Si el precio de la magna esta en 16.47 pesos gastaras "+ str(magna) +" pesos"
        print "Si el precio de la premium esta en 18.21 pesos gastaras "+str(premium)+" pesos"



print "\t\t\t\t\t\t\t\tServicio 1\n\n"
o=raw_input("Dame el punto de origen: ")
d=raw_input("Dame el destino deseado: ")
rendimiento=float(raw_input("Dame el rendimiento de combustible de tu automovil en km/l: "))
com=Combustible()
com.distancia(o,d,rendimiento)
