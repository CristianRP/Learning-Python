import textwrap


direccion = "3a. Avenida 9-00 Interior Finca El Zapote, Zona 2, Guatemala, Guatemala"

departamentos = ['Alta Verapaz','Baja Verapaz','Chimaltenango','Chiquimula','El Progreso',
'Escuintla','Guatemala','Huehuetenango','Izabal','Jalapa','Jutiapa','Petén','Quetzaltenango',
'Quiché','Retalhuleu','Sacatepéquez','San Marcos','Santa Rosa','Sololá','Suchitepéquez',
'Totonicapán','Zacapa']


def search_zona(direccion):
    no_zona = 0
    for i in direccion:
        if ('Zona' in i.strip()):
            zona = i.split("Zona")
            for x in zona:
                if x != None:
                    no_zona = x
    return no_zona


def search_departamento(direccion):
    count = 0
    departamento = ''
    for i in range(len(direccion)):
        if (direccion[i].strip() in departamentos):
            count += 1
            if (count > 1):
                departamento = direccion[count]
            else:
                departamento = direccion[count + 1]

    return departamento

def search_avenida(direccion):
    direccion = direccion[:12]
    return direccion

def search_calle(direccion):
    direccion = direccion[12:]
    return direccion

def search_no_casa(direccion):
    direccion = direccion[12:]
    direccion = direccion[:4]
    return direccion

def search_colonia(direccion):
    direccion = direccion[len(direccion)-10:]
    return direccion

def determinar_direccion(direccion):
    direccion = direccion.split(",")
    print('Avenida: {0}'.format(search_avenida(direccion[0])))
    print('Calle: {0}'.format(search_calle(direccion[0])))
    print('Número de casa: {0}'.format(search_no_casa(direccion[0])))
    print('Colonia: {0}'.format(search_colonia(direccion[0])))
    search_colonia(direccion[0])
    print('Zona: {0}'.format(search_zona(direccion)))
    print('Municipio: {0}'.format(direccion[2]))
    print('Departamento: {0}'.format(search_departamento(direccion)))

determinar_direccion(direccion)