import re

class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    def __init__(self):
        self.__nombre = ""
        self.__historia = 0
        self.__tipo = ""
        self.__peso = 0
        self.__fecha_ingreso = ""
        self.__lista_medicamentos = []

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
            
    def asignarNombre(self, n):
        self.__nombre = n
    def asignarHistoria(self, nh):
        self.__historia = nh
    def asignarTipo(self, t):
        self.__tipo = t
    def asignarPeso(self, p):
        self.__peso = p
    def asignarFecha(self, f):
        self.__fecha_ingreso = f
    def asignarLista_Medicamentos(self, n):
        self.__lista_medicamentos = n 

class sistemaV:
    def __init__(self):
        self.__lista_mascotas = []
    
    def verificarExiste(self, historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        return False
        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas) 
    
    def ingresarMascota(self, mascota):
        self.__lista_mascotas.append(mascota) 

    def verFechaIngreso(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return "La mascota no está en el sistema."

    def verMedicamento(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos()
        return "La mascota no está registrada en el sistema."
    
    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                self.__lista_mascotas.remove(masc)
                return "Mascota eliminada del sistema con éxito."
        return "La historia clínica no está en el sistema."

def main():
    servicio_hospitalario = sistemaV()

    while True:
        print(f"\nMascotas hospitalizadas actualmente: {servicio_hospitalario.verNumeroMascotas()} / 10")
        menu = input('''\nIngrese una opción: 
1- Ingresar una mascota 
2- Ver fecha de ingreso 
3- Ver número de mascotas en el servicio 
4- Ver medicamentos que se están administrando
5- Eliminar mascota 
6- Salir 
Usted ingresó la opción: ''')

        if not menu.isdigit():
            print("Debe ingresar un número válido.")
            continue

        menu = int(menu)

        if menu == 1:
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio disponible para nuevas mascotas.")
                continue

            historia = input("Ingrese la historia clínica de la mascota: ")
            if not historia.isdigit():
                print("El número de historia clínica debe ser un número.")
                continue
            historia = int(historia)

            if servicio_hospitalario.verificarExiste(historia):
                print("Ya existe una mascota con ese número de historia clínica.")
                continue

            nombre = input("Ingrese el nombre de la mascota: ")
            tipo = input("Ingrese el tipo de mascota (canino o felino): ").lower()
            if tipo not in ["canino", "felino"]:
                print("El tipo debe ser 'canino' o 'felino'.")
                continue

            peso = input("Ingrese el peso de la mascota: ")
            if not peso.isdigit():
                print("El peso debe ser un número.")
                continue
            peso = int(peso)

            fecha = input("Ingrese la fecha de ingreso (dd/mm/aaaa): ")
            if not re.match(r"^\d{2}/\d{2}/\d{4}$", fecha):
                print("La fecha debe tener el formato dd/mm/aaaa.")
                continue

            nm = input("Ingrese la cantidad de medicamentos: ")
            if not nm.isdigit():
                print("Debe ingresar un número válido.")
                continue
            nm = int(nm)

            lista_med = []
            nombres_med = set()

            for i in range(nm):
                nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                if nombre_medicamentos in nombres_med:
                    print("No se pueden ingresar medicamentos repetidos.")
                    continue
                nombres_med.add(nombre_medicamentos)

                dosis = input("Ingrese la dosis: ")
                if not dosis.isdigit():
                    print("La dosis debe ser un número.")
                    continue
                dosis = int(dosis)

                medicamento = Medicamento()
                medicamento.asignarNombre(nombre_medicamentos)
                medicamento.asignarDosis(dosis)
                lista_med.append(medicamento)

            mas = Mascota()
            mas.asignarNombre(nombre)
            mas.asignarHistoria(historia)
            mas.asignarPeso(peso)
            mas.asignarTipo(tipo)
            mas.asignarFecha(fecha)
            mas.asignarLista_Medicamentos(lista_med)
            servicio_hospitalario.ingresarMascota(mas)

        elif menu == 2:
            historia = input("Ingrese la historia clínica de la mascota: ")
            if not historia.isdigit():
                print("Debe ingresar un número válido.")
                continue
            historia = int(historia)

            fecha = servicio_hospitalario.verFechaIngreso(historia)
            print("Fecha de ingreso:", fecha)

        elif menu == 3:
            numero = servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es:", numero)

        elif menu == 4:
            historia = input("Ingrese la historia clínica de la mascota: ")
            if not historia.isdigit():
                print("Debe ingresar un número válido.")
                continue
            historia = int(historia)

            medicamentos = servicio_hospitalario.verMedicamento(historia)
            if isinstance(medicamentos, str):
                print(medicamentos)
            else:
                print("Los medicamentos suministrados son:")
                for m in medicamentos:
                    print(f"- {m.verNombre()}")

        elif menu == 5:
            historia = input("Ingrese la historia clínica de la mascota a eliminar: ")
            if not historia.isdigit():
                print("Debe ingresar un número válido.")
                continue
            historia = int(historia)

            mensaje = servicio_hospitalario.eliminarMascota(historia)
            print(mensaje)

        elif menu == 6:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break

        else:
            print("Usted ingresó una opción no válida, inténtelo nuevamente...")

if __name__ == '__main__':
    main()
