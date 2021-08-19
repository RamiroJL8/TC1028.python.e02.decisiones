#ramiro Juárez 
print("--------------------------------------------------------------------------")
print ()
edad = int(input("Ingresa tu edad: "))
if edad <= 0:
    print("respuesta incorrecta")
elif edad < 18:
        print("Usted no puede tramitar su licencia ya que es menor de edad")
else:
         Id = input("¿Tienes identificación oficial? ")
         if Id == "si":
             print("Usted es candidato a tramitar su licencia ")
         else:
            print ("Usted no puede tramitar su licencia sin su identificación oficial")
print ()
print("--------------------------------------------------------------------------")
