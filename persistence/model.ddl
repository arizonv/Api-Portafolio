CREATE TABLE Permiso (
    id NUMBER PRIMARY KEY,
    clase VARCHAR2(15) NOT NULL,
    nombre VARCHAR2(50) NOT NULL,
    CONSTRAINT uq_permiso UNIQUE (clase, nombre)
);

CREATE TABLE Rol (
    id NUMBER PRIMARY KEY,
    nombre VARCHAR2(15) UNIQUE NOT NULL
);

CREATE TABLE RolPermiso (
    id NUMBER PRIMARY KEY,
    rol_id NUMBER NOT NULL,
    permiso_id NUMBER NOT NULL,
    CONSTRAINT fk_rol_permiso_rol FOREIGN KEY (rol_id) REFERENCES Rol(id),
    CONSTRAINT fk_rol_permiso_permiso FOREIGN KEY (permiso_id) REFERENCES Permiso(id),
    CONSTRAINT uq_rol_permiso UNIQUE (rol_id, permiso_id)
);

CREATE TABLE Usuario (
    id NUMBER PRIMARY KEY,
    username VARCHAR2(30) UNIQUE NOT NULL,
    name VARCHAR2(20) NOT NULL,
    apellidos VARCHAR2(30) NOT NULL,
    email VARCHAR2(254) UNIQUE NOT NULL,
    is_staff NUMBER(1) DEFAULT 0 NOT NULL,
    is_active NUMBER(1) DEFAULT 1 NOT NULL,
    date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    roles_id NUMBER,
    CONSTRAINT fk_usuario_rol FOREIGN KEY (roles_id) REFERENCES Rol(id)
);

CREATE TABLE Cliente (
    id NUMBER PRIMARY KEY,
    user_id NUMBER UNIQUE NOT NULL,
    rut VARCHAR2(10) NOT NULL,
    sexo VARCHAR2(10) NOT NULL,
    CONSTRAINT fk_cliente_usuario FOREIGN KEY (user_id) REFERENCES Usuario(id)
);

CREATE TABLE Reserva (
    id NUMBER PRIMARY KEY,
    cliente_id NUMBER NOT NULL,
    agenda_id NUMBER NOT NULL,
    dia DATE NOT NULL,
    estado VARCHAR2(20) DEFAULT 'disponible' NOT NULL,
    CONSTRAINT fk_reserva_cliente FOREIGN KEY (cliente_id) REFERENCES Cliente(id),
    CONSTRAINT fk_reserva_agenda FOREIGN KEY (agenda_id) REFERENCES Agenda(id),
    CONSTRAINT uq_reserva UNIQUE (cliente_id, agenda_id, dia)
);

CREATE TABLE Ticket (
    id NUMBER PRIMARY KEY,
    cliente_id NUMBER NOT NULL,
    codigo VARCHAR2(10) NOT NULL,
    fecha_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    reserva_id NUMBER NOT NULL,
    CONSTRAINT fk_ticket_cliente FOREIGN KEY (cliente_id) REFERENCES Cliente(id),
    CONSTRAINT fk_ticket_reserva FOREIGN KEY (reserva_id) REFERENCES Reserva(id)
);

CREATE TABLE Boleta (
    id NUMBER PRIMARY KEY,
    fecha_emision TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    cliente_id NUMBER NOT NULL,
    reserva_id NUMBER NOT NULL,
    total NUMBER(10, 2) NOT NULL,
    CONSTRAINT fk_boleta_cliente FOREIGN KEY (cliente_id) REFERENCES Cliente(id),
    CONSTRAINT fk_boleta_reserva FOREIGN KEY (reserva_id) REFERENCES Reserva(id)
);

CREATE TABLE TipoCancha (
    id NUMBER PRIMARY KEY,
    nombre VARCHAR2(50) NOT NULL,
    precio NUMBER(8) NOT NULL,
    descripcion CLOB
);

CREATE TABLE Cancha (
    id NUMBER PRIMARY KEY,
    numeracion VARCHAR2(10) NOT NULL,
    tipo_id NUMBER NOT NULL,
    CONSTRAINT fk_cancha_tipo FOREIGN KEY (tipo_id) REFERENCES TipoCancha(id)
);

CREATE TABLE Horario (
    id NUMBER PRIMARY KEY,
    hora_inicio TIMESTAMP,
    hora_fin TIMESTAMP,
    meridiem VARCHAR2(2) DEFAULT 'PM' NOT NULL
);

CREATE TABLE Agenda (
    id NUMBER PRIMARY KEY,
    cancha_id NUMBER NOT NULL,
    horario_id NUMBER NOT NULL,
    disponible NUMBER(1) DEFAULT 1 NOT NULL,
    CONSTRAINT fk_agenda_cancha FOREIGN KEY (cancha_id) REFERENCES Cancha(id),
    CONSTRAINT fk_agenda_horario FOREIGN KEY (horario_id) REFERENCES Horario(id)
);
