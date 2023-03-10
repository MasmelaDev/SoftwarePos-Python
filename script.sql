CREATE SCHEMA IF NOT EXISTS softwarePos_db;


CREATE TABLE IF NOT EXISTS softwarePos_db.clientes (
  telefono VARCHAR(11) NOT NULL,
  nombre VARCHAR NULL,
  direccion VARCHAR NULL,
  barrio VARCHAR NULL,
  PRIMARY KEY (telefono));



CREATE TABLE IF NOT EXISTS softwarePos_db.ventas (
  id_ventas INT NOT NULL,
  cliente VARCHAR NOT NULL,
  total INT NOT NULL,
  pedido VARCHAR NOT NULL,
  PRIMARY KEY (id_ventas));



CREATE TABLE IF NOT EXISTS softwarePos_db.pendientes (
  id_ventas INT NOT NULL,
  cliente VARCHAR NOT NULL,
  total INT NOT NULL,
  pedido VARCHAR NOT NULL,
  domiciliario VARCHAR(45) NULL,
  PRIMARY KEY (id_ventas));


