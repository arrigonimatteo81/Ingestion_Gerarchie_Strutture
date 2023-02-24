insert into config_tables values('REDENT','td_pg_db_entita_mens_sg', NULL, NULL, '(SELECT BANCA, TIPO_ENTITA,DESCRIZIONE,DESCRIZIONE_ESTESA,FLAG_SEGNO,COLORE_ENTITA,COLORE_BORDO,COLORE_PIVOT,FLAG_TIPO_SELEZIONE,TIPO_MODELLO,STATUS_RIGA,DATA_VA,ORA_VA,SPORTELLO_ESEC,OPERATORE,FLAG_MULTIBANCA,FLAG_GESTIONE_DOMINI,DATA_LENGTH,DATA_LENGTH_PADRE,FLAG_STORICIZZA, row_number() over(order by BANCA) as ROW_N FROM REDENT WHERE 1=1 {additional_where})as subquery','{"db_host": "localhost", "db_name": "RDBP0_DOMINI", "db_user": "teo", "db_password": "Matteo1981"}','{"db_user": "teo", "db_driver": "com.mysql.cj.jdbc.Driver", "db_password": "Matteo1981", "db_url_input": "jdbc:mysql://localhost:3306/RDBP0_DOMINI"}',NULL, 'DOMINIO');
insert into config_tables values('REDVEN','td_pg_db_dominio_sg', NULL, 100, '(SELECT BANCA, TIPO_ENTITA, COD_ENTITA, DESCRIZIONE_VAL_ENTITA, DESCRIZIONE_ESTESA, FLAG_TERMINALE, STATUS_RIGA, DATA_VA, ORA_VA, SPORTELLO_ESEC, OPERATORE, row_number() over(order by BANCA) as ROW_N FROM REDVEN WHERE 1=1 {additional_where})as subquery','{"db_host": "localhost", "db_name": "RDBP0_DOMINI", "db_user": "teo", "db_password": "Matteo1981"}','{"db_user": "teo", "db_driver": "com.mysql.cj.jdbc.Driver", "db_password": "Matteo1981", "db_url_input": "jdbc:mysql://localhost:3306/RDBP0_DOMINI"}','SELECT count(1) from REDVEN WHERE 1=1 {additional_where}', 'DOMINIO');
insert into config_tables values('REDSTR','td_pg_db_struttura_sg', NULL, 100, '(SELECT BANCA, TIPO_ENTITA, PUNTO_DI_VISTA, COD_ENTITA, COD_ENTITA_FIGLIO, PROGRESSIVO, SEGNO, STATUS_RIGA, DATA_VA, ORA_VA, SPORTELLO_ESEC, OPERATORE, row_number() over(order by BANCA) as ROW_N FROM REDSTR WHERE 1=1 {additional_where})as subquery','{"db_host": "localhost", "db_name": "RDBP0_DOMINI", "db_user": "teo", "db_password": "Matteo1981"}','{"db_user": "teo", "db_driver": "com.mysql.cj.jdbc.Driver", "db_password": "Matteo1981", "db_url_input": "jdbc:mysql://localhost:3306/RDBP0_DOMINI"}','SELECT count(1) from REDSTR where 1=1 {additional_where}', 'DOMINIO');
insert into config_tables values('REDPVI','td_pg_db_punti_vista_domini_sg', NULL, NULL, '(SELECT BANCA, TIPO_ENTITA, PUNTO_DI_VISTA, PUBBLICO, DESCRIZIONE_P_VISTA, STATUS_RIGA, FLAG_PC,DATA_VA, ORA_VA, SPORTELLO_ESEC, OPERATORE, row_number() over(order by banca) as ROW_N FROM REDPVI WHERE 1=1 {additional_where})as subquery','{"db_host": "localhost", "db_name": "RDBP0_DOMINI", "db_user": "teo", "db_password": "Matteo1981"}','{"db_user": "teo", "db_driver": "com.mysql.cj.jdbc.Driver", "db_password": "Matteo1981", "db_url_input": "jdbc:mysql://localhost:3306/RDBP0_DOMINI"}','SELECT count(1) from REDPVI where 1=1 {additional_where}', 'DOMINIO');
#TODO nome tabella corretto
insert into config_tables values('REDCLD','TODO', NULL, NULL, '(SELECT BANCA,COD_DATO,CLASSE_DATO,TIPO_DATO,LUNG_DATO,DECIM_DATO,CAMPO_DB,FLAG_MESE_PREC,PERIODI_CONSERVAZ,TIPO_ENTITA,FLAG_RAGGRUPPA,FLAG_TRASCINA,FLAG_TEMPO,row_number() over(order by banca) as ROW_N FROM REDCLD WHERE 1=1 {additional_where})as subquery','{"db_host": "localhost", "db_name": "RDBP0_DOMINI", "db_user": "teo", "db_password": "Matteo1981"}','{"db_user": "teo", "db_driver": "com.mysql.cj.jdbc.Driver", "db_password": "Matteo1981", "db_url_input": "jdbc:mysql://localhost:3306/RDBP0_DOMINI"}','SELECT count(1) from REDCLD where 1=1 {additional_where}', 'DOMINIO');



