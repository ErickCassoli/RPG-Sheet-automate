import uuid
from pymongo import MongoClient

client = MongoClient("mongodb://root:example@mongodb_container:27017/")
db = client["ORDEM_PARANORMAL_RPG"]
collection = db["classes"]
collection.create_index("nome", unique=True)

classe1 = {
    "nome": "Combatente",
    "pv": 20,
    "pe": 2,
    "san": 12,
    "pd": 6,
    "proeficiencias": "Armas simples, armas táticas e proteções leves.",
    "habilidades": {
        "nome": "Ataque Especial",
        "custo": "2PE",
        "pagina": "24OP",
        "descritivo": "+5 no teste de ataque ou dano."
    }
}
classe2 = {
    "nome": "Especialista",
    "pv": 16,
    "pe": 3,
    "san": 16,
    "pd": 8,
    "proeficiencias": "Armas simples e proteções leves.",
    "habilidades": [
        {
        "nome": "Eclético",
        "custo": "2PE",
        "pagina": "28OP",
        "descritivo": "Recebe Treinado na perícia do teste."
        },
        {
        "nome": "Perito",
        "custo": "2PE",
        "pagina": "28OP",
        "descritivo": "+1d6 no resultado do teste das perícias definidas. +"
        }
    ]

}
classe3 = {
    "nome": "Ocultista",
    "pv": 12,
    "pe": 4,
    "san": 20,
    "pd": 10,
    "proeficiencias": "Armas simples.",
    "habilidades": [{
        "nome": "Escolhido Pelo Outro Lado",
        "custo": "0PE",
        "pagina": "32OP",
        "descritivo": "3 rituais de 1º circulo. +"
    }]
}
classe4 = {
    "nome": "Sobrevivente",
    "pv": 8,
    "pe": 2,
    "san": 8,
    "pd": 4,
    "proeficiencias": "Armas simples.",
    "habilidades": [{
        "nome": "Empenho",
        "custo": "1PE",
        "pagina": "31SH",
        "descritivo": "+2 no teste de perícia."
    }]
}

classes = [classe1, classe2, classe3, classe4]

def gerar_id():
    # Opção 1: Utilizando UUIDs
    return str(uuid.uuid4())
    # Opção 2: Gerando IDs sequenciais (menos recomendado para ambientes distribuídos)
    # return next(id_generator)  # Assumindo que id_generator é um gerador de IDs sequenciais

# Atribuindo IDs e inserindo na coleção
for classe in classes:
    classe["_id"] = gerar_id()
    try:
        result = collection.insert_one(classe)
        print(f"Documento {classe['nome']} inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir documento: {e}")

