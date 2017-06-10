#servicio dos, calculo del punto donde se acaba la gas + busqueda de gasolineras
import requests
class Agotamiento():
    def punto_de_alerta_de_combustible_bajo(self,rendimieto,captanque,tanque):

        self.combustible= captanque*tanque #con esta opercion se cuanta gasolina tiene cualquier carro
        self.agotamiento=self.combustible*rendimieto#con esta opercaion se cuantos kilometros podre avanzar con dicho combustible calculado
        suma=0
        o=raw_input("Dame el punto de origen: ")
        d=raw_input("Dame el destino deseado: ")
        #pido el origen y destino para despues mandarlo como parametro a la api de google directions
        a=requests.get(params={"origin": o, "destination":d}, url="https://maps.googleapis.com/maps/api/directions/json?key=   '"#La key se obtiene enhttps://developers.google.com/maps/web-services/?hl=es-419 al registrar un proyecto"'   ").json()
        lista=a["routes"][0]["legs"][0]["steps"]# ingreso a todas las direcciones
        #utilizo el for para entrar en cada direccion que me da la api
        for x in lista:
            #se necesitara la longitud y latitud para despues de que bote la suma siendo mayor al kilometraje que el auto puede avanzar, estos se guarden y se pasen a la siguiente api (google places)
            latitud=x["start_location"]["lat"]
            longitud=x["start_location"]["lng"]
            #por cada senalamiento de direccion que me de la api, esta contiene el valor en metros o kilometros
            #dis sera el valor en kilometros o metros, se utilizara el split para ver en que unidad lo esta dado
            dis=x["distance"]["text"]
            dis=dis.split(" ")
            if dis[1]== "m":
                #dis tuvo un valor en m, por lo tanto se convierte en kilometros y se sigue la suma
                dis=float(dis[0])/1000
                if self.agotamiento<suma: #checa si la suma no ha pasado la cantidad de kilometros que puede avanzar el auto
                    break #si paso la suma, hace un break para terminar el proceso
                suma+=dis #si no ha pasado la suma, suma dis a suma
            else: #dis obtuvo un valor en kilometros
                dis=float(dis[0])
                if self.agotamiento<suma:#checa si la suma no ha pasado la cantidad de kilometros que puede avanzar el auto
                    break#si paso la suma, hace un break para terminar el proceso
                suma+=dis#si no ha pasado la suma, suma dis a suma
        if suma<self.agotamiento: #si al terminar la suma no paso el agotamiento manda el mensaje
            print "ALcanzas a llegar a tu destino sin poblemas"
        else: #si la suma paso al agotamiento de la gasolina, me otorga la latitud y longitud obtenida anteriormente y las junta en una variable
            self.latlng=str(latitud)+","+str(longitud)
            print "Las coordenadas son: "+str(self.latlng)+" se esta buscando las gasolineras mas cercanas al punto de alerta de combustible"
            ago.places(self.latlng)#mando a llamar a la funcion con la api de places pasandole la latitud y longitud en la cual el coche tendra un rango de 20 km antes de quedarse barado
    def places(self,latlng):
        a=requests.get(params={"query":"gasolineras","location":latlng,"radius":"10000","key":"La key se obtiene en https://developers.google.com/maps/web-services/?hl=es-419 al registrar un proyecto"}, url="https://maps.googleapis.com/maps/api/place/textsearch/json").json()
        print"\n\n\n"
        print("La primera gasolinera mas cercana es:")
        print a["results"][0]["formatted_address"]
        print("La segunda gasolinera mas cercana es:")
        print a["results"][1]["formatted_address"]
        print("La tercera gasolinera mas cercana es:")
        print a["results"][2]["formatted_address"]
        print("La cuarta gasolinera mas cercana es:")
        print a["results"][3]["formatted_address"]
        print("La quinta gasolinera mas cercana es:")
        print a["results"][4]["formatted_address"]


print "\t\t\t\t\t\t\t\tServicio 2"
#para el uso del sevicio es necesario el rendimiento de gasolina, la capacidad del tanque y la cantidad de gasolina disponible en el tanque
rendimiento=float(raw_input("\n\nDame el rendimiento de gasolina de tu automovil en km/l: "))
captanque=float(raw_input("Dame la capacidad de tu tanque de gasolina "))
#la cantidad de combustible con la cual dispongo se ingresa del 0 al 1 siendo .5 la mitad del tanque
tanque=float(raw_input("Dame en fraccion la cantidad de gasolina con la cual dispones "))
ago=Agotamiento()
ago.punto_de_alerta_de_combustible_bajo(rendimiento,captanque,tanque)
