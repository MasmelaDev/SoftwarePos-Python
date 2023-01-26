from Conexion import Conexion


class CursorDelPool:

    def __init__(self):
        self._conn = None
        self._cursor = None

    def __enter__(self):
        self._conn = Conexion.obtenerConexion()
        self._cursor = self._conn.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self._conn.rollback()
            print(f'Error, rollback {exc_val}{exc_type} {exc_tb}')

        else:
            self._conn.commit()
        self._cursor.close()
        Conexion.liberarConexion(self._conn)
