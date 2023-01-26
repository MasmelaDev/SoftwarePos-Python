from psycopg2 import pool

class Conexion:
    _DATABASE = 'test_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _HOST = '127.0.0.1'
    _DB_PORT = '5432'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerPool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,host= cls._HOST,user=cls._USERNAME, password=cls._PASSWORD, port=cls._DB_PORT,database= cls._DATABASE)

                return cls._pool
            except  Exception as e:
                print(f'Error al obtener el pool: {e}')
        else:
            return cls._pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.obtenerPool().getconn()
        return conexion

    @classmethod
    def liberarConexion(cls,conexion):
        cls.obtenerPool().putconn(conexion)


    @classmethod
    def cerrarConexion(cls):
        cls.obtenerPool().closeall()










