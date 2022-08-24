insert into DOMO_REGION (REG_ID, REG_NOMBRE) values (1, 'F2WW1Y2M9XQXDUEJPDDQCMBDK1C082');

insert into DOMO_REGION (REG_ID, REG_NOMBRE) values (0, 'C1ADH3DLPLR OUWFUNQK5HHDXEVML2');

insert into DOMO_CIUDAD (CIU_ID, REG_ID, CIU_NOMBRE) values (1, 1, 'B3XB1B85KW JIYDACW7YUJ32JI4Y84HAVPJKPBO0');

insert into DOMO_CIUDAD (CIU_ID, REG_ID, CIU_NOMBRE) values (0, 1, '9Y JWFDCP05QYTY01YYO3H8JWATICCMAJULGYPWP');

insert into DOMO_DIRECCION (DIR_ID, CIU_ID, DIR_NOMBRECALLE, DIR_NUMEROCALLE) values (1, 1, 'QOAQ8Q4LVD3WQMX52DNTCQI1OK9Q9L8XYCVHPKO5XOW7HFP8H6', 1);

insert into DOMO_DIRECCION (DIR_ID, CIU_ID, DIR_NOMBRECALLE, DIR_NUMEROCALLE) values (0, 1, 'MUJQQBINCCPJ X5AV7F15N6G11UKV5G6FATII5S5432J1MGHM9', 0);

insert into DOMO_TIPOUSUARIO (TIP_ID, TIP_NOMBRE, TIP_DESCRIPCION) values (1, 'N850GYR8TMTIB7A6KFIJ', '37KNKUO8SVCCKQ2RCQJTHN5L4 BQJE6QOIKSG9QDKCF8 Q9A7SR C1RQ550JS4H54519LF1AH 1FP5A4KRS0Y8KBC0QT2T283DIF L2T85AUBJQSAHHIQAMO01E4RDHHIH75EPASNDVR438NFU9GV0U3OUDI5BE7N2ROEB8UYDXW9OF E 2D9RCN67MC8UHN1SDLBOGLL 7COT0 U6C0NM4FM0NHTUFXGHS 9NJKD7WN1OORPS5OKBBDDDF4HRY');

insert into DOMO_TIPOUSUARIO (TIP_ID, TIP_NOMBRE, TIP_DESCRIPCION) values (0, '0Q440N0VW6WSPKFWTC89', '504995T3487TPS57C7GY B62B5IHVLSV82WLBOCRMKA9V8NDMWUU1XAI2VUYTAQW3825EA478XX2WCDYEIVF8AAUASVDDI3XGI5Q59M647QLW03UG5KUI0JAJDCXEX T01QSPK2DAJIRFRAUD45P4J14BH39527EDCL7H18KPD7 G12XP4Y7R2GM066J966M06NGE9NL7FV8CY6 X1I4HJ22XSQJSB0FBN1IRNE9IOT VG3 D1GNTRVU8Y3I9BH');

insert into DOMO_TIPORESTAURANTE (TPR_ID, TPR_NOMBRE, TPR_DESCRIPCION) values (1, 'GFA7AWY9NMKO9HC3NR8JRYT4YTNY5V15A8OWXAWT', 'LENDRKJ268BAQAIRULX0VMUVL63H3WFBNREG 29AYCPA6I9WJM73GXIE890RAC6B8LH68B6P4C1OU28MODOD30UP5O2YO8KS8IFBO36PPHRE21F8O2XBNJ47BV9AV DKGBV0VXXRMCF NCF3Q8PXF ADKJSJUW3IL7O3T7MCMRSDTLKJ1NYP2JXPPNXX11UH9KTSU 6YGUS658TYNCPQN7APCH7C76EE 4F S576QYFHOHQTJO6LOR8Y2J73MY7');

insert into DOMO_TIPORESTAURANTE (TPR_ID, TPR_NOMBRE, TPR_DESCRIPCION) values (0, 'K08BC6YH1D0V3KFXC6CFX5 I0090NOV2WQGI5V4C', 'LPP GYQ2CR4J5W7RSMMUK5 0W2MCJ7BH3RQ TLVGFFLO1JP6 2YAIDDJ7IND6E2NLL CXGY D7 IP6HYAKXH2Q5EOM HICVHEJW 995B49X6 IN6PHQ3P9ICI6J2SMCJ5YG85CO62 OAGY9VF943KLOX42WU0F19PH6SOPQ2QS1QKJEW1MDYN4WO9F1 YNM19T4TP2MH0EAVG 84CCAGPSG0WFI08UP28UTTUOMR1L9H4NY8EE7V99O8CGGX651');

insert into DOMO_TIPODEPAGO (TPG_ID, TPG_ETIQUETA, TPG_DESCRIPION) values (1, 'UYUTBLJJASE1TB1CNR2VRBX50FOJ95', 'Q0RXY0SHDRYKTVAVAR5IY0XXF9P90 BBPGXO6Y40VB4STFHA8E');

insert into DOMO_TIPODEPAGO (TPG_ID, TPG_ETIQUETA, TPG_DESCRIPION) values (0, 'PLEPFEJDMH20S1OSLLXTN0QJH65WIX', 'VH9YX8XMOKL17LYEGH93QGSFT8XC3YEGA4WAW8J44G T6CM74Y');

insert into DOMO_USUARIO (USR_ID, TIP_ID, USR_LOGIN, USR_CONTRASENA, USR_ESTADO) values (1, 0, 'XOJHYGHAXY35LX9VWR8H', 'PESYG6YNO7CDKRT0WOWL6LVXJL8J9LPXDY8A05FGBI2TFBHV3WXIYYS9SFH6C7YUWJSSJPLUAT2TOISA', '6LS2DKN6ICVCYQ1DAGTM');

insert into DOMO_USUARIO (USR_ID, TIP_ID, USR_LOGIN, USR_CONTRASENA, USR_ESTADO) values (0, 1, 'E622YY4FTVXGNL1V8WXG', 'C2U OCB74WOBOYQTN6NJ4IHI0HTOCN13YQ55B7KB5AP8TIQRFYUB3YGBDIQO6DV7XUP0Q4HX2R2DQJ7J', 'VKH11W8TAOXXFB89SL1 ');

insert into DOMO_RESTAURANTE (RTR_ID, DIR_ID, TPR_ID, RTR_NOMBRE, RTR_DESCRIPCION, RTR_OPVEGA, RTR_OPVEGE, RTR_DUENONOMBRE, RTR_DUENOAPELLIDO) values (1, 0, 0, 'BHNWBVA2DMNWSQK5W51O42MRBF8EQ1GVPQMFTPOUVC4OTP49GB', 'TBLSS7V4SGBH0JXRRYC3RM81BE518JTIO3UC U55B69QEADA8VC3RF8BVJEQ2KJUQ9 18KDMF7A472P IF4KGMWYWHTH90M5UHADISKRQY6H9RN274B1PQUH52 M0ETDA7NRM7WD7QFO7H099C6XBMTWV 9IJI02QNOQCSPO9K4KQNRX17MS0EQRNMKKUDBB9TLTDTFIP932A 2TDK75EHM4I7H6XDWODHBJ8SP8RFR4BH7CE45L1IPMURBUO35', true, true, 'P0H6P5DOCRBCPBHCDH0 1UHNQ9D1DA7CCJJ5T181', 'X0J8WMQW90DJXU83LK17A8NGGX97 9GU1KGC3AKP');

insert into DOMO_RESTAURANTE (RTR_ID, DIR_ID, TPR_ID, RTR_NOMBRE, RTR_DESCRIPCION, RTR_OPVEGA, RTR_OPVEGE, RTR_DUENONOMBRE, RTR_DUENOAPELLIDO) values (0, 1, 1, 'WA 3RK0WE186JCGH2G1RI4H7ODE5WU5BIA MIYKXO9IR36QMLE', '02WTJJR3ENDPR27S32 VFCOBV62PW7D1MCXULR7EIG2MDPXB1GB5C7M0BJI4OE3LGYT0KHH66HH78H3QBGPJBO6FPJHG0KXOYWO LGKTN9701UPE9GBOP3L4OL2S56MABVSC5MY0W1UIMCA1YGE41YN2LQCYNXHVH7CNX1OYQO016QTQ827B8XMLOOHUBMB97WNAYYA6RPDV4WX2QO1ODSCGVSO378FP1L1LJPWO9BM59WPYX88FYJ6UY14EQVO', true, true, '9GEB5KM32OK1A5P19323R65P3RL1I3V31VDAL2FM', 'W2RQ4685LI83D9 REIDXUDER5U22QXRQLOOX5ET1');

insert into DOMO_AFORO (AFO_ID, RTR_ID, AFO_CAPACIDADMAX, AFO_CAPACIDADACTUAL) values (1, 0, 1, 1);

insert into DOMO_AFORO (AFO_ID, RTR_ID, AFO_CAPACIDADMAX, AFO_CAPACIDADACTUAL) values (0, 1, 0, 0);

insert into DOMO_HORARIO (HOR_ID, RTR_ID, HOR_DIAINICIO, HOR_DIATERMINO, HOR_HORAINICIO, HOR_HORATERMINO, HOR_NOMBRE, HOR_ACTIVO) values (1, 1, 1, 0, '0:0:0', '0:0:0', 'VCBQIL0FHD1R7I9XWKKD', true);

insert into DOMO_HORARIO (HOR_ID, RTR_ID, HOR_DIAINICIO, HOR_DIATERMINO, HOR_HORAINICIO, HOR_HORATERMINO, HOR_NOMBRE, HOR_ACTIVO) values (0, 1, 0, 1, '1:25:43', '1:38:1', 'KPV6GMXTDKPS644X4CN9', true);

insert into DOMO_MESA (MSA_ID, RTR_ID, MSA_NUMERO, MSA_CAPACIDAD, MSA_DESCRIPCION) values (1, 1, 0, 1, 'UUH47J6OIYHK0KSHRYYRJDLWWLJA1WAYAQWXU2DHFYK25F2CAAVQTHABU428IOWIM9MGPU0IEVKR3JB200WLWSSGDPBJFI6HHQW5MM10R0XD1PE96J0JIC1LW514B2I0SNHW8UH84PSYWD8JDGU55W4V8GKAIK92RNP0WJDADKN2EOQBEFED2V2EEQQR30WMUJG5SGT7PAOL0BT1FDCNDAY3QAYM XWHU83FWYWWLPGV0SJXTBTQWUXWSJ2GUMS');

insert into DOMO_MESA (MSA_ID, RTR_ID, MSA_NUMERO, MSA_CAPACIDAD, MSA_DESCRIPCION) values (0, 1, 1, 0, 'ERWIDY3R7RW8NH3W6BGIW9X5LH5K53Y2  S7TFLKU70N191XXT5MPWKSU TF2 IBS2B45OQIJAE MYYQ4MUW6 F19PH3YIH4AX2R3RKURKKYA WEP99MRGU7DF8NXHS4UPR6QJRU1V5WFIL4GJ6LA4SIK39NMHW0OWBYMNLQOFYNTHE04IK4 IYB6106XU2G08R6PJ3X0LXJLPACCMK4HWMWFSYU9P25XOCHCEUQ637HCN BLGG VEQOH9UUD0G');

insert into DOMO_CARTA (CAR_ID, RTR_ID, CAR_NOMBRE, CAR_URL, CAR_ACTIVA) values (1, 1, 'NS7D0OLLWX2BIHUGECG8', '2GGX0X24EKNCA183LWV51GHAW90PBNLUC9C5FCABAKBD47UI15CMOA5TPWLOC2GCXX7RQ0QI1ID CTOA7POFFDAALIIYN552TOLD7G9GJ4PMQ2K9 3F7OR PSP6IK39HUF1MD97DDW8R88UK2J6G5NUIAR18OAWIIQ6X19GXXV P4SFTVXJMRF0HUKLWW9OG8SLPBEE3CUXOYBO1OS41RM5W2PC6GPU 2GY8LRYCM63VJLLMICLXOXGD9GVPSH2', true);

insert into DOMO_CARTA (CAR_ID, RTR_ID, CAR_NOMBRE, CAR_URL, CAR_ACTIVA) values (0, 1, 'IDKOSYRAF Q3RNB GTHH', '9 AXQJMNIGYKA JMD4FPGB5PYJNRXNLLRNF993EGTCWGVP9SJ4J4PRA43TULB257FIQOVHNWXLDUJCYLRVTNKDIJNR924DI7MVOYF641XBDY V161I53 T49VVQSL45F1QEXT0OH8BNXXI23TYX8O0K5GDTIU7O9UWQEP2DDR8I1YSQIYYCYC5HMF9N XSWLK049QMEBRIXHIHW1QY65LRNKBE1YQBPU7EOFHE3KYCML0OLXR8UPVL G CI86H8', true);

insert into DOMO_ENCARGADORTR (USR_ID, RTR_ID, ENC_ID, ENC_NOMBRE, ENC_APELLIDO, ENC_RUT) values (0, 0, 1, 'THMMOK9QH6NYAQH0I1FQDS9JBL3XBD6BLSU4EOJ9', 'AF5PODJLWFOSTT4KKMFAVVVKNR7VHC8WA1XS9ACW', 'GAECVCOTWAI4U');

insert into DOMO_ENCARGADORTR (USR_ID, RTR_ID, ENC_ID, ENC_NOMBRE, ENC_APELLIDO, ENC_RUT) values (1, 1, 0, 'XU2Q1LF5VD8U99RDSH6NBAK748ELCOANOYD39EB1', 'VW8VOEL6ESEXXCE2UVB5F54GEMIHUV9QR0JWNBMN', '89MIYIYBIC5SR');

insert into DOMO_CLIENTE (CLI_ID, USR_ID, DIR_ID, CLI_NOMBRE, CLI_APELLIDO, CLI_RUT, CLI_TELEFONO, CLI_CORREO) values (1, 0, 1, 'TXP73TSBNU7FNHD59QTWSQD09VV9YRJ8INVNBMUR', 'WMLNNY33309L EQ0K3VKRLM HSQYYX7Y0FVX6SN2', 'PWEH6B9S2G36Y', 1, 'S3JGGFDM0MXMGDBD1LP1MM MQDJFOQTQRATE066P88X PPW SW');

insert into DOMO_CLIENTE (CLI_ID, USR_ID, DIR_ID, CLI_NOMBRE, CLI_APELLIDO, CLI_RUT, CLI_TELEFONO, CLI_CORREO) values (0, 1, 1, 'N66S7DHO65HM9D7RMRKH78KLQASAB2O  J57U6H9', 'IL 15FXQ300Y4HGH2TAELBGGNKK4VIMERT505JYG', 'YBCDDPLCI UC9', 0, 'J9FP8 CUDX6KYCNHPNAD8LLRDQ56RMN98SONE2F0V5GOH3WFSP');

insert into DOMO_RESERVA (RSV_ID, MSA_ID, TPG_ID, CLI_ID, RSV_HORA, RSV_FECHA, RSV_ESTADO, RSV_FECHADEREGISTRO) values (1, 1, 1, 0, '1:43:33', '1441-11-26', 'SH84VXDP3VHW4RIYX0O03M0GMPVOR2', '676-7-22');

insert into DOMO_RESERVA (RSV_ID, MSA_ID, TPG_ID, CLI_ID, RSV_HORA, RSV_FECHA, RSV_ESTADO, RSV_FECHADEREGISTRO) values (0, 1, 1, 1, '0:0:0', '1-1-1', ' 9L4D5257297JKG349TL9JJIX63NRI', '1-1-1');

insert into DOMO_VALORACION (VAL_ID, RSV_ID, VAL_TITULO, VAL_DESCRIPCION, VAL_ESTRELLA) values (1, 0, '03LT1A7ER98SD2VKH89V0JSMLH4WIA', 'XTSPY9OWLMSJFES80K62S9BRWJCSRR5Q29EHH5DG1L7DQGX5P UNRY0XF6VVOW3YSUWNJCDFYIAE2 56OLWBWBMXYC0CMP9 AAE89S3XGFBYIT9C7V40K9GX6ABYIHWIVUB3DGT8ST06XTVWNUODWTTFXTM8 L2G1AKTBCS1CQH1QVKFM250N1U648BJBIT F GT4J36OR881XTSTMJ45XM6YC1XGM2MTRM9J3RUJ169MWY2457TIL3TPLYB0FN', 0);

insert into DOMO_VALORACION (VAL_ID, RSV_ID, VAL_TITULO, VAL_DESCRIPCION, VAL_ESTRELLA) values (0, 1, 'A2B8PRISWW27 5ASQC0X2H9L3FQS9R', 'VP X5J7XCD138LCVNK828U91RO4MR5APQORX4CBU695LR4HNO3HMSA5NF7UONO2G1ONBWWL582LM8EVB1GEHFFFKR0 LIHPY8HGX8CSQ9WH28W9U07NWSE07QE13GHKACCQ9SR1JH5PGB1OGC8QMO666VXBLLICOXUUHD2PQRP  74GFDXW8TOE59QV32DYI12 EQ5ENDTRJJD68X 5S3QH1I9LA4QODAF0IRS2Q759N1WQHCJC692HWPD3IX60', 1);

