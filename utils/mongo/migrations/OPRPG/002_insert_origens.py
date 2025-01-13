import uuid
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
origem18 = {
    "nome": "Experimento",
    "pericias": ["atletismo","fortitude"],
    "habilidade": {
        "nome": "Mutação",
        "custo": "0PE",
        "pagina": "9SH",
        "descritivo": "+2 resistência a dano. +2 em pericia a escolha. -1d20 em Diplomacia. "
    }
}
origem19 = {
    "nome": "Explorador",
    "pericias": ["fortitude","sobrevivencia"],
    "habilidade": {
        "nome": "Manual Do Sobrevivente",
        "custo": "2PE",
        "pagina": "9SH",
        "descritivo": "+5 em testes resistência contra armadilhas, clima, doenças."
    }
}
origem20 = {
    "nome": "Fanático Por Criaturas",
    "pericias": ["investigacao","ocultismo"],
    "habilidade": {
        "nome": "Conhecimento Oculto",
        "custo": "2PE",
        "pagina": "10SH",
        "descritivo": "+2 em todos os testes contra a criatura se identifica-lá."
    }
}
origem21 = {
    "nome": "Inventor Paranormal",
    "pericias": ["profissao","vontade"],
    "habilidade": {
        "nome": "Invenção Paranormal",
        "custo": "0PE",
        "pagina": "10SH",
        "descritivo": "Item com um ritual a escolha. Falhar num teste DT15 enguiça "
    }
}
origem22 = {
    "nome": "Fotógrafo",
    "pericias": ["artes","percepcao"],
    "habilidade": {
        "nome": "Manual Do Sobrevivente",
        "custo": "2PE",
        "pagina": "9SH",
        "descritivo": "+5 em testes investigação ou percepção através de camera ou foto."
    }
}
origem23 = {
    "nome": "Investigador",
    "pericias": ["investigacao","percepcao"],
    "habilidade": {
        "nome": "Faro Para Pistas",
        "custo": "1PE",
        "pagina": "19OP",
        "descritivo": "+5 em testes para procurar pistas. 1x por cena."
    }
}
origem24 = {
    "nome": "Jovem Místico",
    "pericias": ["ocultismo","religiao"],
    "habilidade": {
        "nome": "A Culpa É Das Estrelas",
        "custo": "1PE",
        "pagina": "11SH",
        "descritivo": "Role 1d6. +2 em perícias até o fim da cena se cair o número da sorte."
    }
}
origem25 = {
    "nome": "Legista Do Turno Da Noite",
    "pericias": ["ciencias","medicina"],
    "habilidade": {
        "nome": "Luto Habitual",
        "custo": "2PE",
        "pagina": "11SH",
        "descritivo": "Metade do dano mental a critério do mestre. +5 em primeiros socorros ou necropsia."
    }
}
origem26 = {
    "nome": "Lutador",
    "pericias": ["luta","reflexos"],
    "habilidade": {
        "nome": "Mão Pesada",
        "custo": "0PE",
        "pagina": "19OP",
        "descritivo": "+2 no dano corpo a corpo."
    }
}
origem27 = {
    "nome": "Magnata",
    "pericias": ["diplomacia","pilotagem"],
    "habilidade": {
        "nome": "Patrocinador Da Ordem",
        "custo": "0PE",
        "pagina": "20OP",
        "descritivo": "Seu limite de crédito é sempre um acima do atual."
    }
}
origem28 = {
    "nome": "Mateiro",
    "pericias": ["percepcao","sobrevivencia"],
    "habilidade": {
        "nome": "Mapa Celeste",
        "custo": "2PE",
        "pagina": "12SH",
        "descritivo": "Você sabe as direções cardeais vendo o céu. 2PE rola vantagem em sobrevivente."
    }
}
origem29 = {
    "nome": "Mercenário",
    "pericias": ["iniciativa","intimidacao"],
    "habilidade": {
        "nome": "Posição De Combate",
        "custo": "2PE",
        "pagina": "20OP",
        "descritivo": "Recebe ação de movimento adicional em cenas de ação."
    }
}
origem30 = {
    "nome": "Mergulhador",
    "pericias": ["atletismo","fortitude"],
    "habilidade": {
        "nome": "Fôlego de Nadador",
        "custo": "2PE",
        "pagina": "12SH",
        "descritivo": "+5 PV e pode prender a respiração por 2xVIG rodadas. Teste de natação desloca 9m."
    }
}
origem31 = {
    "nome": "Militar",
    "pericias": ["pontaria","tatica"],
    "habilidade": {
        "nome": "Para Bellum",
        "custo": "0PE",
        "pagina": "20OP",
        "descritivo": "+2 para dano em armas de fogo."
    }
}
origem32 = {
    "nome": "Motorista",
    "pericias": ["pilotagem","reflexos"],
    "habilidade": {
        "nome": "Mãos No Volante",
        "custo": "2PE",
        "pagina": "13SH",
        "descritivo": "+5 em testes de Pilotagem ou resistência enquanto pilota."
    }
}
origem33 = {
    "nome": "Nerd Entusiasta",
    "pericias": ["ciencias","tecnologia"],
    "habilidade": {
        "nome": "O Inteligentão",
        "custo": "0PE",
        "pagina": "13SH",
        "descritivo": "Ler em interlúdio aumenta +1 dado como bônus."
    }
}
origem34 = {
    "nome": "Operário",
    "pericias": ["fortitude","profissao"],
    "habilidade": {
        "nome": "Ferramenta De Trabalho",
        "custo": "0PE",
        "pagina": "20OP",
        "descritivo": "+1 em testes, dano e ameaça com uma feramenta escolhida."
    }
}
origem35 = {
    "nome": "Policial",
    "pericias": ["percepcao","pontaria"],
    "habilidade": {
        "nome": "Patrulha",
        "custo": "0PE",
        "pagina": "20OP",
        "descritivo": "Recebe +2 em Defesa"
    }
}
origem36 = {
    "nome": "Profetizado",
    "pericias": ["vontade","ocultismo"],
    "habilidade": {
        "nome": "Luta Ou Fuga",
        "custo": "0PE",
        "pagina": "13SH",
        "descritivo": "+2 em vontade com referência a sua premonição. +2PE temporários na cena."
    }
}
origem37 = {
    "nome": "Psicólogo",
    "pericias": ["intuicao","profissao"],
    "habilidade": {
        "nome": "Terapia",
        "custo": "0PE",
        "pagina": "13SH",
        "descritivo": "Usa Profissão como Diplomacia."
    }
}
origem38 = {
    "nome": "Religioso",
    "pericias": ["religiao","vontade"],
    "habilidade": {
        "nome": "Acalentar",
        "custo": "0PE",
        "pagina": "20OP",
        "descritivo": "+5 em testes de Religião para acalmar. Recupera 1d6+PRE de sanidade."
    }
}
origem39 = {
    "nome": "Reporter Investigativo",
    "pericias": ["atualidades","investigacao"],
    "habilidade": {
        "nome": "Encontrar A Verdade",
        "custo": "2PE",
        "pagina": "13SH",
        "descritivo": "Usa Investigação para persuadir. 2PE recebe +5 em Investigação."
    }
}
origem40 = {
    "nome": "Servidor Público",
    "pericias": ["intuicao","vontade"],
    "habilidade": {
        "nome": "Espírito Cívico",
        "custo": "1PE",
        "pagina": "20OP",
        "descritivo": "+2 em testes para ajudar. "
    }
}
origem41 = {
    "nome": "T.I.",
    "pericias": ["investigacao","tecnologia"],
    "habilidade": {
        "nome": "Motor De Busca",
        "custo": "2PE",
        "pagina": "21OP",
        "descritivo": "Com internet, troca teste de perícia por Tecnologia."
    }
}
origem42 = {
    "nome": "Teórico Da Conspiração",
    "pericias": ["investigacao","ocultismo"],
    "habilidade": {
        "nome": "Eu Já Sabia!",
        "custo": "0PE",
        "pagina": "21OP",
        "descritivo": "Resistência a dano mental igual ao INT."
    }
}
origem43 = {
    "nome": "Trabalhador Rural",
    "pericias": ["adestramento","sobrevivencia"],
    "habilidade": {
        "nome": "Desbravador",
        "custo": "2PE",
        "pagina": "21OP",
        "descritivo": "+5 em testes de Adestramento ou Sobrevivência. Terreno dificil não afeta."
    }
}
origem44 = {
    "nome": "Trambiqueiro",
    "pericias": ["crime","enganacao"],
    "habilidade": {
        "nome": "Impostor",
        "custo": "2PE",
        "pagina": "21OP",
        "descritivo": "1x por cena troca pericia por Enganação em testes."
    }
}
origem45 = {
    "nome": "Universitário",
    "pericias": ["atualidades","investigacao"],
    "habilidade": {
        "nome": "Dedicação",
        "custo": "0PE",
        "pagina": "21OP",
        "descritivo": "+1PE, e 1PE adicional a cada NEX ímpar. +1 limite de PE."
    }
}
origem46 = {
    "nome": "Vítima",
    "pericias": ["reflexos","vontade"],
    "habilidade": {
        "nome": "Cicatrizes Psicológicas",
        "custo": "0PE",
        "pagina": "21OP",
        "descritivo": "+1 Sanidade para cada 5% de NEX."
    }
}
origem47 = {
    "nome": "Jornalista",
    "pericias": ["atualidades","investigacao"],
    "habilidade": {
        "nome": "Fontes Confiáveis",
        "custo": "1PE",
        "pagina": "MP",
        "descritivo": "1x/sessão rola novamente um teste de pista com +5 bônus."
    }
}
origem48 = {
    "nome": "Ginasta",
    "pericias": ["acrobacia","reflexos"],
    "habilidade": {
        "nome": "Mobilidade Acrobática",
        "custo": "0PE",
        "pagina": "MP",
        "descritivo": "+2 Defesa. +3m Deslocamento."
    }
}
origem49 = {
    "nome": "Gaudério Abutre",
    "pericias": ["luta","pilotagem"],
    "habilidade": {
        "nome": "Fraternidade Gaudéria",
        "custo": "1PE",
        "pagina": "MP",
        "descritivo": "Troca de lugar para levar um ataque/efeito. +2 teste de ataque prox turno."
    }
}
origem50 = {
    "nome": "Cientista Forense",
    "pericias": ["ciencias","investigacao"],
    "habilidade": {
        "nome": "Investigação Científica",
        "custo": "0PE",
        "pagina": "MP",
        "descritivo": "1x/cena. Gasta ação livre para procurar pistas. Usa Ciências no lugar."
    }
}
origem51 = {
    "nome": "Dublê",
    "pericias": ["reflexos","pilotagem"],
    "habilidade": {
        "nome": "Destemido",
        "custo": "0PE",
        "pagina": "MP",
        "descritivo": "Falhar num teste danoso, recebe +5 no teste"
    }
}
origem52 = {
    "nome": "Blaster",
    "pericias": ["ciencias","profissao"],
    "habilidade": {
        "nome": "Explosão Solidária",
        "custo": "2PE",
        "pagina": "MP",
        "descritivo": "+2d6 dano explosivos. 2PE melhora explosivo em interlúdio. +5CD"
    }
}
origem53 = {
    "nome": "Revoltado",
    "pericias": ["furtividade","vontade"],
    "habilidade": {
        "nome": "Antes só...",
        "custo": "0PE",
        "pagina": "MP",
        "descritivo": "+1 Defesa, perícias e limite PE por turno sem aliado al. curto."
    }
}
origem54 = {
    "nome": "Personal Trainer",
    "pericias": ["atletismo","ciencias"],
    "habilidade": {
        "nome": "Todo Mundo Pagando 10",
        "custo": "2PE",
        "pagina": "MP",
        "descritivo": "+2 em testes de FOR ou AGI para aliados. Luta/pontaria não."
    }
}
origem55 = {
    "nome": "Body Builder",
    "pericias": ["atletismo","fortitude"],
    "habilidade": {
        "nome": "Saindo Da Jaula",
        "custo": "2PE",
        "pagina": "MP",
        "descritivo": "+5 em testes de FOR ou VIG. Luta não."
    }
}
origem56 = {
    "nome": "Escritor",
    "pericias": ["artes","atualidades"],
    "habilidade": {
        "nome": "Bagagem De Leitura",
        "custo": "2PE",
        "pagina": "MP",
        "descritivo": "1x/cena para treinar perícia até fim da cena."
    }
}
origem57 = {
    "nome": "Professor",
    "pericias": ["ciencias","intuicao"],
    "habilidade": {
        "nome": "Aula De Campo",
        "custo": "2PE",
        "pagina": "MP",
        "descritivo": "1x/cena +1 em atributo de outro personagem. Fim da cena."
    }
}

origens = [origem, origem2, origem3, origem4, origem5, origem6, origem7, origem8, origem9, origem9, origem10, origem11, origem12, origem13, origem14, origem15, origem16, origem17, origem18, origem19, origem20, origem21, origem22, origem23, origem24, origem25, origem26, origem27, origem28, origem29, origem30, origem31, origem32, origem33, origem34, origem35, origem36, origem37, origem38, origem39, origem40, origem41, origem42, origem43, origem44, origem45, origem46, origem47, origem48, origem49, origem50, origem51, origem52, origem53, origem54, origem55, origem56, origem57]

def gerar_id():
    # Opção 1: Utilizando UUIDs
    return str(uuid.uuid4())
    # Opção 2: Gerando IDs sequenciais (menos recomendado para ambientes distribuídos)
    # return next(id_generator)  # Assumindo que id_generator é um gerador de IDs sequenciais

# Atribuindo IDs e inserindo na coleção
for origem in origens:
    origem["_id"] = gerar_id()
    try:
        result = collection.insert_one(origem)
        print(f"Documento {origem['nome']} inserido com sucesso!")
    except Exception as e:
        print(f"Erro ao inserir documento: {e}")

for origem in origens:
    try:
        result = collection.insert_one(origem)
        print(f"Documento {origem['nome']} inserido com sucesso!")
    except client.errors.DuplicateKeyError:
        print(f"Já existe uma origem com o nome {origem['nome']}.")