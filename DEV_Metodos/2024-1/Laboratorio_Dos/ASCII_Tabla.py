def generate_dict(names, *lists):
    # Crear un diccionario vacío
    result = {}

    # Asignar cada nombre a su lista correspondiente
    for i, name in enumerate(names):
        if i < len(lists):
            result[name] = lists[i]
        else:
            result[name] = []

    return result

def print_ascii_table(data):
    # Calcula el ancho máximo de cada columna
    columns = list(data.keys())
    col_widths = {col: max(len(col), max(len(str(item)) for item in data[col])) for col in columns}

    # Calcula el ancho total de la tabla
    table_width = sum(col_widths.values()) + 3 * (len(columns) - 1) + 4

    # Función auxiliar para crear una línea de separación
    def separator():
        return '+' + '+'.join(['-' * (col_widths[col] + 2) for col in columns]) + '+'

    # Imprime la fila de encabezado
    def print_header():
        header = '| ' + ' | '.join([col.ljust(col_widths[col]) for col in columns]) + ' |'
        print(separator())
        print(header)
        print(separator())

    # Imprime las filas de datos
    def print_rows():
        max_rows = max(len(data[col]) for col in columns)
        for i in range(max_rows):
            row = '| '
            for col in columns:
                value = str(data[col][i]) if i < len(data[col]) else ''
                row += value.ljust(col_widths[col]) + ' | '
            print(row)
        print(separator())

    # Construcción de la tabla
    print_header()
    print_rows()