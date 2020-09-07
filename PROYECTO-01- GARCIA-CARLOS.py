#Importando los datos de LifeStore file
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
import datetime

#User y Pass
usuarios_admin = [["admin", "123"], ["dgrc", "pass"]]
usuarios_Normal = [["lalo", "lol"]]

#Creando login
print("************************************")
print("        Bienvenido a Life Store")
print("************************************")
print("\n")
print(datetime.datetime.now())

# 1 si es admin, 0 si no lo es
rol_status = ""
#Lectura de credenciales del usuario
user_in = input("Ingresa tu usuario: ")
pswd_in = input("Ingresa tu contraseña: ")

#validación de credenciales de acceso
for usuario in usuarios_admin:
    if usuario[0] == user_in and usuario[1] == pswd_in:
        rol_status = "1"#1 si es admin
        break
    else:
        continue
for usuario in usuarios_Normal:
    if usuario[0] == user_in and usuario[1] == pswd_in:
        rol_status = "0"#0 si es un usuario promedio
        break
    else:
        continue

#privilegios y opciones si es admin
if rol_status == "1":
    print("\n")
    print("_________Eres administrador_________")
    print("\n")
    #menú de navegación
    print("Bienvenido, ¿Qué información desea consultar?")
    print("\n")
    print("1.- Productos más vendidos y productos rezagados")
    print("2.- Productos por reseña en el servicio ")
    print("3.- Ingresos y ventas")
    print("4.- Salir")
    #Lectura de opción elegida
    opcion = input("Escriba la opción deseada: ")
    #menú de información que es posible brindar en opc 1
    if opcion == "1":
        print("A.- 50 productos más vendidos: ")
        print("B- 100 productos con mayores busquedas:")
        print("C.- 50 menos vendidos por categoría: ")
        print("D.- 100 menos buscados por categoria")
        print("\n")
        opcionL = input("Elija la opción deseada: ")
        print("\n")
        if opcionL=="A" or opcionL=="a":
          print("PRODUCTOS MÁS VENDIDOS \n")
          total_ventas = []  #[[id_producto,nombre_producto,contador_ventas]]
          cnt = 0
          for producto in lifestore_products:
            for venta in lifestore_sales:
              if producto[0] == venta[1]:
                cnt += 1
            total_ventas.append([producto[0], cnt])
            cnt = 0
          ventas_ordenadas = []
          while total_ventas:
            minimo = total_ventas[0][1]
            lista_actual = total_ventas[0]
            for venta in total_ventas:
              if venta[1] > minimo:
                minimo = venta[1]
                lista_actual = venta
            ventas_ordenadas.append(lista_actual)
            total_ventas.remove(lista_actual)
          cnt_loop = 0
          for i in ventas_ordenadas:
            for nombre in lifestore_products:
              if cnt_loop==50:
                break
              if i[0] == nombre[0]:
                print("|ID del producto: ", nombre[0]," |Descripción: ", nombre[1]," || |Unidades Vendidas: ", i[1], "|")
                print("*********************")
                cnt_loop += 1
        if opcionL=="B" or opcionL=="b":
          total_busqueda=[] #[[id_producto, nombre_producto, cnt_busqueda]]
          #contador para identificación de semejanzas en los registros
          cnt_busq=0
          #por cada producto en lifestore_products, hacer una iteracion por cada busqueda realizada
          for producto in lifestore_products:
            for busqueda in lifestore_searches:
              if producto[0]==busqueda[1]:#si el id_producto es igual al id_producto de la busqueda
                cnt_busq+=1#aumentar contador de busqueda
            total_busqueda.append([producto[0],cnt_busq])#agregar en la lista total busqueda la pareja del id del producto y el total de veces encontrado, el cua esta almacenado en el cnt_busq
            cnt_busq=0 #se reinicia el contador

          busquedas_ordenadas=[] #se crea una lista vacia donde se almacenarán los registros ordenados [id_producto, cnt_busq]

          #reutilice el codigo de ordenamiento del inciso a
          while total_busqueda:
            minimo = total_busqueda[0][1]
            lista_actual = total_busqueda[0]
            for venta in total_busqueda:
              if venta[1] > minimo:
                minimo = venta[1]
                lista_actual = venta
            busquedas_ordenadas.append(lista_actual)
            total_busqueda.remove(lista_actual)


          cnt_loop = 0
          #por cada elemento en busquedas ordenadas iterar en lifestore_products
          for i in busquedas_ordenadas:
            for nombre in lifestore_products:
              if cnt_loop==100:
                break
                #impresión en consola de los resultados
              if i[0] == nombre[0]:
                print("|ID del producto: ", nombre[0]," |Descripción: ", nombre[1]," || |Busquedas Realizadas: ", i[1], "|")
                print("*********************")
                cnt_loop+=1
        if opcionL=="C" or opcionL=="c":
          total_ventas = [] #[[id_producto,contador_ventas]]
          cnt = 0
          for producto in lifestore_products:
            for venta in lifestore_sales:
              if producto[0] == venta[1]:
                cnt+=1
            total_ventas.append([producto[0], cnt])
            cnt = 0
          ventas_ordenadas = []
          while total_ventas:
            minimo = total_ventas[0][1]
            lista_actual = total_ventas[0]
            for venta in total_ventas:
              if venta[1] < minimo:
                minimo = venta[1]
                lista_actual = venta
            ventas_ordenadas.append(lista_actual)
            total_ventas.remove(lista_actual)

          Lista_Cat=[]#[categoria,cant_vendidas]

          #contador audifonos
          print("Top menos vendido, CATEGORÍA AUDIFONOS \n")
          for a in ventas_ordenadas:
            if a[0]>=84 and a[0]<=96:
              Lista_Cat.append(a)
          cnt_loop=0
          for i in Lista_Cat:
            for nombre in lifestore_products:
              if cnt_loop == 50:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("Producto: ", nombre[1], "Unidades vendidas: ", i[1])
                print("********************* ")
                
          Lista_Cat=[]

          #contador bocinas
          print("\n****************************************")
          print("Top menos vendido, CATEGORÍA BOCINAS \n")
          for a in ventas_ordenadas:
            if a[0]>=74 and a[0]<=83:
              Lista_Cat.append(a)
          cnt_loop=0
          for i in Lista_Cat:
            for nombre in lifestore_products:
              if cnt_loop == 50:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Unidades vendidas: ", i[1])
                print("*********************")
          Lista_Cat=[]

          #categoria pantallas
          print("\n****************************************")
          print("Top menos vendido, CATEGORÍA PANTALLAS \n")
          for a in ventas_ordenadas:
            if a[0]>=62 and a[0]<=73:
              Lista_Cat.append(a)
          cnt_loop=0
          for i in Lista_Cat:
            for nombre in lifestore_products:
              if cnt_loop == 50:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Unidades vendidas: ", i[1])
                print("*********************")
          Lista_Cat=[]
          #CATEGORIA MEMORIAS USB
          print("\n****************************************")
          print("Top menos vendido, CATEGORÍA MEMORIAS USB \n")
          for a in ventas_ordenadas:
            if a[0]>=60 and a[0]<=61:
              Lista_Cat.append(a)
          cnt_loop=0
          for i in Lista_Cat:
            for nombre in lifestore_products:
              if cnt_loop == 50:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Unidades vendidas: ", i[1])
                print("*********************")
          Lista_Cat=[]

          #DISCOS DUROS
          print("\n****************************************")
          print("Top menos vendido, DISCOS DUROS \n")
          for a in ventas_ordenadas:
            if a[0]>=47 and a[0]<=59:
              Lista_Cat.append(a)
          cnt_loop=0
          for i in Lista_Cat:
            for nombre in lifestore_products:
              if cnt_loop == 50:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Unidades vendidas: ", i[1])
                print("*********************")
          Lista_Cat=[]

          print("\n****************************************")
          print("Top menos vendido, TARJETAS MADRE  \n")
          for a in ventas_ordenadas:
            if a[0]>=29 and a[0]<=46:
              Lista_Cat.append(a)
          cnt_loop=0
          for i in Lista_Cat:
            for nombre in lifestore_products:
              if cnt_loop == 50:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Unidades vendidas: ", i[1])
                print("*********************")
          Lista_Cat=[]

          #TARJETAS DE VIDEO
          print("\n****************************************")
          print("Top menos vendido, TARJETAS DE VIDEO \n")
          for a in ventas_ordenadas:
            if a[0]>=10 and a[0]<=28:
              Lista_Cat.append(a)
          cnt_loop=0
          for i in Lista_Cat:
            for nombre in lifestore_products:
              if cnt_loop == 50:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Unidades vendidas: ", i[1])
                print("*********************")
          Lista_Cat=[]
          #PROCESADORES 
          print("\n****************************************")
          print("Top menos vendido, CATEGORÍA PROCESADORES \n")
          for a in ventas_ordenadas:
            if a[0]>=1 and a[0]<=9:
              Lista_Cat.append(a)
          cnt_loop=0
          for i in Lista_Cat:
            for nombre in lifestore_products:
              if cnt_loop == 50:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("Producto: ", nombre[1], "Unidades vendidas: ", i[1])
                print("*********************")
          Lista_Cat=[]
        if opcionL=="D" or opcionL=="d":
          total_busqueda=[] #[[id_producto, nombre_producto, cnt_busqueda]]
          #contador para identificación de semejanzas en los registros
          cnt_busq=0

          #por cada producto en lifestore_products, hacer una iteracion por cada busqueda realizada
          for producto in lifestore_products:
            for busqueda in lifestore_searches:
              if producto[0]==busqueda[1]:#si el id_producto es igual al id_producto de la busqueda
                cnt_busq+=1#aumentar contador de busqueda
            total_busqueda.append([producto[0],cnt_busq])#agregar en la lista total busqueda la pareja del id del producto y el total de veces encontrado, el cua esta almacenado en el cnt_busq
            cnt_busq=0 #se reinicia el contador

          busquedas_ordenadas=[] #se crea una lista vacia donde se almacenarán los registros ordenados [id_producto, cnt_busq]

          #reutilice el codigo de ordenamiento del inciso a
          while total_busqueda:
            minimo = total_busqueda[0][1]
            lista_actual = total_busqueda[0]
            for venta in total_busqueda:
              if venta[1] <minimo:
                minimo = venta[1]
                lista_actual = venta
            busquedas_ordenadas.append(lista_actual)
            total_busqueda.remove(lista_actual)

          Lista_Busq=[]#[Busquedas,cant_vendidas]

          #contador audifonos
          print("Top menos buscado, CATEGORÍA AUDIFONOS \n")
          for a in busquedas_ordenadas:
            if a[0]>=84 and a[0]<=96:#rangos de id categoria audifonos
              Lista_Busq.append(a)#agregar a una lista todos los productos de categoria audifonos junto a sus unidades buscadas

          cnt_loop=0 #contador para repeticiones del loop
          for i in Lista_Busq: #iteraciones de busqueda 
            for nombre in lifestore_products:
              if cnt_loop == 100:#detener el loop cuando el contador llegue a 0
                break
              if i[0] == nombre[0]:
                cnt_loop += 1 #hacer una disminución en reversa del cnt_loop
                print("Top", cnt_loop)
                #impresión de pantalla de resultados
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Veces que ha sido buscado en la BD: ", i[1])
                print("********************* ")
                
          Lista_Busq=[]

          #contador bocinas
          print("\n****************************************")
          print("Top menos buscado, CATEGORÍA BOCINAS \n")
          for a in busquedas_ordenadas:
            if a[0]>=74 and a[0]<=83:
              Lista_Busq.append(a)
          cnt_loop=0
          for i in Lista_Busq:
            for nombre in lifestore_products:
              if cnt_loop == 100:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Veces que el producto ha sido buscado: ", i[1])
                print("*********************")
          Lista_Busq=[]

          #categoria pantallas
          print("\n****************************************")
          print("Top menos buscao, CATEGORÍA PANTALLAS \n")
          for a in busquedas_ordenadas:
            if a[0]>=62 and a[0]<=73:
              Lista_Busq.append(a)
          cnt_loop=0
          for i in Lista_Busq:
            for nombre in lifestore_products:
              if cnt_loop == 100:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0], "Producto: ", nombre[1], "Veces que el producto ha sido buscado: ", i[1])
                print("*********************")
          Lista_Busq=[]
          #CATEGORIA MEMORIAS USB
          print("\n****************************************")
          print("Top menos buscado, CATEGORÍA MEMORIAS USB \n")
          for a in busquedas_ordenadas:
            if a[0]>=60 and a[0]<=61:
              Lista_Busq.append(a)
          cnt_loop=0
          for i in Lista_Busq:
            for nombre in lifestore_products:
              if cnt_loop == 100:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Veces que el producto ha sido buscado: ", i[1])
                print("*********************")
          Lista_Busq=[]

          #DISCOS DUROS
          print("\n****************************************")
          print("Top menos buscado, DISCOS DUROS \n")
          for a in busquedas_ordenadas:
            if a[0]>=47 and a[0]<=59:
              Lista_Busq.append(a)
          cnt_loop=0
          for i in Lista_Busq:
            for nombre in lifestore_products:
              if cnt_loop == 100:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], " Veces que el producto ha sido buscado: ", i[1])
                print("*********************")
          Lista_Busq=[]

          print("\n****************************************")
          print("Top menos buscado, TARJETAS MADRE  \n")
          for a in busquedas_ordenadas:
            if a[0]>=29 and a[0]<=46:
              Lista_Busq.append(a)
          cnt_loop=0
          for i in Lista_Busq:
            for nombre in lifestore_products:
              if cnt_loop == 100:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Veces que el producto ha sido buscado:  ", i[1])
                print("*********************")
          Lista_Busq=[]

          #TARJETAS DE VIDEO
          print("\n****************************************")
          print("Top menos buscado, TARJETAS DE VIDEO \n")
          for a in busquedas_ordenadas:
            if a[0]>=10 and a[0]<=28:
              Lista_Busq.append(a)
          cnt_loop=0
          for i in Lista_Busq:
            for nombre in lifestore_products:
              if cnt_loop == 100:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Veces que el producto ha sido buscado: ", i[1])
                print("*********************")
          Lista_Busq=[]
          #PROCESADORES 
          print("\n****************************************")
          print("Top menos buscados, CATEGORÍA BOCINAS \n")
          for a in busquedas_ordenadas:
            if a[0]>=1 and a[0]<=9:
              Lista_Busq.append(a)
          cnt_loop=0
          for i in Lista_Busq:
            for nombre in lifestore_products:
              if cnt_loop == 100:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Veces que el producto ha sido buscado: ", i[1])
                print("*********************")
          Lista_Busq=[]
        
    if opcion=="2":
      print("\n A.- 20 Productos con mejores reseñas \n")
      print("B.- 20 Productos con peores reseñas \n")
      opcionL=input("Elija la opción deseada: ")
      print("\n")
      if opcionL=="A" or opcionL=="a":
        formato_ideal=[] #[id_prod, prom_rese,cant_dev]
        prelista=[]
        for i in lifestore_sales:
          prelista.append([i[1],i[2],i[4]])
        #print(prelista)
        print("**************************")

        cnt_res=0
        acum_res=0
        cant_dev=0
        for i in lifestore_sales:
          for a in prelista:
            if i[1]==a[0]:
              cnt_res+=1
              acum_res+=a[1]
              cant_dev+=a[2]
          prom=acum_res/cnt_res
          formato_ideal.append([i[1],prom,cant_dev])
          cnt_res=0
          acum_res=0
          cant_dev=0

        #print(formato_ideal)
        Lista_depurada=[]#[id producto, prom_reseña, cant-dev]
        for i in formato_ideal:
          if i not in Lista_depurada:
            Lista_depurada.append(i)
        #print(Lista_depurada, "\n")

        reseñas_ordenadas=[] #se crea una lista vacia donde se almacenarán los registros ordenados [id_producto, cnt_busq]

        #reutilice el codigo de ordenamiento del inciso a
        while Lista_depurada:
          minimo = Lista_depurada[0][1]
          lista_actual = Lista_depurada[0]
          for venta in Lista_depurada:
            if venta[1] > minimo:
              minimo = venta[1]
              lista_actual = venta
          reseñas_ordenadas.append(lista_actual)
          Lista_depurada.remove(lista_actual)

        cnt_loop = 1
        #por cada elemento en busquedas ordenadas iterar en lifestore_products
        print("PRODUCTOS CON MEJORES RESEÑAS")
        for i in reseñas_ordenadas:
          for nombre in lifestore_products:
            if cnt_loop==21:
              break
              #impresión en consola de los resultados
            if i[0] == nombre[0]:
              print("Top ",cnt_loop,"|ID del producto: ", nombre[0]," |Descripción: ", nombre[1]," || |Promedio de reseñas: ", i[1], "|", "Devoluciones: ",i[2])
              print("*********************")
              cnt_loop+=1
      if opcionL=="B" or opcionL=="b":
        formato_ideal=[] #[id_prod, prom_rese,cant_dev]
        prelista=[]#obteniendo datos necesarios para el ordenamiento
        for i in lifestore_sales:
          prelista.append([i[1],i[2],i[4]])
        #print(prelista)
        print("**************************")

        cnt_res=0
        acum_res=0
        cant_dev=0
        for i in lifestore_sales:
          for a in prelista:
            if i[1]==a[0]:
              cnt_res+=1
              acum_res+=a[1]
              cant_dev+=a[2]
          prom=acum_res/cnt_res
          formato_ideal.append([i[1],prom,cant_dev])
          cnt_res=0
          acum_res=0
          cant_dev=0

        #print(formato_ideal)
        Lista_depurada=[]#[id producto, prom_reseña, cant-dev]
        for i in formato_ideal:
          if i not in Lista_depurada:
            Lista_depurada.append(i)

        reseñas_ordenadas=[] #se crea una lista vacia donde se almacenarán los registros ordenados [id_producto, cnt_busq]

        #reutilice el codigo de ordenamiento del inciso a
        while Lista_depurada:
          minimo = Lista_depurada[0][1]
          lista_actual = Lista_depurada[0]
          for venta in Lista_depurada:
            if venta[1] < minimo:
              minimo = venta[1]
              lista_actual = venta
          reseñas_ordenadas.append(lista_actual)
          Lista_depurada.remove(lista_actual)
        res_orden2=[]
        while reseñas_ordenadas:
          minimo = reseñas_ordenadas[0][2]
          lista_actual = reseñas_ordenadas[0]
          for venta in reseñas_ordenadas:
            if venta[1] < minimo:
              minimo = venta[1]
              lista_actual = venta
          res_orden2.append(lista_actual)
          reseñas_ordenadas.remove(lista_actual)
        cnt_loop = 1
        #por cada elemento en busquedas ordenadas iterar en lifestore_products
        print("PRODUCTOS CON PEORES RESEÑAS \n")
        for i in res_orden2:
          for nombre in lifestore_products:
            if cnt_loop==21:
              break
              #impresión en consola de los resultados
            if i[0] == nombre[0]:
              print("Top ",cnt_loop,"|ID del producto: ", nombre[0]," |Descripción: ", nombre[1]," || |Promedio de reseñas: ", i[1], "|", "Devoluciones: ",i[2])
              print("*********************")
              cnt_loop+=1
    if opcion=="3":
      print("\n")
      print("A.- Ingresos mensuales y Ventas promedio mensuales")
      print("B.- Total de ventas anuales")
      print("C.- Top de meses con más ventas")
      opcionL=input("\n Ingrese la opcion deseada: \n")
      if opcionL=="A" or opcionL=="a":
        prelista=[]#[id_producto, mes ó año de venta]
        #Creando prelista con iteracion a partir de meses
        for i in lifestore_sales:
          for a in lifestore_products:
            if i[1]==a[0]:
              b=i[3]
              c=a[2]
          prelista.append([i[1],b[3:5],c]) 

        acum_mens=0
        cont_ventas=0
        #mes de enero 
        for i in prelista:
          if i[1]=="01":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        print("\nVentas del mes de ENERO: $", acum_mens)
        if cont_ventas>0:
          print("Ventas promedio del mes de ENERO: ",acum_mens/cont_ventas, "\n")
        cont_ventas=0
        acum_mens=0
        #mes de febrero 
        for i in prelista:
          if i[1]=="02":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        print("\nVentas del mes de FEBRERO: $", acum_mens)
        if cont_ventas>0:
          print("Ventas promedio del mes de FEBRERO: ",acum_mens/cont_ventas, "\n")
        cont_ventas=0
        acum_mens=0
        #mes de Marzo 
        for i in prelista:
          if i[1]=="03":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        print("\nVentas del mes de MARZO: $", acum_mens)
        if cont_ventas>0:
          print("Ventas promedio del mes de MARZO: ",acum_mens/cont_ventas, "\n")
        cont_ventas=0
        acum_mens=0
        #mes de ABRIL 
        for i in prelista:
          if i[1]=="04":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        print("\nVentas del mes de ABRIL: $", acum_mens)
        if cont_ventas>0:
          print("Ventas promedio del mes de ABRIL: ",acum_mens/cont_ventas, "\n")
        cont_ventas=0
        acum_mens=0
        #mes de MAYO 
        for i in prelista:
          if i[1]=="05":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        print("\nVentas del mes de MAYO: $", acum_mens)
        if cont_ventas>0:
          print("Ventas promedio del mes de MAYO: ",acum_mens/cont_ventas, "\n")
        cont_ventas=0
        acum_mens=0
        #mes de JUNIO 
        for i in prelista:
          if i[1]=="06":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        print("\nVentas del mes de JUNIO: $", acum_mens)
        if cont_ventas>0:
          print("Ventas promedio del mes de JUNIO: ",acum_mens/cont_ventas, "\n")
        cont_ventas=0
        acum_mens=0
        #mes de JULIO 
        for i in prelista:
          if i[1]=="07":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        print("\nVentas del mes de JULIO: $", acum_mens)
        if cont_ventas>0:
          print("Ventas promedio del mes de JULIO: ",acum_mens/cont_ventas, "\n")
        cont_ventas=0
        acum_mens=0
        #mes de AGOSTO 
        for i in prelista:
          if i[1]=="08":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        print("\nVentas del mes de AGOSTO: $", acum_mens)
        if cont_ventas>0:
          print("Ventas promedio del mes de AGOSTO: ",acum_mens/cont_ventas, "\n")
        cont_ventas=0
        acum_mens=0
        #mes de SEPTIEMBRE 
        for i in prelista:
          if i[1]=="09":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        print("\nVentas del mes de SEPTIEMBRE: $", acum_mens)
        if cont_ventas>0:
          print("Ventas promedio del mes de SEPTIEMBRE: ",acum_mens/cont_ventas, "\n")
        cont_ventas=0
        acum_mens=0
        #mes de OCTUBRE 
        for i in prelista:
          if i[1]=="10":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        print("\nVentas del mes de OCTUBRE: $", acum_mens)
        if cont_ventas>0:
          print("Ventas promedio del mes de OCTUBRE: ",acum_mens/cont_ventas, "\n")
        cont_ventas=0
        acum_mens=0
        #mes de NOVIEMBRE 
        for i in prelista:
          if i[1]=="11":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        print("\nVentas del mes de NOVIEMBRE: $", acum_mens)
        if cont_ventas>0:
          print("Ventas promedio del mes de NOVIEMBRE: ",acum_mens/cont_ventas, "\n")
        cont_ventas=0
        acum_mens=0
        #mes de DICIEMBRE 
        for i in prelista:
          if i[1]=="12":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        print("\nVentas del mes de DICIEMBRE: $", acum_mens)
        if cont_ventas>0:
          print("Ventas promedio del mes de DICIEMBRE: ",acum_mens/cont_ventas, "\n")
        cont_ventas=0
        acum_mens=0


      if opcionL=="B" or opcionL=="b":
        prelista=[]#[id_producto, mes ó año de venta]
        #Creando prelista con iteracion a partir de meses
        for i in lifestore_sales:
          for a in lifestore_products:
            if i[1]==a[0]:
              b=i[3]
              c=a[2]
          prelista.append([i[1],b[3:5],c]) 

        #año 2020
        acumulador_venta=0
        for i in lifestore_sales:
          for a in lifestore_products:
            año=i[3]#calculando ingresos por años, haciendo slice
            l=año[6:10]
            if l=="2020":
              if i[1]==a[0]:
                acumulador_venta+=a[2]
        print("Ventas del año 2020: $ ",acumulador_venta ,"\n")
        acumulador_venta=0

      if opcionL=="C" or opcionL=="c":
        prelista=[]
        for i in lifestore_sales:
          for a in lifestore_products:
            if i[1]==a[0]:
              b=i[3]
              c=a[2]
          prelista.append([i[1],b[3:5],c])
        acum_mens=0
        cont_ventas=0
        rank_meses=[]
        #mes de enero 
        for i in prelista:
          if i[1]=="01":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        rank_meses.append(["ENERO",acum_mens])
        cont_ventas=0
        acum_mens=0
        #mes de febrero 
        for i in prelista:
          if i[1]=="02":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        rank_meses.append(["FEBRERO",acum_mens])
        cont_ventas=0
        acum_mens=0
        #mes de Marzo 
        for i in prelista:
          if i[1]=="03":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        rank_meses.append(["MARZO",acum_mens])
        cont_ventas=0
        acum_mens=0
        #mes de ABRIL 
        for i in prelista:
          if i[1]=="04":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        rank_meses.append(["ABRIL",acum_mens])
        cont_ventas=0
        acum_mens=0
        #mes de MAYO 
        for i in prelista:
          if i[1]=="05":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        rank_meses.append(["MAYO",acum_mens])
        cont_ventas=0
        acum_mens=0
        #mes de JUNIO 
        for i in prelista:
          if i[1]=="06":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        rank_meses.append(["JUNIO",acum_mens])
        cont_ventas=0
        acum_mens=0
        #mes de JULIO 
        for i in prelista:
          if i[1]=="07":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        rank_meses.append(["JULIO", acum_mens])
        acum_mens=0
        #mes de AGOSTO 
        for i in prelista:
          if i[1]=="08":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        rank_meses.append(["AGOSTO", acum_mens])
        cont_ventas=0
        acum_mens=0
        #mes de SEPTIEMBRE 
        for i in prelista:
          if i[1]=="09":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        rank_meses.append(["SEPTIEMBRE", acum_mens])
        cont_ventas=0
        acum_mens=0
        #mes de OCTUBRE 
        for i in prelista:
          if i[1]=="10":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        rank_meses.append(["OCTUBRE", acum_mens])
        cont_ventas=0
        acum_mens=0
        #mes de NOVIEMBRE 
        for i in prelista:
          if i[1]=="11":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        rank_meses.append(["NOVIEMBRE", acum_mens])
        cont_ventas=0
        acum_mens=0
        #mes de DICIEMBRE 
        for i in prelista:
          if i[1]=="12":#comparando el slice del mes con 01-12 según el mes que se desea obtener
            acum_mens+=i[2]#acumulando cantidades
            cont_ventas+=1#contando cantidades acumuladas
        rank_meses.append([" DICIEMRBE", acum_mens])
        cont_ventas=0
        acum_mens=0
        rank_orden=[]
        while rank_meses:
          minimo = rank_meses[0][1]
          lista_actual = rank_meses[0]
          for venta in rank_meses:
            if venta[1] > minimo:
              minimo = venta[1]
              lista_actual = venta
          rank_orden.append(lista_actual)
          rank_meses.remove(lista_actual)
        print(rank_orden)
        cnt=1
        print("RANKING DE LOS MESES CON MÁS VENTAS EN EL AÑO 2020 \n")
        for i in rank_orden:
          print("TOP ", cnt, "El mes de ", i[0], "con la cantidad de $ ", i[1])
          cnt+=1

    if opcion=="4":
      print("Saliendo del programa")
    
      

                      

#privilegios si es usuario normal
elif rol_status == "0":
    print("\n")
    print("_________Eres empleado general_________")
    print("\n")
    print("Bienvenido, ¿Qué información desea consultar?")
    print("\n")
    print("1.- Productos más vendidos y productos rezagados")
    print("2.- Productos por reseña en el servicio ")
    print("3.- Salir")
    opcion = input(" Escriba la opción deseada: ")
    if opcion == "1":
        print("A.- 50 productos más vendidos: ")
        print("B- 100 productos con mayores busquedas:")
        print("C.- 50 menos vendidos por categoría: ")
        print("D.- 100 menos buscados por categoria")
        print("\n")
        opcionL = input("Elija la opción deseada: ")
        print("\n")
        if opcionL=="A" or opcionL=="a":
          print("PRODUCTOS MÁS VENDIDOS \n")
          total_ventas = []  #[[id_producto,nombre_producto,contador_ventas]]
          cnt = 0
          for producto in lifestore_products:
            for venta in lifestore_sales:
              if producto[0] == venta[1]:
                cnt += 1
            total_ventas.append([producto[0], cnt])
            cnt = 0
          ventas_ordenadas = []
          while total_ventas:
            minimo = total_ventas[0][1]
            lista_actual = total_ventas[0]
            for venta in total_ventas:
              if venta[1] > minimo:
                minimo = venta[1]
                lista_actual = venta
            ventas_ordenadas.append(lista_actual)
            total_ventas.remove(lista_actual)
          cnt_loop = 0
          for i in ventas_ordenadas:
            for nombre in lifestore_products:
              if cnt_loop==50:
                break
              if i[0] == nombre[0]:
                print("|ID del producto: ", nombre[0]," |Descripción: ", nombre[1]," || |Unidades Vendidas: ", i[1], "|")
                print("*********************")
                cnt_loop += 1
        if opcionL=="B" or opcionL=="b":
          total_busqueda=[] #[[id_producto, nombre_producto, cnt_busqueda]]
          #contador para identificación de semejanzas en los registros
          cnt_busq=0
          #por cada producto en lifestore_products, hacer una iteracion por cada busqueda realizada
          for producto in lifestore_products:
            for busqueda in lifestore_searches:
              if producto[0]==busqueda[1]:#si el id_producto es igual al id_producto de la busqueda
                cnt_busq+=1#aumentar contador de busqueda
            total_busqueda.append([producto[0],cnt_busq])#agregar en la lista total busqueda la pareja del id del producto y el total de veces encontrado, el cua esta almacenado en el cnt_busq
            cnt_busq=0 #se reinicia el contador

          busquedas_ordenadas=[] #se crea una lista vacia donde se almacenarán los registros ordenados [id_producto, cnt_busq]

          #reutilice el codigo de ordenamiento del inciso a
          while total_busqueda:
            minimo = total_busqueda[0][1]
            lista_actual = total_busqueda[0]
            for venta in total_busqueda:
              if venta[1] > minimo:
                minimo = venta[1]
                lista_actual = venta
            busquedas_ordenadas.append(lista_actual)
            total_busqueda.remove(lista_actual)


          cnt_loop = 0
          #por cada elemento en busquedas ordenadas iterar en lifestore_products
          for i in busquedas_ordenadas:
            for nombre in lifestore_products:
              if cnt_loop==100:
                break
                #impresión en consola de los resultados
              if i[0] == nombre[0]:
                print("|ID del producto: ", nombre[0]," |Descripción: ", nombre[1]," || |Busquedas Realizadas: ", i[1], "|")
                print("*********************")
                cnt_loop+=1
        if opcionL=="C" or opcionL=="c":
          total_ventas = [] #[[id_producto,contador_ventas]]
          cnt = 0
          for producto in lifestore_products:
            for venta in lifestore_sales:
              if producto[0] == venta[1]:
                cnt+=1
            total_ventas.append([producto[0], cnt])
            cnt = 0
          ventas_ordenadas = []
          while total_ventas:
            minimo = total_ventas[0][1]
            lista_actual = total_ventas[0]
            for venta in total_ventas:
              if venta[1] < minimo:
                minimo = venta[1]
                lista_actual = venta
            ventas_ordenadas.append(lista_actual)
            total_ventas.remove(lista_actual)

          Lista_Cat=[]#[categoria,cant_vendidas]

          #contador audifonos
          print("Top menos vendido, CATEGORÍA AUDIFONOS \n")
          for a in ventas_ordenadas:
            if a[0]>=84 and a[0]<=96:
              Lista_Cat.append(a)
          cnt_loop=0
          for i in Lista_Cat:
            for nombre in lifestore_products:
              if cnt_loop == 50:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("Producto: ", nombre[1], "Unidades vendidas: ", i[1])
                print("********************* ")
                
          Lista_Cat=[]

          #contador bocinas
          print("\n****************************************")
          print("Top menos vendido, CATEGORÍA BOCINAS \n")
          for a in ventas_ordenadas:
            if a[0]>=74 and a[0]<=83:
              Lista_Cat.append(a)
          cnt_loop=0
          for i in Lista_Cat:
            for nombre in lifestore_products:
              if cnt_loop == 50:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Unidades vendidas: ", i[1])
                print("*********************")
          Lista_Cat=[]

          #categoria pantallas
          print("\n****************************************")
          print("Top menos vendido, CATEGORÍA PANTALLAS \n")
          for a in ventas_ordenadas:
            if a[0]>=62 and a[0]<=73:
              Lista_Cat.append(a)
          cnt_loop=0
          for i in Lista_Cat:
            for nombre in lifestore_products:
              if cnt_loop == 50:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Unidades vendidas: ", i[1])
                print("*********************")
          Lista_Cat=[]
          #CATEGORIA MEMORIAS USB
          print("\n****************************************")
          print("Top menos vendido, CATEGORÍA MEMORIAS USB \n")
          for a in ventas_ordenadas:
            if a[0]>=60 and a[0]<=61:
              Lista_Cat.append(a)
          cnt_loop=0
          for i in Lista_Cat:
            for nombre in lifestore_products:
              if cnt_loop == 50:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Unidades vendidas: ", i[1])
                print("*********************")
          Lista_Cat=[]

          #DISCOS DUROS
          print("\n****************************************")
          print("Top menos vendido, DISCOS DUROS \n")
          for a in ventas_ordenadas:
            if a[0]>=47 and a[0]<=59:
              Lista_Cat.append(a)
          cnt_loop=0
          for i in Lista_Cat:
            for nombre in lifestore_products:
              if cnt_loop == 50:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Unidades vendidas: ", i[1])
                print("*********************")
          Lista_Cat=[]

          print("\n****************************************")
          print("Top menos vendido, TARJETAS MADRE  \n")
          for a in ventas_ordenadas:
            if a[0]>=29 and a[0]<=46:
              Lista_Cat.append(a)
          cnt_loop=0
          for i in Lista_Cat:
            for nombre in lifestore_products:
              if cnt_loop == 50:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Unidades vendidas: ", i[1])
                print("*********************")
          Lista_Cat=[]

          #TARJETAS DE VIDEO
          print("\n****************************************")
          print("Top menos vendido, TARJETAS DE VIDEO \n")
          for a in ventas_ordenadas:
            if a[0]>=10 and a[0]<=28:
              Lista_Cat.append(a)
          cnt_loop=0
          for i in Lista_Cat:
            for nombre in lifestore_products:
              if cnt_loop == 50:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Unidades vendidas: ", i[1])
                print("*********************")
          Lista_Cat=[]
          #PROCESADORES 
          print("\n****************************************")
          print("Top menos vendido, CATEGORÍA PROCESADORES \n")
          for a in ventas_ordenadas:
            if a[0]>=1 and a[0]<=9:
              Lista_Cat.append(a)
          cnt_loop=0
          for i in Lista_Cat:
            for nombre in lifestore_products:
              if cnt_loop == 50:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("Producto: ", nombre[1], "Unidades vendidas: ", i[1])
                print("*********************")
          Lista_Cat=[]
        if opcionL=="D" or opcionL=="d":
          total_busqueda=[] #[[id_producto, nombre_producto, cnt_busqueda]]
          #contador para identificación de semejanzas en los registros
          cnt_busq=0

          #por cada producto en lifestore_products, hacer una iteracion por cada busqueda realizada
          for producto in lifestore_products:
            for busqueda in lifestore_searches:
              if producto[0]==busqueda[1]:#si el id_producto es igual al id_producto de la busqueda
                cnt_busq+=1#aumentar contador de busqueda
            total_busqueda.append([producto[0],cnt_busq])#agregar en la lista total busqueda la pareja del id del producto y el total de veces encontrado, el cua esta almacenado en el cnt_busq
            cnt_busq=0 #se reinicia el contador

          busquedas_ordenadas=[] #se crea una lista vacia donde se almacenarán los registros ordenados [id_producto, cnt_busq]

          #reutilice el codigo de ordenamiento del inciso a
          while total_busqueda:
            minimo = total_busqueda[0][1]
            lista_actual = total_busqueda[0]
            for venta in total_busqueda:
              if venta[1] <minimo:
                minimo = venta[1]
                lista_actual = venta
            busquedas_ordenadas.append(lista_actual)
            total_busqueda.remove(lista_actual)

          Lista_Busq=[]#[Busquedas,cant_vendidas]

          #contador audifonos
          print("Top menos buscado, CATEGORÍA AUDIFONOS \n")
          for a in busquedas_ordenadas:
            if a[0]>=84 and a[0]<=96:#rangos de id categoria audifonos
              Lista_Busq.append(a)#agregar a una lista todos los productos de categoria audifonos junto a sus unidades buscadas

          cnt_loop=0 #contador para repeticiones del loop
          for i in Lista_Busq: #iteraciones de busqueda 
            for nombre in lifestore_products:
              if cnt_loop == 100:#detener el loop cuando el contador llegue a 0
                break
              if i[0] == nombre[0]:
                cnt_loop += 1 #hacer una disminución en reversa del cnt_loop
                print("Top", cnt_loop)
                #impresión de pantalla de resultados
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Veces que ha sido buscado en la BD: ", i[1])
                print("********************* ")
                
          Lista_Busq=[]

          #contador bocinas
          print("\n****************************************")
          print("Top menos buscado, CATEGORÍA BOCINAS \n")
          for a in busquedas_ordenadas:
            if a[0]>=74 and a[0]<=83:
              Lista_Busq.append(a)
          cnt_loop=0
          for i in Lista_Busq:
            for nombre in lifestore_products:
              if cnt_loop == 100:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Veces que el producto ha sido buscado: ", i[1])
                print("*********************")
          Lista_Busq=[]

          #categoria pantallas
          print("\n****************************************")
          print("Top menos buscao, CATEGORÍA PANTALLAS \n")
          for a in busquedas_ordenadas:
            if a[0]>=62 and a[0]<=73:
              Lista_Busq.append(a)
          cnt_loop=0
          for i in Lista_Busq:
            for nombre in lifestore_products:
              if cnt_loop == 100:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0], "Producto: ", nombre[1], "Veces que el producto ha sido buscado: ", i[1])
                print("*********************")
          Lista_Busq=[]
          #CATEGORIA MEMORIAS USB
          print("\n****************************************")
          print("Top menos buscado, CATEGORÍA MEMORIAS USB \n")
          for a in busquedas_ordenadas:
            if a[0]>=60 and a[0]<=61:
              Lista_Busq.append(a)
          cnt_loop=0
          for i in Lista_Busq:
            for nombre in lifestore_products:
              if cnt_loop == 100:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Veces que el producto ha sido buscado: ", i[1])
                print("*********************")
          Lista_Busq=[]

          #DISCOS DUROS
          print("\n****************************************")
          print("Top menos buscado, DISCOS DUROS \n")
          for a in busquedas_ordenadas:
            if a[0]>=47 and a[0]<=59:
              Lista_Busq.append(a)
          cnt_loop=0
          for i in Lista_Busq:
            for nombre in lifestore_products:
              if cnt_loop == 100:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], " Veces que el producto ha sido buscado: ", i[1])
                print("*********************")
          Lista_Busq=[]

          print("\n****************************************")
          print("Top menos buscado, TARJETAS MADRE  \n")
          for a in busquedas_ordenadas:
            if a[0]>=29 and a[0]<=46:
              Lista_Busq.append(a)
          cnt_loop=0
          for i in Lista_Busq:
            for nombre in lifestore_products:
              if cnt_loop == 100:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Veces que el producto ha sido buscado:  ", i[1])
                print("*********************")
          Lista_Busq=[]

          #TARJETAS DE VIDEO
          print("\n****************************************")
          print("Top menos buscado, TARJETAS DE VIDEO \n")
          for a in busquedas_ordenadas:
            if a[0]>=10 and a[0]<=28:
              Lista_Busq.append(a)
          cnt_loop=0
          for i in Lista_Busq:
            for nombre in lifestore_products:
              if cnt_loop == 100:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Veces que el producto ha sido buscado: ", i[1])
                print("*********************")
          Lista_Busq=[]
          #PROCESADORES 
          print("\n****************************************")
          print("Top menos buscados, CATEGORÍA BOCINAS \n")
          for a in busquedas_ordenadas:
            if a[0]>=1 and a[0]<=9:
              Lista_Busq.append(a)
          cnt_loop=0
          for i in Lista_Busq:
            for nombre in lifestore_products:
              if cnt_loop == 100:
                break
              if i[0] == nombre[0]:
                cnt_loop += 1
                print("Top", cnt_loop)
                print("ID: ",nombre[0],"Producto: ", nombre[1], "Veces que el producto ha sido buscado: ", i[1])
                print("*********************")
          Lista_Busq=[]
        
    if opcion=="2":
      print("\n A.- 20 Productos con mejores reseñas \n")
      print("B.- 20 Productos con peores reseñas \n")
      opcionL=input("Elija la opción deseada: ")
      print("\n")
      if opcionL=="A" or opcionL=="a":
        formato_ideal=[] #[id_prod, prom_rese,cant_dev]
        prelista=[]
        for i in lifestore_sales:
          prelista.append([i[1],i[2],i[4]])
        #print(prelista)
        print("**************************")

        cnt_res=0
        acum_res=0
        cant_dev=0
        for i in lifestore_sales:
          for a in prelista:
            if i[1]==a[0]:
              cnt_res+=1
              acum_res+=a[1]
              cant_dev+=a[2]
          prom=acum_res/cnt_res
          formato_ideal.append([i[1],prom,cant_dev])
          cnt_res=0
          acum_res=0
          cant_dev=0

        #print(formato_ideal)
        Lista_depurada=[]#[id producto, prom_reseña, cant-dev]
        for i in formato_ideal:
          if i not in Lista_depurada:
            Lista_depurada.append(i)
        print(Lista_depurada, "\n")

        reseñas_ordenadas=[] #se crea una lista vacia donde se almacenarán los registros ordenados [id_producto, cnt_busq]

        #reutilice el codigo de ordenamiento del inciso a
        while Lista_depurada:
          minimo = Lista_depurada[0][1]
          lista_actual = Lista_depurada[0]
          for venta in Lista_depurada:
            if venta[1] > minimo:
              minimo = venta[1]
              lista_actual = venta
          reseñas_ordenadas.append(lista_actual)
          Lista_depurada.remove(lista_actual)

        cnt_loop = 1
        #por cada elemento en busquedas ordenadas iterar en lifestore_products
        print("PRODUCTOS CON MEJORES RESEÑAS")
        for i in reseñas_ordenadas:
          for nombre in lifestore_products:
            if cnt_loop==21:
              break
              #impresión en consola de los resultados
            if i[0] == nombre[0]:
              print("Top ",cnt_loop,"|ID del producto: ", nombre[0]," |Descripción: ", nombre[1]," || |Promedio de reseñas: ", i[1], "|", "Devoluciones: ",i[2])
              print("*********************")
              cnt_loop+=1
      if opcionL=="B" or opcionL=="b":
        formato_ideal=[] #[id_prod, prom_rese,cant_dev]
        prelista=[]#obteniendo datos necesarios para el ordenamiento
        for i in lifestore_sales:
          prelista.append([i[1],i[2],i[4]])
        #print(prelista)
        print("**************************")

        cnt_res=0
        acum_res=0
        cant_dev=0
        for i in lifestore_sales:
          for a in prelista:
            if i[1]==a[0]:
              cnt_res+=1
              acum_res+=a[1]
              cant_dev+=a[2]
          prom=acum_res/cnt_res
          formato_ideal.append([i[1],prom,cant_dev])
          cnt_res=0
          acum_res=0
          cant_dev=0

        #print(formato_ideal)
        Lista_depurada=[]#[id producto, prom_reseña, cant-dev]
        for i in formato_ideal:
          if i not in Lista_depurada:
            Lista_depurada.append(i)

        reseñas_ordenadas=[] #se crea una lista vacia donde se almacenarán los registros ordenados [id_producto, cnt_busq]

        #reutilice el codigo de ordenamiento del inciso a
        while Lista_depurada:
          minimo = Lista_depurada[0][1]
          lista_actual = Lista_depurada[0]
          for venta in Lista_depurada:
            if venta[1] < minimo:
              minimo = venta[1]
              lista_actual = venta
          reseñas_ordenadas.append(lista_actual)
          Lista_depurada.remove(lista_actual)
        res_orden2=[]
        while reseñas_ordenadas:
          minimo = reseñas_ordenadas[0][2]
          lista_actual = reseñas_ordenadas[0]
          for venta in reseñas_ordenadas:
            if venta[1] < minimo:
              minimo = venta[1]
              lista_actual = venta
          res_orden2.append(lista_actual)
          reseñas_ordenadas.remove(lista_actual)
        cnt_loop = 1
        #por cada elemento en busquedas ordenadas iterar en lifestore_products
        print("PRODUCTOS CON PEORES RESEÑAS \n")
        for i in res_orden2:
          for nombre in lifestore_products:
            if cnt_loop==21:
              break
              #impresión en consola de los resultados
            if i[0] == nombre[0]:
              print("Top ",cnt_loop,"|ID del producto: ", nombre[0]," |Descripción: ", nombre[1]," || |Promedio de reseñas: ", i[1], "|", "Devoluciones: ",i[2])
              print("*********************")
              cnt_loop+=1
    
    

else:
    print("Credenciales incorrectas, verifique su información ingresada.")
