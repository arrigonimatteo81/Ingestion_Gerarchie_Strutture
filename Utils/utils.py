import argparse
import logging
import logging.handlers
import time


def configure_log():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s:%(levelname)s:%(message)s"
    )
    logging.getLogger("py4j").setLevel(logging.INFO)
    logging.Formatter.converter = time.gmtime


def parse_arguments():
    # EtlRequest("mio_id_processo", 20230101,Semaforo("id_da_semaforo", 3239, 202301, "READDR", "Rapporti", "MY", None, None, None))
    parser = argparse.ArgumentParser(description='Data ingestion')
    parser.add_argument("--p", help="Process ID")
    parser.add_argument("--s", help="Semaforo")

    return parser.parse_args()
