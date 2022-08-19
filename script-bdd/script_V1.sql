/*==============================================================*/
/* DBMS name:      PostgreSQL 8                                 */
/* Created on:     08-05-2022 20:26:14                          */
/*==============================================================*/


drop table DOMO_AFORO;

drop table DOMO_CIUDAD;

drop index INDEX_APELLIDOCLI;

drop table DOMO_CLIENTE;

drop table DOMO_DIRECCION;

drop index INDEX_APELLIDO_ENC;

drop table DOMO_ENCARGADORTR;

drop index INDEX_NUM_MESA;

drop table DOMO_MESA;

drop table DOMO_REGION;

drop table DOMO_RESERVA;

drop table DOMO_RESTAURANTE;

drop index INDEX_TIPID;

drop table DOMO_TIPOUSUARIO;

drop table DOMO_USUARIO;

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
   CLI_ID               SERIAL               not null,
   RSV_ID               INT4                 null,
   USR_ID               INT4                 null,
   CLI_NOMBRE           VARCHAR(40)          null,
   CLI_APELLIDO         VARCHAR(40)          null,
   CLI_TIPO             CHAR                 null,
   CLI_RUT              INT4                 null,
   constraint PK_DOMO_CLIENTE primary key (CLI_ID)
);

/*==============================================================*/
/* Index: INDEX_APELLIDOCLI                                     */
/*==============================================================*/
create  index INDEX_APELLIDOCLI on DOMO_CLIENTE (
( CLI_APELLIDO )
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
   constraint PK_DOMO_ENCARGADORTR primary key (ENC_ID)
);

/*==============================================================*/
/* Index: INDEX_APELLIDO_ENC                                    */
/*==============================================================*/
create  index INDEX_APELLIDO_ENC on DOMO_ENCARGADORTR (
( ENC_APELLIDO )
);

/*==============================================================*/
/* Table: DOMO_MESA                                             */
/*==============================================================*/
create table DOMO_MESA (
   MSA_ID               SERIAL               not null,
   RTR_ID               INT4                 null,
   MSA_CAPACIDAD        INT4                 null,
   MSA_NUMERO           INT4                 null,
   MSA_DESCRIPCION      VARCHAR(50)          null,
   constraint PK_DOMO_MESA primary key (MSA_ID)
);

/*==============================================================*/
/* Index: INDEX_NUM_MESA                                        */
/*==============================================================*/
create  index INDEX_NUM_MESA on DOMO_MESA (
( MSA_NUMERO )
);

/*==============================================================*/
/* Table: DOMO_REGION                                           */
/*==============================================================*/
create table DOMO_REGION (
   REG_ID               SERIAL not null,
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
   RSV_HORA             TIME                 null,
   RSV_FECHA            DATE                 null,
   RSV_ASISTENCIA       BOOL                 null,
   RSV_FECHADEREGISTRO  DATE                 null,
   constraint PK_DOMO_RESERVA primary key (RSV_ID)
);

/*==============================================================*/
/* Table: DOMO_RESTAURANTE                                      */
/*==============================================================*/
create table DOMO_RESTAURANTE (
   RTR_ID               SERIAL               not null,
   DIR_ID               INT4                 null,
   RTR_NOMBRE           VARCHAR(50)          null,
   RTR_DESCRIPCION      VARCHAR(100)         null,
   TPR_ID               INT4                 null,
   RTR_CARTA            VARCHAR(100)         null,
   RTR_OPVEGE           BOOL                 null,
   RTR_OPVEGA           BOOL                 null,
   RTR_NOMBREDUENO      VARCHAR(40)          null,
   RTR_APELLIDODUENO    VARCHAR(40)          null,
   constraint PK_DOMO_RESTAURANTE primary key (RTR_ID)
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
/* Index: INDEX_TIPID                                           */
/*==============================================================*/
create unique index INDEX_TIPID on DOMO_TIPOUSUARIO (
( TIP_ID )
);

/*==============================================================*/
/* Table: DOMO_USUARIO                                          */
/*==============================================================*/
create table DOMO_USUARIO (
   USR_ID               SERIAL               not null,
   TIP_ID               INT4                 null,
   USR_LOGIN            VARCHAR(20)          null,
   USR_CONTRASENA       VARCHAR(18)          null,
   constraint PK_DOMO_USUARIO primary key (USR_ID)
);
drop table DOMO_HORARIO;

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
   HOR_DISPONIBILIDAD   BOOL                 null,
   constraint PK_DOMO_HORARIO primary key (HOR_ID)
);

alter table DOMO_HORARIO
   add constraint FK_DOMO_HOR_REFERENCE_DOMO_RES foreign key (RTR_ID)
      references DOMO_RESTAURANTE (RTR_ID)
      on delete restrict on update restrict;

/*==============================================================*/
/* Table: DOMO_TIPORESTAURANTE                                  */
/*==============================================================*/

create table DOMO_TIPORESTAURANTE (
   TPR_ID               SERIAL               not null,
   TPR_NOMBRE           VARCHAR(20)          null,
   TPR_DESCRIPCION      TEXT                 null,
   constraint PK_DOMO_TIPO_RESTAURANTE primary key (TIP_ID)
);

/*==============================================================*/
/* Table: DOMO_HORARIO                                          */
/*==============================================================*/

create table DOMO_HORARIO(
   HOR_ID               SERIAL               not null,
   RTR_ID               INT4                 null,
   HOR_DIAINICIO        INT4                 null,
   HOR_DIATERMINO       INT4                 null,
   HOR_HORAINICIO       TIME                 null,
   HOR_HORATERMINO      TIME                 null,
   HOR_ASISTENCIA       BOOL                 null,
   constraint PK_DOMO_HORARIO primary key (HOR_ID)
);

/*==============================================================*/
/* Table: DOMO_TIPODEPAGO                                       */
/*==============================================================*/

create table DOMO_TIPODEPAGO(
   TPG_ID               SERIAL               not null,
   TPG_ETIQUETA         VARCHAR(30)          null,
   TPG_DESCRIPCION      VARCHAR(50)          null,
   constraint PK_DOMO_TIPODEPAGO primary key (TDP_ID)
);

alter table DOMO_HORARIO
   add constraint FK_DOMO_HORARIO_DOMO_RESTAURANTE foreign key (RTR_ID)
      references DOMO_RESTAURANTE (RTR_ID)
      on delete restrict on update restrict;


alter table DOMO_AFORO
   add constraint FK_DOMO_AFO_REFERENCE_DOMO_RES foreign key (RTR_ID)
      references DOMO_RESTAURANTE (RTR_ID)
      on delete restrict on update restrict;

alter table DOMO_CIUDAD
   add constraint FK_DOMO_CIU_REFERENCE_DOMO_REG foreign key (REG_ID)
      references DOMO_REGION (REG_ID)
      on delete restrict on update restrict;

alter table DOMO_CLIENTE
   add constraint FK_DOMO_CLI_REFERENCE_DOMO_RES foreign key (RSV_ID)
      references DOMO_RESERVA (RSV_ID)
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

alter table DOMO_MESA
   add constraint FK_DOMO_MES_REFERENCE_DOMO_RES foreign key (RTR_ID)
      references DOMO_RESTAURANTE (RTR_ID)
      on delete restrict on update restrict;

alter table DOMO_RESERVA
   add constraint FK_DOMO_RES_REFERENCE_DOMO_MES foreign key (MSA_ID)
      references DOMO_MESA (MSA_ID)
      on delete restrict on update restrict;

alter table DOMO_RESTAURANTE
   add constraint FK_DOMO_RES_REFERENCE_DOMO_DIR foreign key (DIR_ID)
      references DOMO_DIRECCION (DIR_ID)
      on delete restrict on update restrict;

alter table DOMO_RESTAURANTE
   add constraint FK_DOMO_RES_REFERENCE_DOMO_TPR foreign key (TPR_ID)
      references DOMO_TIPORESTAURANTE (TPR_ID)
      on delete restrict on update restrict;

alter table DOMO_USUARIO
   add constraint FK_DOMO_USU_REFERENCE_DOMO_TIP foreign key (TIP_ID)
      references DOMO_TIPOUSUARIO (TIP_ID)
      on delete restrict on update restrict;

