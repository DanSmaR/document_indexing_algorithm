import sys
from typing import TypeVar, TypedDict, List
from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer

T = TypeVar("T")


class FileInfo(TypedDict):
    nome_do_arquivo: str
    qtd_linhas: int
    linhas_do_arquivo: List[str]


def process(path_file: str, queue: Queue[FileInfo]) -> None:
    text_list = txt_importer(path_file)
    if not text_list:
        raise RuntimeError("There is no file to process")

    is_in_queue = check_node_in_queue(path_file, queue)
    if not is_in_queue:
        file_info: FileInfo = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(text_list),
            "linhas_do_arquivo": text_list
        }
        queue.enqueue(file_info)
        print(file_info, file=sys.stdout)


def check_node_in_queue(
        path_file: str,
        queue: Queue[FileInfo],
) -> bool:
    is_in_queue = False
    for index in range(len(queue)):
        queue_node = queue.search(index)
        if not queue_node:
            continue
        if queue_node.get("nome_do_arquivo") == path_file:
            is_in_queue = True
            break
    return is_in_queue


def remove(queue: Queue[FileInfo]):
    if queue.is_empty():
        print("Não há elementos", file=sys.stdout)
        return None
    file_removed = queue.dequeue()
    print(f"Arquivo {file_removed['nome_do_arquivo']} removido com sucesso")


def file_metadata(queue: Queue[FileInfo], position):
    """Aqui irá sua implementação"""
