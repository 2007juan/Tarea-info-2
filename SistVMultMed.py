import re

class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self, med):
        self.__nombre = med 
    def asignarDosis(self, med):
        self.__dosis = med 

class Mascota:
    def __init__(self):
        self.__nombre= ""
        self.__historia=0
        self.__tipo=""
        self.__peso=0
        self.__fecha_ingreso=""
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    def eliminarMedicamento(self, nombre_medicamento):
        for m in self.__lista_medicamentos:
            if m.verNombre().lower() == nombre_medicamento.lower():
                self.__lista_medicamentos.remove(m)
                return f"Medicamento '{nombre_medicamento}' eliminado con éxito"
        return f"El medicamento '{nombre_medicamento}' no está en la lista"

class sistemaV:
    def __init__(self):
        self.__caninos = {}
        self.__felinos = {}
    
    def verificarExiste(self,historia):
        return historia in self.__caninos or historia in self.__felinos
        
    def verNumeroMascotas(self):
        return len(self.__caninos) + len(self.__felinos)
    
    def ingresarMascota(self,mascota):
        if mascota.verTipo().lower() == "canino":
            self.__caninos[mascota.verHistoria()] = mascota
        elif mascota.verTipo().lower() == "felino":
            self.__felinos[mascota.verHistoria()] = mascota
   
    def verFechaIngreso(self,historia):
        if historia in self.__caninos:
            return self.__caninos[historia].verFecha()
        elif historia in self.__felinos:
            return self.__felinos[historia].verFecha()
        return "La mascota no está en el sistema"

    def verMedicamento(self,historia):
        if historia in self.__caninos:
            return self.__caninos[historia].verLista_Medicamentos()
        elif historia in self.__felinos:
            return self.__felinos[historia].verLista_Medicamentos()
        return "La mascota no está registrada en el sistema"
    
    def eliminarMascota(self, historia):
        if historia in self.__caninos:
            del self.__caninos[historia]
            return "Mascota eliminada del sistema con éxito"
        elif historia in self.__felinos:
            del self.__felinos[historia]
            return "Mascota eliminada del sistema con éxito"
        return "La historia clínica no está en el sistema"

    def eliminarMedicamentoDeMascota(self, historia, nombre_medicamento):
        if historia in self.__caninos:
            return self.__caninos[historia].eliminarMedicamento(nombre_medicamento)
        elif historia in self.__felinos:
            return self.__felinos[historia].eliminarMedicamento(nombre_medicamento)
        return "La mascota no está registrada en el sistema"

def validar_fecha(fecha):
    patron = r"^\d{2}/\d{2}/\d{4}$"
    return bool(re.match(patron, fecha))

def main():
    servicio_hospitalario = sistemaV()
    while True:
        print(f"\nNúmero de mascotas actualmente: {servicio_hospitalario.verNumeroMascotas()} / 10")
        menu=int(input('''\nIngrese una opción: 
1- Ingresar una mascota 
2- Ver fecha de ingreso 
3- Ver número de mascotas en el servicio 
4- Ver medicamentos que se están administrando
5- Eliminar mascota 
6- Eliminar medicamento de una mascota
7- Salir 
Opción: ''' ))

        if menu==1:
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            try:
                historia=int(input("Ingrese la historia clínica de la mascota: "))
                if historia <= 0:
                    print("El número de historia clínica debe ser un número positivo.")
                    continue
            except:
                print("Debe ingresar un número válido.")
                continue

            if servicio_hospitalario.verificarExiste(historia):
                print("Ya existe una mascota con esa historia clínica")
                continue

            nombre=input("Ingrese el nombre de la mascota: ")
            tipo=input("Ingrese el tipo de mascota (felino o canino): ").lower()
            if tipo not in ["canino", "felino"]:
                print("El tipo de mascota debe ser 'canino' o 'felino'")
                continue

            try:
                peso=int(input("Ingrese el peso de la mascota: "))
            except:
                print("Debe ingresar un número válido para el peso.")
                continue

            fecha=input("Ingrese la fecha de ingreso (dd/mm/aaaa): ")
            if not validar_fecha(fecha):
                print("Formato de fecha incorrecto. Debe ser dd/mm/aaaa.")
                continue

            try:
                nm=int(input("Ingrese cantidad de medicamentos: "))
            except:
                print("Debe ingresar un número válido para la cantidad de medicamentos.")
                continue

            lista_med=[]
            nombres_med = set()

            for i in range(nm):
                nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                if nombre_medicamentos in nombres_med:
                    print("No se pueden ingresar medicamentos repetidos.")
                    continue
                nombres_med.add(nombre_medicamentos)

                try:
                    dosis =int(input("Ingrese la dosis: "))
                except:
                    print("Debe ingresar una dosis válida.")
                    continue

                medicamento = Medicamento()
                medicamento.asignarNombre(nombre_medicamentos)
                medicamento.asignarDosis(dosis)
                lista_med.append(medicamento)

            mas= Mascota()
            mas.asignarNombre(nombre)
            mas.asignarHistoria(historia)
            mas.asignarPeso(peso)
            mas.asignarTipo(tipo)
            mas.asignarFecha(fecha)
            mas.asignarLista_Medicamentos(lista_med)
            servicio_hospitalario.ingresarMascota(mas)

        elif menu==2:
            try:
                q = int(input("Ingrese la historia clínica de la mascota: "))
                if q <= 0:
                    print("El número de historia clínica debe ser un número positivo.")
                    continue
            except:
                print("Debe ingresar un número válido.")
                continue
            print(servicio_hospitalario.verFechaIngreso(q))
            
        elif menu==3:
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4:
            try:
                q = int(input("Ingrese la historia clínica de la mascota: "))
                if q <= 0:
                    print("El número de historia clínica debe ser un número positivo.")
                    continue
            except:
                print("Debe ingresar un número válido.")
                continue
            resultado = servicio_hospitalario.verMedicamento(q)
            if isinstance(resultado, str):
                print(resultado)
            else:
                print("Los medicamentos suministrados son: ")
                for m in resultado:
                    print(f"- {m.verNombre()} (Dosis: {m.verDosis()})")
        
        elif menu == 5:
            try:
                q = int(input("Ingrese la historia clínica de la mascota: "))
                if q <= 0:
                    print("El número de historia clínica debe ser un número positivo.")
                    continue
            except:
                print("Debe ingresar un número válido.")
                continue
            print(servicio_hospitalario.eliminarMascota(q))
        
        elif menu == 6:
            try:
                historia = int(input("Ingrese la historia clínica de la mascota: "))
                if historia <= 0:
                    print("El número de historia clínica debe ser un número positivo.")
                    continue
            except:
                print("Debe ingresar un número válido.")
                continue
            nombre_medicamento = input("Ingrese el nombre del medicamento que desea eliminar: ")
            print(servicio_hospitalario.eliminarMedicamentoDeMascota(historia, nombre_medicamento))

        elif menu==7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()

