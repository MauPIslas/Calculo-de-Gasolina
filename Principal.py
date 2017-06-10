class Principal:
    def servicio(self, serv):
        print "\n\n"
        if serv=="1":
            import pro
        elif serv=="2":
            import dir
        else:
            print "No elegiste una de las dos opciones"


print "\n\n\t\t\t\t\t\t Servicios referentes al consumo de combustible"
print"\n\n\t\t\t 1.- Cantidad total de gasolina necesaria para ir de un lugar a otro y costo"
print"\t\t\t 2.- Alerta de combustible, Hasta a donde llego con un determinado combustible y buqueda de gasolineras "

serv=raw_input("\n\n Ingresa el numero de servicio a utilizar ")
pri=Principal()
pri.servicio(serv)
