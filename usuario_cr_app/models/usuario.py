# importar la función que devolverá una instancia de una conexión
from usuario_cr_app.config.mysqlconnection import connectToMySQL
# modelar la clase después de la tabla friend de nuestra base de datos
class Users:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido= data['apellido']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['update_at']

    # ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('Users_Schema').query_db(query)
        # crear una lista vacía para agregar nuestras instancias de friends
        get_usuario = []
        # Iterar sobre los resultados de la base de datos y crear instancias de friends con cls
        for usuarios in results:
            get_usuario.append( cls(usuarios) )
        return get_usuario

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM usuarios WHERE id = %(id_usuario)s;"
        result = connectToMySQL('Users_Schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def delete_one(cls, data):
        query = "DELETE FROM usuarios WHERE id = %(id_usuario)s;"
        return connectToMySQL('Users_Schema').query_db(query,data)

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO usuarios ( nombre, apellido , email , created_at, update_at ) VALUES ( %(fname)s , %(lname)s , %(email)s , NOW() , NOW() );"
        # data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL('Users_Schema').query_db( query, data )

    @classmethod
    def edit_one(cls, data ):
        print("edit_one")
        query = "UPDATE usuarios SET nombre=%(fname)s, apellido=%(lname)s, email= %(email)s, created_at=NOW(), update_at=NOW()  WHERE id = %(id_usuario)s;"
        return connectToMySQL('Users_Schema').query_db( query, data )



