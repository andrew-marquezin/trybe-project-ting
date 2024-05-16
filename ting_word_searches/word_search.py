def exists_word(word, instance):
    existing = []

    for file in instance.queue:
        occurencies = [
            {"linha": index + 1}
            for index, line in enumerate(file["linhas_do_arquivo"])
            if word.lower() in line.lower()
        ]

        if len(occurencies) == 0:
            return []

        existing.append({
            "palavra": word,
            "arquivo": file["nome_do_arquivo"],
            "ocorrencias": occurencies
        })

    return existing


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
