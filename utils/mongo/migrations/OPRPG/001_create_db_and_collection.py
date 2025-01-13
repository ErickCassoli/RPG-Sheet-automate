from pymongo import MongoClient

client = MongoClient("mongodb://root:example@mongodb_container:27017/")
db = client["ORDEM_PARANORMAL_RPG"]
collection = db["origens"]
collection.create_index("nome", unique=True)

# Inserindo um documento com estrutura definida
origem = {
    "nome": ,
    "pericias": [],
    "habilidade": {
        "nome": ,
        "custo": ,
        "pagina": ,
        "descritivo":
    }
}

try:
    result = collection.insert_one(origem)
    print("Documento inserido com sucesso!")
except pymongo.errors.DuplicateKeyError:
    print("Já existe uma origem com este nome.")
