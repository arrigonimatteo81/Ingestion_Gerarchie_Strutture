import json
import sys
from types import SimpleNamespace


from Classes.Ingestion.BuilderDefault import BuilderDefault
from Classes.Ingestion.BuilderRedent import BuilderRedent
from Classes.Ingestion.BuilderRedpvi import BuilderRedpvi
from Classes.Ingestion.BuilderRedstr import BuilderRedstr
from Classes.Ingestion.BuilderRedven import BuilderRedven
from Classes.ProcessLog.ProcessLog import ProcessLog
from Etl.EtlRequestStrutture import EtlRequestStrutture
from Process.SubProcessLogStrutture import SubProcessLogStrutture
from Registro.RegistroStrutture import RegistroStrutture
from Utils.constants import TAB_REDENT, TAB_REDVEN, TAB_REDSTR, TAB_REDPVI
from Utils.utils import configure_log


def switch_classes(request: EtlRequestStrutture) -> BuilderDefault:
    if request.semaforo.tabella == TAB_REDENT:
        return BuilderRedent(request)
    if request.semaforo.tabella == TAB_REDVEN:
        return BuilderRedven(request)
    if request.semaforo.tabella == TAB_REDSTR:
        return BuilderRedstr(request)
    if request.semaforo.tabella == TAB_REDPVI:
        return BuilderRedpvi(request)


#def getEtlRequestBasedOnArguments(args) -> EtlRequestStrutture:
#    return EtlRequestStrutture(args.p, SemaforoStrutture(args.s.split("|")[0], args.s.split("|")[1],
#                                       args.s.split("|")[2])
#                      )


if __name__ == '__main__':
    # codice commentato, io mi passo un json in input es. {\"processId\":\"1\",\"semaforo\":{\"id\":\"1\", \"abi\":\"1025\"}}
    #arguments = parse_arguments()
    #req = getEtlRequestBasedOnArguments(arguments)
    jsonEtlRequest = sys.argv[1]
    req = json.loads(jsonEtlRequest, object_hook=lambda d: SimpleNamespace(**d))
    subprocessLog = SubProcessLogStrutture()

    if not subprocessLog.SubprocessIsRunning(req):
        subprocessLog.InitSubprocessLog(req)

        configure_log()

        cls = switch_classes(req)

        etlResponse = cls.ingest()

        if etlResponse.status == 'OK':
            subprocessLog.CloseSubprocessLogOK(etlResponse)
            registro = RegistroStrutture
            registro.upsertRegistro(banca=req.semaforo.abi, tabella=req.semaforo.tabella,
                                    semaforo_id=req.semaforo.id)
        else:
            subprocessLog.CloseSubprocessLogKO(etlResponse)