import mysql.connector
import datetime

from Classes.Etl import EtlRequest, EtlResponse

class ProcessLog:
    db_param = {"jar_path": "/Layer_gestionale/config/jar/mysql-connector-j-8.0.32.jar", \
                "db_user": "testlab", \
                "db_password": "testlab", \
                "db_url_config": "jdbc:mysql://localhost:3306/lab", \
                "db_driver": "com.mysql.cj.jdbc.Driver"}
    configdb = None

    def __init__(self):
        self.configdb = mysql.connector.connect( \
            host="localhost", \
            user=self.db_param["db_user"], \
            password=self.db_param["db_password"], \
            database="lab")
    def startProcessLog(self, request: EtlRequest):
        process_id = request.processId
        semaforoID = request.semaforo.id
        banca = request.semaforo.abi
        periodoRif = ""
        tabella = ""
        tipoCaricamento = ""
        provenienza = ""
        idFile = ""
        colonnaValore = ""
        oCarico = request.semaforo.oCarico

        # scrivo tabella td_pg_db_log_processi_domini_sg
        configcursor = self.configdb.cursor()
        configcursor.execute(
            "insert into td_pg_db_log_processi_domini_sg (ID_PROCESSO, provenienza, tipo_caricamento, banca, step, num_periodo_rif, des_status, tms_data_ora_inizio, ID_SEMAFORO) values ('" + process_id + "','" + provenienza + "','" + tipoCaricamento + "', '" + str(
                banca) + "','stage','" + str(periodoRif) + "','RUNNING','" + datetime.datetime.now().strftime(
                "%Y/%m/%d %H:%M:%S") + "','" + str(semaforoID) + "')")
        self.configdb.commit()

        # scrivo tabella td_pg_db_log_sottoprocessi
        configcursor = self.configdb.cursor()
        configcursor.execute(
            "insert into td_pg_db_log_sottoprocessi_domini_sg (ID_PROCESSO, provenienza, tipo_caricamento, banca, step, tabella, des_status, tms_data_ora_inizio, ID_SEMAFORO) values ('" + process_id + "','" + provenienza + "','" + tipoCaricamento + "', '" + str(
                banca) + "','stage','" + str(tabella) + "','RUNNING','" + datetime.datetime.now().strftime(
                "%Y/%m/%d %H:%M:%S") + "','" + str(semaforoID) + "')")
        self.configdb.commit()

    def endProcessLog(self, request: EtlRequest, response: EtlResponse):
        process_id = response.processId
        semaforoID = request.semaforo.id
        banca = request.semaforo.abi
        periodoRif = ""
        tabella = ""
        tipoCaricamento = ""
        provenienza = ""
        idFile = ""
        colonnaValore = ""
        oCarico = request.semaforo.oCarico

        error = response.error

        if response.status == 'OK':
            # vado a settare come ok nel log processo e ci metto anche la data di fine
            configcursor = self.configdb.cursor()
            configcursor.execute(
                "update td_pg_db_log_processi_domini_sg set des_status='OK', tms_data_ora_fine='" + datetime.datetime.now().strftime(
                    "%Y/%m/%d %H:%M:%S") + "' where ID_PROCESSO ='" + process_id + "' and step='stage'")
            self.configdb.commit()

            configcursor = self.configdb.cursor()
            configcursor.execute(
                "update td_pg_db_log_sottoprocessi_domini_sg set des_status='OK', tms_data_ora_fine='" + datetime.datetime.now().strftime(
                    "%Y/%m/%d %H:%M:%S") + "' where ID_PROCESSO ='" + process_id + "' and step='stage'")
            self.configdb.commit()

            # genero nuovo record sul log dei processi per far partire il flusso che sposta in dati in silver
            configcursor = self.configdb.cursor()
            configcursor.execute(
                "insert into td_pg_db_log_processi_domini_sg (ID_PROCESSO, provenienza, tipo_caricamento, banca, step, num_periodo_rif, des_status, ID_SEMAFORO) values ('" + process_id + "','" + provenienza + "','" + tipoCaricamento + "', '" + str(
                    banca) + "','silver','" + str(periodoRif) + "','','" + semaforoID + "')")
            self.configdb.commit()

            # verifico se nel registro e' presente la riga
            # oppure devo fare una insert perche' magari hanno aggiunto una
            # provenienza nuova o una banca nuova e non e'
            # stata creata la riga del semaforo
            configcursor = self.configdb.cursor()
            configcursor.execute(
                "select max_data_va, max_id_riga_semaforo td_pg_db_registro_domini_sg where provenienza = '" + provenienza + "' AND banca = '" + banca + "' AND tipo_caricamento='" + tipoCaricamento + "'")
            dbResult = configcursor.fetchone()

            if dbResult is None:
                # faccio insert del registro per dire che abbiamo letto la riga id-esima
                configcursor = self.configdb.cursor()
                configcursor.execute(
                    "insert into td_pg_db_registro_domini_sg (provenienza, tipo_caricamento, banca, max_data_va, max_id_riga_semaforo) values('" + provenienza + "', '" + tipoCaricamento + "', '" + banca + "', '', '" + semaforoID + "')")
                self.configdb.commit()
            else:
                # aggiungo update del registro per dire che abbiamo letto la riga id-esima
                configcursor = self.configdb.cursor()
                configcursor.execute(
                    "update td_pg_db_registro_domini_sg set max_id_riga_semaforo ='" + semaforoID + "' where provenienza = '" + provenienza + "' AND banca = '" + banca + "' AND tipo_caricamento='" + tipoCaricamento + "'")
                self.configdb.commit()
        else:

            # vado a settare come ko nel log processo e ci metto anche la data di fine
            configcursor = self.configdb.cursor()
            configcursor.execute(
                "update td_pg_db_log_processi_domini_sg set des_status='KO', tms_data_ora_fine='" + datetime.datetime.now().strftime(
                    "%Y/%m/%d %H:%M:%S") + "', Note = '" +error+"' where ID_PROCESSO ='" + process_id + "' and step='stage'")
            self.configdb.commit()

            configcursor = self.configdb.cursor()
            configcursor.execute(
                "update td_pg_db_log_sottoprocessi_domini_sg set des_status='KO', tms_data_ora_fine='" + datetime.datetime.now().strftime(
                    "%Y/%m/%d %H:%M:%S") + "', Note = '" +error+"' where ID_PROCESSO ='" + process_id + "' and step='stage'")
            self.configdb.commit()