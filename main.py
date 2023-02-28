import json
import sys
from os import path
from types import SimpleNamespace

from Classes.Ingestion.BuilderDefault import BuilderDefault
from Classes.Ingestion.BuilderRedent import BuilderRedent
from Classes.Ingestion.BuilderRedpvi import BuilderRedpvi
from Classes.Ingestion.BuilderRedstr import BuilderRedstr
from Classes.Ingestion.BuilderRedven import BuilderRedven
from Classes.ProcessLog.ProcessLog import ProcessLog
from Utils.constants import TAB_REDENT, TAB_REDVEN, TAB_REDSTR, TAB_REDPVI
from Utils.utils import configure_log

sys.path.append(path.abspath("../Classes"))
from Classes.Etl.EtlRequestStrutture import EtlRequestStrutture


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

    processLog = ProcessLog()
    processLog.startProcessLog(req)
    configure_log()

    cls = switch_classes(req)

    etlResponse = cls.ingest()
    processLog.endProcessLog(req, etlResponse)
