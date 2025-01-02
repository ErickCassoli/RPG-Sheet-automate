from pymongo import MongoClient

client = MongoClient("mongodb://root:example@mongodb_container:27017/")
db = client["ORDEM_PARANORMAL_RPG"]
collection = db["origens"]
collection.create_index("nome", unique=True)



origem = {
    "nome": "Academico",
    "pericias": ["ciencias","investigacao"],
    "habilidade": {
        "nome": "Saber é Poder",
        "custo": "2PE",
        "pagina": "16OP",
        "descritivo": "+5 em testes de INT."
    }
}
origem2 = {
    "nome": "Agente De Saúde",
    "pericias": ["intuicao","medicina"],
    "habilidade": {
        "nome": "Técnica Medicinal",
        "custo": "0PE",
        "pagina": "16OP",
        "descritivo": "Adiciona INT quando curar."
    }
}
origem3 = {
    "nome": "Amigo Dos Animais",
    "pericias": ["adestramento","percepcao"],
    "habilidade": {
        "nome": "Saber é Poder",
        "custo": "2PE",
        "pagina": "7SH",
        "descritivo": "+5 em testes de INT."
    }
}
origem4 = {
    "nome": "Amnésico",
    "pericias": ["adestramento","percepcao"],
    "habilidade": {
        "nome": "Vislimbres Do Passado",
        "custo": "0PE",
        "pagina": "16OP",
        "descritivo": "Recebe 1d4PE. Relembre o passado. INT(DT10)."
    }
}
origem5 = {
    "nome": "Artista",
    "pericias": ["artes","enganacao"],
    "habilidade": {
        "nome": "Magnum Opus",
        "custo": "0PE",
        "pagina": "17OP",
        "descritivo": "+5 em PRE contra um personagem escolhido."
    }
}
origem6 = {
    "nome": "Astronauta",
    "pericias": ["ciencias","fortitude"],
    "habilidade": {
        "nome": "Acostumado Ao Extremo",
        "custo": "1PE",
        "pagina": "8SH",
        "descritivo": "Reduz dano fogo, frio ou mental em 5."
    }
}
origem7 = {
    "nome": "Atleta",
    "pericias": ["acrobacia","atletismo"],
    "habilidade": {
        "nome": "110%",
        "custo": "2PE",
        "pagina": "17OP",
        "descritivo": "+5 em testes de FOR ou AGI (luta e pontaria não)."
    }
}
origem8 = {
    "nome": "Chef",
    "pericias": ["fortitude","profissao"],
    "habilidade": {
        "nome": "Ingrediente Secreto",
        "custo": "0PE",
        "pagina": "17OP",
        "descritivo": "Beneficio de 2 pratos em interlúdio ao cozinhar."
    }
}
origem9 = {
    "nome": "Chef Do Outro Lado",
    "pericias": ["ocultismo","profissao"],
    "habilidade": {
        "nome": "Fome Do Outro Lado",
        "custo": "0PE",
        "pagina": "8SH",
        "descritivo": "Comer prato paranormal fornece RD10 ou vulnerabilidade."
    }
}
origem10 = {
    "nome": "Colegial",
    "pericias": ["atualidades","tecnologia"],
    "habilidade": {
        "nome": "Poder Da Amizade",
        "custo": "0PE",
        "pagina": "9SH",
        "descritivo": "+2 em testes de perícia perto do melhor amigo."
    }
}
origem11 = {
    "nome": "Cosplayer",
    "pericias": ["artes","vontade"],
    "habilidade": {
        "nome": "Não é fantasia, é cosplay!",
        "custo": "0PE",
        "pagina": "9SH",
        "descritivo": "Troca enganação por artes em testes. +2 em teste com relação a fanatasia."
    }
}
origem12 = {
    "nome": "Criminoso",
    "pericias": ["crime","furtividade"],
    "habilidade": {
        "nome": "O Crime Compensa",
        "custo": "0PE",
        "pagina": "17OP",
        "descritivo": "Escolhe um item no final de uma missão para levar para prox."
    }
}
origem13 = {
    "nome": "Cultista Arrependido",
    "pericias": ["ocultismo","religiao"],
    "habilidade": {
        "nome": "Traços Do Outro Lado",
        "custo": "0PE",
        "pagina": "18OP",
        "descritivo": "+1 poder paranormal inicial. Sacrifica metade da sanidade."
    }
}
origem14 = {
    "nome": "Desgarrado",
    "pericias": ["fortitude","sobrevivencia"],
    "habilidade": {
        "nome": "Calejado",
        "custo": "0PE",
        "pagina": "18OP",
        "descritivo": "+1 PV para cada 5% de NEX."
    }
}
origem15 = {
    "nome": "Diplomata",
    "pericias": ["atualidades","diplomacia"],
    "habilidade": {
        "nome": "Traços Do Outro Lado",
        "custo": "2PE",
        "pagina": "9SH",
        "descritivo": "+2 em diplomacia."
    }
}
origem16 = {
    "nome": "Engenheiro",
    "pericias": ["profissao","tecnologia"],
    "habilidade": {
        "nome": "Ferramenta Favorita",
        "custo": "0PE",
        "pagina": "18OP",
        "descritivo": "Um item a escolha (exceto armas) conta como -1 em categoria."
    }
}
origem17 = {
    "nome": "Executivo",
    "pericias": ["profissao","diplomacia"],
    "habilidade": {
        "nome": "Processo Otimizado",
        "custo": "2PE",
        "pagina": "18OP",
        "descritivo": "+5 em testes estendidos ou revisar documentos."
    }
}
origem16 = {
    "nome": "Experimento",
    "pericias": ["atletismo","fortitude"],
    "habilidade": {
        "nome": "Mutação",
        "custo": "0PE",
        "pagina": "9SH",
        "descritivo": "+2 resistência a dano. +2 em pericia a escolha. -1d20 em Diplomacia. "
    }
}
origem16 = {
    "nome": "Engenheiro",
    "pericias": ["profissao","tecnologia"],
    "habilidade": {
        "nome": "Ferramenta Favorita",
        "custo": "0PE",
        "pagina": "18OP",
        "descritivo": "Um item a escolha (exceto armas) conta como -1 em categoria."
    }
}



try:
    result = collection.insert_many(origem,)
    print("Documento inserido com sucesso!")
except pymongo.errors.DuplicateKeyError:
    print("Já existe uma origem com este nome.")