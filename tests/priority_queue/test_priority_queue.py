import pytest
from ting_file_management.priority_queue import PriorityQueue
from ting_file_management.file_process import FileInfo


mock_priority_file_info1: FileInfo = {
    "nome_do_arquivo": "path_file1",
    "qtd_linhas": 4,
    "linhas_do_arquivo": ["text"]
}

mock_priority_file_info2: FileInfo = {
    "nome_do_arquivo": "path_file2",
    "qtd_linhas": 2,
    "linhas_do_arquivo": ["text"]
}

mock_priority_file_info3: FileInfo = {
    "nome_do_arquivo": "path_file3",
    "qtd_linhas": 3,
    "linhas_do_arquivo": ["text"]
}

mock_regular_file_info1: FileInfo = {
    "nome_do_arquivo": "path_file3",
    "qtd_linhas": 5,
    "linhas_do_arquivo": ["text"]
}

mock_regular_file_info2: FileInfo = {
    "nome_do_arquivo": "path_file4",
    "qtd_linhas": 7,
    "linhas_do_arquivo": ["text"]
}

FILE_ENQUEUE_ORDER = [
    mock_priority_file_info3,
    mock_regular_file_info2,
    mock_priority_file_info1,
    mock_regular_file_info1,
    mock_priority_file_info2
]

EXPECTED_DEQUEUE_ORDER = [
    mock_priority_file_info3,
    mock_priority_file_info1,
    mock_priority_file_info2,
    mock_regular_file_info2,
    mock_regular_file_info1
]


def test_basic_priority_queueing():
    # testing the enqueue ad dequeue method
    priority_queue = PriorityQueue()
    for file_info in FILE_ENQUEUE_ORDER:
        priority_queue.enqueue(file_info)
    for file_info in EXPECTED_DEQUEUE_ORDER:
        searched_file = priority_queue.dequeue()
        assert searched_file == file_info

    # Testing the search method
    for file_info in FILE_ENQUEUE_ORDER:
        priority_queue.enqueue(file_info)
    for index in range(len(EXPECTED_DEQUEUE_ORDER)):
        searched_file = priority_queue.search(index)
        assert searched_file == EXPECTED_DEQUEUE_ORDER[index]

    # Testing with invalid index
    with pytest.raises(
        IndexError, match="Índice Inválido ou Inexistente"
    ):
        priority_queue.search(len(priority_queue) + 1)
