import logging

from Classes.Etl.EtlRequest import EtlRequest
from Classes.Etl.Semaforo import Semaforo
from Classes.Ingestion.BuilderDefault import BuilderDefault
from Classes.Ingestion.BuilderRedent import BuilderRedent
from Utils.constants import TAB_REDENT
from Utils.utils import configure_log, parse_arguments


def switch_classes(request: EtlRequest) -> BuilderDefault:
    if request.semaforo.tabella == TAB_REDENT:
        return BuilderRedent(request)


def getEtlRequestBasedOnArguments(args) -> EtlRequest:
    return EtlRequest(args.p, args.d, Semaforo(args.s.split("|")[0], args.s.split("|")[1],
                                               args.s.split("|")[2])
                      )


if __name__ == '__main__':
    arguments = parse_arguments()
    req = getEtlRequestBasedOnArguments(arguments)

    configure_log()

    cls = switch_classes(req)

    logging.info(str(cls.ingest()))