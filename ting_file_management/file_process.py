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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
