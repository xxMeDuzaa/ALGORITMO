class TablaHash:
    def __init__(self, size):
        """
        1. create_table(size). Crea y devuelve una tabla hash vacía con la cantidad de elementos
        determinada por el tamaño ingresado.
        """
        self.size = size
        self.table = [None] * size
        self.element_count = 0

    def hash_string(self, codigo: str) -> int:
        """
        Función de hash de Bernstein para cadenas.
        """
        h = 0
        for caracter in codigo:
            h = h * 33 + ord(caracter)
        # Se aplica el operador módulo al resultado de Bernstein para obtener la posición.
        return h % self.size

    def hash_numerica(self, numero: int) -> int:
        """
        Función de hash por división para números.
        """
        # Se aplica el operador módulo sobre el tamaño de la tabla.
        return numero % self.size
    
    def hash_function(self, data):
        """
        5. funcion_hash(data, table_size). Devuelve la posición que le corresponde al dato.
        Esta función elige el algoritmo de hash según el tipo de dato de la clave.
        """
        if isinstance(data, str):
            # Si el dato es una cadena, se usa la función de hash de Bernstein.
            return self.hash_string(data)
        elif isinstance(data, int):
            # Si el dato es un número entero, se usa la función de hash numérica.
            return self.hash_numerica(data)
        else:
            # En caso de otros tipos de datos, se puede agregar una función de hash por defecto.
            # Aquí se usa una versión simple como fallback.
            return hash(data) % self.size

    def probe_function(self, position):
        """
        6. sondeo(position, table_size). Devuelve la nueva posición para resolver colisiones.
        """
        return (position + 1) % self.size

    def add(self, data):
        """
        2. add(table, data). Agrega el elemento a la tabla.
        """
        position = self.hash_function(data)
        
        while self.table[position] is not None:
            position = self.probe_function(position)
        
        self.table[position] = data
        self.element_count += 1
        
    def remove(self, data):
        """
        3. remove(table, data). Elimina y devuelve el elemento.
        """
        position = self.hash_function(data)
        start_position = position
        
        while self.table[position] is not None:
            if self.table[position] == data:
                self.table[position] = None
                self.element_count -= 1
                # En este punto se necesitaría una lógica de reubicación para los elementos colisionados,
                # como se menciona en el documento[cite: 98, 99].
                return data
            
            position = self.probe_function(position)
            if position == start_position:
                break
                
        return None

    def search(self, data):
        """
        4. search(table, data). Devuelve la posición del elemento.
        """
        position = self.hash_function(data)
        start_position = position
        
        while self.table[position] is not None:
            if self.table[position] == data:
                return position
            
            position = self.probe_function(position)
            if position == start_position:
                break
        
        return None

    def count_elements(self):
        """
        7. quantity_elements(table). Devuelve la cantidad de elementos.
        """
        return self.element_count