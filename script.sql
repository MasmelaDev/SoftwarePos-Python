CREATE SCHEMA IF NOT EXISTS softwarePos_db;


CREATE TABLE IF NOT EXISTS softwarePos_db.clientes (
  telefono VARCHAR(11) NOT NULL,
  nombre VARCHAR(45) NULL,
  direccion VARCHAR(45) NULL,
  barrio VARCHAR(45) NULL,
  PRIMARY KEY (telefono));



CREATE TABLE IF NOT EXISTS ventas (
  id_ventas INT NOT NULL,
  cliente VARCHAR(45) NOT NULL,
  total VARCHAR(45) NOT NULL,
  pedido VARCHAR(45) NOT NULL,
  PRIMARY KEY (id_ventas));



CREATE TABLE IF NOT EXISTS pendientes (
  id_ventas INT NOT NULL,
  cliente VARCHAR(45) NOT NULL,
  total VARCHAR(45) NOT NULL,
  pedido VARCHAR(45) NOT NULL,
  domiciliario VARCHAR(45) NULL,
  PRIMARY KEY (id_ventas));


