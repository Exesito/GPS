/*==============================================================*/
/* DBMS name:      PostgreSQL 8                                 */
/* Created on:     06-08-2022 18:28:08                          */
/*==============================================================*/


drop table DOMO_AFORO cascade;

drop table DOMO_CARTA cascade;

drop table DOMO_CIUDAD cascade;

drop table DOMO_CLIENTE cascade;

drop table DOMO_DIRECCION cascade;

drop table DOMO_ENCARGADORTR cascade;

drop table DOMO_HORARIO cascade;

drop table DOMO_MESA cascade;

drop table DOMO_REGION cascade;

drop table DOMO_RESERVA cascade;

drop table DOMO_RESTAURANTE cascade;

drop table DOMO_TIPODEPAGO cascade;

drop table DOMO_TIPORESTAURANTE cascade;

drop table DOMO_TIPOUSUARIO cascade;

drop table DOMO_USUARIO cascade;

drop table DOMO_VALORACION cascade;

/*==============================================================*/
/* Table: DOMO_AFORO                                            */
/*==============================================================*/
create table DOMO_AFORO (
   AFO_ID               SERIAL               not null,
   RTR_ID               INT4                 null,
   AFO_CAPACIDADMAX     INT4                 null,
   AFO_CAPACIDADACTUAL  INT4                 null,
   constraint PK_DOMO_AFORO primary key (AFO_ID)
);

/*==============================================================*/
/* Table: DOMO_CARTA                                            */
/*==============================================================*/
create table DOMO_CARTA (
   CAR_ID               SERIAL               not null,
   RTR_ID               INT4                 null,
   CAR_NOMBRE           VARCHAR(20)          null,
   CAR_URL              VARCHAR(255)         null,
   CAR_ACTIVA           BOOL                 null,
   constraint PK_DOMO_CARTA primary key (CAR_ID)
);

/*==============================================================*/
/* Table: DOMO_CIUDAD                                           */
/*==============================================================*/
create table DOMO_CIUDAD (
   CIU_ID               SERIAL               not null,
   REG_ID               INT4                 null,
   CIU_NOMBRE           VARCHAR(40)          not null,
   constraint PK_DOMO_CIUDAD primary key (CIU_ID)
);

/*==============================================================*/
/* Table: DOMO_CLIENTE                                          */
/*==============================================================*/
create table DOMO_CLIENTE (
   CLI_ID               INT4                 not null,
   USR_ID               INT4                 null,
   DIR_ID               INT4                 null,
   CLI_NOMBRE           VARCHAR(40)          null,
   CLI_APELLIDO         VARCHAR(40)          null,
   CLI_TIPO             CHAR                 null,
   CLI_TELEFONO         INT4                 null,
   CLI_RUT              VARCHAR(13)          null,
   constraint PK_DOMO_CLIENTE primary key (CLI_ID)
);

/*==============================================================*/
/* Table: DOMO_DIRECCION                                        */
/*==============================================================*/
create table DOMO_DIRECCION (
   DIR_ID               SERIAL               not null,
   CIU_ID               INT4                 null,
   DIR_NOMBRECALLE      VARCHAR(50)          null,
   DIR_NUMEROCALLE      INT4                 null,
   constraint PK_DOMO_DIRECCION primary key (DIR_ID)
);

/*==============================================================*/
/* Table: DOMO_ENCARGADORTR                                     */
/*==============================================================*/
create table DOMO_ENCARGADORTR (
   USR_ID               INT4                 null,
   RTR_ID               INT4                 null,
   ENC_ID               SERIAL               not null,
   ENC_NOMBRE           VARCHAR(40)          null,
   ENC_APELLIDO         VARCHAR(40)          null,
   ENC_RUT              VARCHAR(13)          null,
   constraint PK_DOMO_ENCARGADORTR primary key (ENC_ID)
);

/*==============================================================*/
/* Table: DOMO_HORARIO                                          */
/*==============================================================*/
create table DOMO_HORARIO (
   HOR_ID               SERIAL               not null,
   RTR_ID               INT4                 null,
   HOR_DIAINICIO        INT4                 null,
   HOR_DIATERMINO       INT4                 null,
   HOR_HORAINICIO       TIME                 null,
   HOR_HORATERMINO      TIME                 null,
   HOR_NOMBRE           VARCHAR(20)          null,
   HOR_ACTIVO           BOOL                 null,
   constraint PK_DOMO_HORARIO primary key (HOR_ID)
);

/*==============================================================*/
/* Table: DOMO_MESA                                             */
/*==============================================================*/
create table DOMO_MESA (
   MSA_ID               SERIAL               not null,
   RTR_ID               INT4                 null,
   MSA_NUMERO           INT4                 null,
   MSA_CAPACIDAD        INT4                 null,
   MSA_DESCRIPCION      TEXT                 null,
   constraint PK_DOMO_MESA primary key (MSA_ID)
);

/*==============================================================*/
/* Table: DOMO_REGION                                           */
/*==============================================================*/
create table DOMO_REGION (
   REG_ID               SERIAL               not null,
   REG_NOMBRE           VARCHAR(30)          not null,
   constraint PK_DOMO_REGION primary key (REG_ID)
);

/*==============================================================*/
/* Table: DOMO_RESERVA                                          */
/*==============================================================*/
create table DOMO_RESERVA (
   RSV_ID               SERIAL               not null,
   MSA_ID               INT4                 null,
   TPG_ID               INT4                 null,
   CLI_ID               INT4                 null,
   RSV_HORA             TIME                 null,
   RSV_FECHA            DATE                 null,
   RSV_ESTADO           VARCHAR(30)          null,
   RSV_FECHADEREGISTRO  DATE                 null,
   constraint PK_DOMO_RESERVA primary key (RSV_ID)
);

/*==============================================================*/
/* Table: DOMO_RESTAURANTE                                      */
/*==============================================================*/
create table DOMO_RESTAURANTE (
   RTR_ID               SERIAL               not null,
   DIR_ID               INT4                 null,
   TPR_ID               INT4                 null,
   RTR_NOMBRE           VARCHAR(50)          null,
   RTR_DESCRIPCION      TEXT                 null,
   RTR_OPVEGA           BOOL                 null,
   RTR_OPVEGE           BOOL                 null,
   RTR_DUENONOMBRE      VARCHAR(40)          null,
   RTR_DUENOAPELLIDO    VARCHAR(40)          null,
   constraint PK_DOMO_RESTAURANTE primary key (RTR_ID)
);

/*==============================================================*/
/* Table: DOMO_TIPODEPAGO                                       */
/*==============================================================*/
create table DOMO_TIPODEPAGO (
   TPG_ID               SERIAL               not null,
   TPG_ETIQUETA         VARCHAR(30)          null,
   TPG_DESCRIPION       VARCHAR(50)          null,
   constraint PK_DOMO_TIPODEPAGO primary key (TPG_ID)
);

/*==============================================================*/
/* Table: DOMO_TIPORESTAURANTE                                  */
/*==============================================================*/
create table DOMO_TIPORESTAURANTE (
   TPR_ID               SERIAL               not null,
   TPR_NOMBRE           VARCHAR(40)          null,
   TPR_DESCRIPCION      TEXT                 null,
   constraint PK_DOMO_TIPORESTAURANTE primary key (TPR_ID)
);

/*==============================================================*/
/* Table: DOMO_TIPOUSUARIO                                      */
/*==============================================================*/
create table DOMO_TIPOUSUARIO (
   TIP_ID               SERIAL               not null,
   TIP_NOMBRE           VARCHAR(20)          null,
   TIP_DESCRIPCION      TEXT                 null,
   constraint PK_DOMO_TIPOUSUARIO primary key (TIP_ID)
);

/*==============================================================*/
/* Table: DOMO_USUARIO                                          */
/*==============================================================*/
create table DOMO_USUARIO (
   USR_ID               SERIAL               not null,
   TIP_ID               INT4                 null,
   USR_LOGIN            VARCHAR(40)          null,
   USR_CONTRASENA       VARCHAR(80)          null,
   USR_ESTADO           VARCHAR(20)          null,
   constraint PK_DOMO_USUARIO primary key (USR_ID)
);

/*==============================================================*/
/* Table: DOMO_VALORACION                                       */
/*==============================================================*/
create table DOMO_VALORACION (
   VAL_ID               SERIAL               not null,
   RSV_ID               INT4                 null,
   VAL_TITULO           VARCHAR(30)          null,
   VAL_DESCRIPCION      TEXT                 null,
   VAL_ESTRELLA         FLOAT4               null,
   constraint PK_DOMO_VALORACION primary key (VAL_ID)
);

alter table DOMO_AFORO
   add constraint FK_DOMO_AFO_REFERENCE_DOMO_RES foreign key (RTR_ID)
      references DOMO_RESTAURANTE (RTR_ID)
      on delete restrict on update restrict;

alter table DOMO_CARTA
   add constraint FK_DOMO_CAR_REFERENCE_DOMO_RES foreign key (RTR_ID)
      references DOMO_RESTAURANTE (RTR_ID)
      on delete restrict on update restrict;

alter table DOMO_CIUDAD
   add constraint FK_DOMO_CIU_REFERENCE_DOMO_REG foreign key (REG_ID)
      references DOMO_REGION (REG_ID)
      on delete restrict on update restrict;

alter table DOMO_CLIENTE
   add constraint FK_DOMO_CLI_REFERENCE_DOMO_DIR foreign key (DIR_ID)
      references DOMO_DIRECCION (DIR_ID)
      on delete restrict on update restrict;

alter table DOMO_CLIENTE
   add constraint FK_DOMO_CLI_REFERENCE_DOMO_USU foreign key (USR_ID)
      references DOMO_USUARIO (USR_ID)
      on delete restrict on update restrict;

alter table DOMO_DIRECCION
   add constraint FK_DOMO_DIR_REFERENCE_DOMO_CIU foreign key (CIU_ID)
      references DOMO_CIUDAD (CIU_ID)
      on delete restrict on update restrict;

alter table DOMO_ENCARGADORTR
   add constraint FK_DOMO_ENC_REFERENCE_DOMO_RES foreign key (RTR_ID)
      references DOMO_RESTAURANTE (RTR_ID)
      on delete restrict on update restrict;

alter table DOMO_ENCARGADORTR
   add constraint FK_DOMO_ENC_REFERENCE_DOMO_USU foreign key (USR_ID)
      references DOMO_USUARIO (USR_ID)
      on delete restrict on update restrict;

alter table DOMO_HORARIO
   add constraint FK_DOMO_HOR_REFERENCE_DOMO_RES foreign key (RTR_ID)
      references DOMO_RESTAURANTE (RTR_ID)
      on delete restrict on update restrict;

alter table DOMO_MESA
   add constraint FK_DOMO_MES_REFERENCE_DOMO_RES foreign key (RTR_ID)
      references DOMO_RESTAURANTE (RTR_ID)
      on delete restrict on update restrict;

alter table DOMO_RESERVA
   add constraint FK_DOMO_RES_REFERENCE_DOMO_TIP foreign key (TPG_ID)
      references DOMO_TIPODEPAGO (TPG_ID)
      on delete restrict on update restrict;

alter table DOMO_RESERVA
   add constraint FK_DOMO_RES_REFERENCE_DOMO_MES foreign key (MSA_ID)
      references DOMO_MESA (MSA_ID)
      on delete restrict on update restrict;

alter table DOMO_RESERVA
   add constraint FK_DOMO_RES_REFERENCE_DOMO_CLI foreign key (CLI_ID)
      references DOMO_CLIENTE (CLI_ID)
      on delete restrict on update restrict;

alter table DOMO_RESTAURANTE
   add constraint FK_DOMO_RES_REFERENCE_DOMO_TIP foreign key (TPR_ID)
      references DOMO_TIPORESTAURANTE (TPR_ID)
      on delete restrict on update restrict;

alter table DOMO_RESTAURANTE
   add constraint FK_DOMO_RES_REFERENCE_DOMO_DIR foreign key (DIR_ID)
      references DOMO_DIRECCION (DIR_ID)
      on delete restrict on update restrict;

alter table DOMO_USUARIO
   add constraint FK_DOMO_USU_REFERENCE_DOMO_TIP foreign key (TIP_ID)
      references DOMO_TIPOUSUARIO (TIP_ID)
      on delete restrict on update restrict;

alter table DOMO_VALORACION
   add constraint FK_DOMO_VAL_REFERENCE_DOMO_RES foreign key (RSV_ID)
      references DOMO_RESERVA (RSV_ID)
      on delete restrict on update restrict;

