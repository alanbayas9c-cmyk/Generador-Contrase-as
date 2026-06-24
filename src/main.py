import random
import string
import os
from datetime import datetime

# ==============================
# HISTORIAL
# ==============================
historial = []

# ==============================
# LIMPIAR PANTALLA
# ==============================

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

# ==============================
# GENERADORES
# ==============================

def generar_basica():
    return "ABC123"

def generar_segura():
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(12))

def generar_personalizada(longitud):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(longitud))

# ==============================
# EVALUAR SEGURIDAD
# ==============================

def evaluar_fortaleza(password):
    tiene_minuscula = any(c.islower() for c in password)
    tiene_mayuscula = any(c.isupper() for c in password)
    tiene_numero = any(c.isdigit() for c in password)
    tiene_simbolo = any(c in string.punctuation for c in password)

    puntos = sum([tiene_minuscula, tiene_mayuscula, tiene_numero, tiene_simbolo])

    if len(password) < 8:
        return "❌ Débil"
    elif puntos == 2:
        return "⚠️ Media"
    elif puntos >= 3:
        return "🔥 Fuerte"
    else:
        return "❌ Débil"

# ==============================
# HISTORIAL
# ==============================

def ver_historial():
    if not historial:
        print("❌ No hay contraseñas aún.")
        return

    print("\n===== HISTORIAL =====")
    for i, item in enumerate(historial, 1):
        print(f"{i}. {item['password']} | {item['fecha']} | {item['seguridad']}")

def guardar_archivo():
    if not os.path.exists("historial"):
        os.makedirs("historial")

    with open("historial/historial.txt", "w") as file:
        for item in historial:
            file.write(f"{item['password']} | {item['fecha']} | {item['seguridad']}\n")

    print("✔ Historial guardado correctamente")

# ==============================
# GUARDAR CONTRASEÑA
# ==============================

def guardar(password):
    historial.append({
        "password": password,
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "seguridad": evaluar_fortaleza(password)
    })

# ==============================
# MENÚ PRINCIPAL
# ==============================

def menu():
    while True:
        limpiar()

        print("=========================================")
        print("      🔐 GENERADOR DE CONTRASEÑAS PRO")
        print("=========================================")
        print("1. Generar contraseña básica")
        print("2. Generar contraseña segura")
        print("3. Generar contraseña personalizada")
        print("4. Ver historial")
        print("5. Guardar historial en archivo")
        print("6. Salir")

        opcion = input("\nSelecciona una opción: ")

        # ==========================
        # OPCIÓN 1
        # ==========================
        if opcion == "1":
            password = generar_basica()
            print("\n🔑 Contraseña:", password)
            print("🔐 Seguridad:", evaluar_fortaleza(password))
            guardar(password)
            input("\nPresiona ENTER para continuar...")

        # ==========================
        # OPCIÓN 2
        # ==========================
        elif opcion == "2":
            password = generar_segura()
            print("\n🔑 Contraseña:", password)
            print("🔐 Seguridad:", evaluar_fortaleza(password))
            guardar(password)
            input("\nPresiona ENTER para continuar...")

        # ==========================
        # OPCIÓN 3
        # ==========================
        elif opcion == "3":
            try:
                longitud = int(input("Ingresa la longitud: "))
                password = generar_personalizada(longitud)
                print("\n🔑 Contraseña:", password)
                print("🔐 Seguridad:", evaluar_fortaleza(password))
                guardar(password)
            except:
                print("❌ Ingresa un número válido")

            input("\nPresiona ENTER para continuar...")

        # ==========================
        # OPCIÓN 4
        # ==========================
        elif opcion == "4":
            ver_historial()
            input("\nPresiona ENTER para continuar...")

        # ==========================
        # OPCIÓN 5
        # ==========================
        elif opcion == "5":
            guardar_archivo()
            input("\nPresiona ENTER para continuar...")

        # ==========================
        # OPCIÓN 6
        # ==========================
        elif opcion == "6":
            print("\n👋 Saliendo del sistema...")
            break

        else:
            print("\n❌ Opción inválida")
            input("\nPresiona ENTER para continuar...")

# ==============================
# EJECUTAR PROGRAMA
# ==============================

menu()
