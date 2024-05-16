import pytest

from ting_file_management.priority_queue import PriorityQueue


mock = [
        {
            "nome_do_arquivo": "mock1.txt",
            "qtd_linhas": 7,
            "linhas_do_arquivo": [
                "Lorem ipsum dolor sit amet",
                "Nullam pharetra nibh fringilla posuere ullamcorper",
                "Nullam pulvinar neque consectetur tortor ultrices",
                "Praesent mollis sagittis diam",
                "Mauris quis dignissim tellus",
                "Aliquam molestie mollis nibh",
                "Phasellus feugiat felis id lorem porttitor"
            ]
        },
        {
            "nome_do_arquivo": "mock2.txt",
            "qtd_linhas": 3,
            "linhas_do_arquivo": [
                "Donec risus urna, efficitur in nisi fringilla",
                "In vulputate enim id lectus egestas",
                "Suspendisse ipsum lectus"
            ]
        }
    ]


def test_basic_priority_queueing():
    instance = PriorityQueue()
    assert len(instance) == 0

    instance.enqueue(mock[0])
    assert len(instance) == 1
    assert len(instance.regular_priority) == 1

    instance.enqueue(mock[1])
    assert len(instance) == 2
    assert len(instance.high_priority) == 1
    assert instance.search(0) == mock[1]
    assert instance.search(1) == mock[0]

    with pytest.raises(IndexError):
        instance.search(3)

    instance.dequeue()
    assert len(instance) == 1
    assert len(instance.high_priority) == 0

    instance.dequeue()
    assert len(instance) == 0
    assert len(instance.regular_priority) == 0
