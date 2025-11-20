import sys

def generar_gramatica_atributos(arch, esquema):
    f = open(arch, "r")
    base = f.read()
    f.close()


    if "atributos=" in esquema:
        partes = esquema.split("atributos=")
        tablas_txt = partes[0].replace("tablas", "").replace(",", "").strip()
        atributos_txt = partes[1].strip()
    else:
        tablas_txt = esquema
        atributos_txt = ""

   
    tablas = tablas_txt.split()
    atributos = atributos_txt.split(",")

    
    nueva = base

  
    nueva = nueva.replace(
        "create",
        "create returns [String code, boolean valid]"
    )
    nueva = nueva.replace(
        "CREATE TABLE ID LPAREN listaCampos RPAREN",
        "CREATE TABLE ID LPAREN listaCampos RPAREN { $code = $text; $valid = true; }"
    )

    # insert
    nueva = nueva.replace(
        "INSERT INTO ID LPAREN listaCampos RPAREN VALUES LPAREN listaValores RPAREN",
        "INSERT INTO ID LPAREN listaCampos RPAREN VALUES LPAREN listaValores RPAREN { $code = $text; $valid = true; }"
    )

    # select
    nueva = nueva.replace(
        "read",
        "read returns [String code, boolean valid]"
    )
    nueva = nueva.replace(
        "SELECT listaCampos FROM ID",
        "SELECT listaCampos FROM ID { $code = $text; $valid = true; }"
    )

    # update
    nueva = nueva.replace(
        "update",
        "update returns [String code, boolean valid]"
    )
    nueva = nueva.replace(
        "UPDATE ID SET listaAsignaciones",
        "UPDATE ID SET listaAsignaciones { $code = $text; $valid = true; }"
    )

    # delete
    nueva = nueva.replace(
        "delete",
        "delete returns [String code, boolean valid]"
    )
    nueva = nueva.replace(
        "DELETE FROM ID",
        "DELETE FROM ID { $code = $text; $valid = true; }"
    )
    nueva = nueva.replace(
        "DROP TABLE ID",
        "DROP TABLE ID { $code = $text; $valid = true; }"
    )

    out = open("gramatica_generada.g4", "w")
    out.write(nueva)
    out.close()

    return "gramatica_generada.g4"


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("uso: python3 Punto1.py archivo esquema")
        sys.exit(0)

    arch = sys.argv[1]
    esquema = " ".join(sys.argv[2:])

    gen = generar_gramatica_atributos(arch, esquema)
    print("archivo generado:", gen)
