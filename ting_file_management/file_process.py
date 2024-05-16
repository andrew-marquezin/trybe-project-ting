import sys

from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    processed_file = False
    for file in instance.queue:
        if file["nome_do_arquivo"] == path_file:
            processed_file = True
            break

    lines = txt_importer(path_file)
    item = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines),
        "linhas_do_arquivo": lines
    }

    if not processed_file:
        instance.enqueue(item)
    print(item)


def remove(instance):
    if instance.__len__() > 0:
        file_name = instance.dequeue()["nome_do_arquivo"]
        print(f"Arquivo {file_name} removido com sucesso")
    else:
        print("Não há elementos")


def file_metadata(instance, position):
    try:
        print(instance.search(position))
    except IndexError:
        print("Posição inválida", file=sys.stderr)
