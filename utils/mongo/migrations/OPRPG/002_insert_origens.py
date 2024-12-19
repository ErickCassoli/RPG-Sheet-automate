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
        "pagina": "16",
        "descritivo": "Recebe +5 em testes de Intelecto."
    }
}
origem2 = {
    "nome": "Academico",
    "pericias": ["ciencias","investigacao"],
    "habilidade": {
        "nome": "Saber é Poder",
        "custo": "2PE",
        "pagina": "16",
        "descritivo": "Recebe +5 em testes de Intelecto."
    }
}
origem3 = {
    "nome": "Academico",
    "pericias": ["ciencias","investigacao"],
    "habilidade": {
        "nome": "Saber é Poder",
        "custo": "2PE",
        "pagina": "16",
        "descritivo": "Recebe +5 em testes de Intelecto."
    }
}



try:
    result = collection.insert_many(origem,)
    print("Documento inserido com sucesso!")
except pymongo.errors.DuplicateKeyError:
    print("Já existe uma origem com este nome.")