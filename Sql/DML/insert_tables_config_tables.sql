insert into config_tables values('REDENT','ta_pg_db_entita_mens_sg', NULL, NULL, '(SELECT BANCA, TIPO_ENTITA,DESCRIZIONE,DESCRIZIONE_ESTESA,FLAG_SEGNO,COLORE_ENTITA,COLORE_BORDO,COLORE_PIVOT,FLAG_TIPO_SELEZIONE,TIPO_MODELLO,STATUS_RIGA,DATA_VA,ORA_VA,SPORTELLO_ESEC,OPERATORE,FLAG_MULTIBANCA,FLAG_GESTIONE_DOMINI,DATA_LENGTH,DATA_LENGTH_PADRE,FLAG_STORICIZZA, row_number() over(order by BANCA) as ROW_N FROM REDENT WHERE 1=1 {additional_where})as subquery','{"db_host": "localhost", "db_name": "RDBP0_DOMINI", "db_user": "teo", "db_password": "Matteo1981"}','{"db_user": "teo", "db_driver": "com.mysql.cj.jdbc.Driver", "db_password": "Matteo1981", "db_url_input": "jdbc:mysql://localhost:3306/RDBP0_DOMINI"}',NULL);