from typing import List, TypedDict
from ting_file_management.queue import Queue
from ting_file_management.file_process import FileInfo


class LineOcurrence(TypedDict):
    linha: int


class ExistWordResultInfo(TypedDict):
    palavra: str
    arquivo: str
    ocorrencias: List[LineOcurrence]


def exists_word(word: str, queue: Queue[FileInfo]):
    lowered_word = word.lower()
    exists_word_result_list: List[ExistWordResultInfo] = []
    if len(queue) == 0:
        return []
    check_word_in_files_info(
        word,
        queue,
        lowered_word,
        exists_word_result_list
    )
    return exists_word_result_list


def check_word_in_files_info(
        word: str,
        queue: Queue[FileInfo],
        lowered_word: str,
        exists_word_result_list: List[ExistWordResultInfo]
):
    for index in range(len(queue)):
        exists_word_result: ExistWordResultInfo = {
            'palavra': "",
            'arquivo': "",
            'ocorrencias': []
        }
        file_info = queue.search(index)
        if not file_info:
            continue
        check_word_in_lines(lowered_word, exists_word_result, file_info)
        if len(exists_word_result['ocorrencias']) == 0:
            continue
        exists_word_result['palavra'] = word
        exists_word_result['arquivo'] = file_info['nome_do_arquivo']
        exists_word_result_list.append(exists_word_result.copy())


def check_word_in_lines(
        lowered_word: str,
        exists_word_result: ExistWordResultInfo,
        file_info: FileInfo
):
    for line, text in enumerate(file_info['linhas_do_arquivo']):
        if lowered_word not in text.lower():
            continue
        exists_word_result['ocorrencias'].append({'linha': line + 1})


def search_by_word(word: str, queue: Queue[FileInfo]):
    """Aqui irá sua implementação"""
