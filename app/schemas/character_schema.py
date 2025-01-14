from pydantic import BaseModel, model_validator
from typing import Optional
from enum import Enum


# Enum para "origem"
class Origem(str, Enum):
    academico = "Acadêmico"
    agente_de_saude = "Agente De Saúde"
    amnesico = "Amnésico"
    artista = "Artista"
    atleta = "Atleta"
    chef = "Chef"
    criminoso = "Criminoso"
    cultista_arrependido = "Cultista Arrependido"
    desgarrado = "Desgarrado"
    engenheiro = "Engenheiro"
    executivo = "Executivo"
    investigador = "Investigador"
    lutador = "Lutador"
    magnata = "Magnata"
    mercenario = "Mercenário"
    militar = "Militar"
    operario = "Operário"
    policial = "Policial"
    religioso = "Religioso"
    servidor_publico = "Servidor Público"
    teorico_da_conspiracao = "Teórico Da Conspiração"
    ti = "T.I."
    trabalhador_rural = "Trabalhador Rural"
    trambiqueiro = "Trambiqueiro"
    universitario = "Universitário"
    vitima = "Vítima"
    amigo_dos_animais = "Amigo dos Animais"
    astronauta = "Astronauta"
    chef_do_outro_lado = "Chef do Outro Lado"
    colegial = "Colegial"
    cosplayer = "Cosplayer"
    diplomata = "Diplomata"
    explorador = "Explorador"
    experimento = "Experimento"
    fanatico_por_criaturas = "Fanático por Criaturas"
    fotografo = "Fotógrafo"
    inventor_paranormal = "Inventor Paranormal"
    jovem_mistico = "Jovem Místico"
    legista_do_turno_da_noite = "Legista do Turno da Noite"
    mateiro = "Mateiro"
    mergulhador = "Mergulhador"
    motorista = "Motorista"
    nerd_entusiasta = "Nerd Entusiasta"
    profetizado = "Profetizado"
    psicologo = "Psicólogo"
    reporter_investigativo = "Repórter Investigativo"
    ginasta = "Ginasta"
    jornalista = "Jornalista"
    professor = "Professor"
    escritor = "Escritor"
    body_builder = "Body Builder"
    personal_trainer = "Personal Trainer"
    revoltado = "Revoltado"
    duble = "Dublê"
    gauderio_abutre = "Gaudério Abutre"
    blaster = "Blaster"
    cientista_forense = "Ciêntista Forense"

# Enum para "classe"
class Classe(str, Enum):
    combatente = "Combatente"
    especialista = "Especialista"
    ocultista = "Ocultista"
    sobrevivente = "Sobrevivente"


# Modelo principal do Personagem
class Character(BaseModel):
    personagem: str
    jogador: str
    origem: Origem
    classe: Classe
    nex: Optional[int] = None
    nivel_nex: Optional[int] = None
    patente: Optional[str] = None
    deslocamento: int
    equip: Optional[int] = None
    outros: Optional[int] = None
    protecao: int
    resistencia: int

    # Atributos individuais
    forca: int
    agilidade: int
    presenca: int
    inteligencia: int
    vigor: int

    # Validações customizadas
    @model_validator(mode='after')
    def valida_escolhas(self):
        # Validação para NEX, nível/NEX e patente
        opcoes_nex = [self.nex, self.nivel_nex, self.patente]
        if sum(1 for opcao in opcoes_nex if opcao is not None) != 1:
            raise ValueError("Escolha apenas uma opção entre NEX, nível/NEX e patente.")

        # Validação para PE e SAN ou PD
        if self.pd is not None and (self.pe is not None or self.san is not None):
            raise ValueError("Se PD for escolhido, PE e SAN não podem ser preenchidos.")
        if self.pe is not None and self.san is None:
            raise ValueError("Se PE for escolhido, SAN também deve ser informado.")
        if self.pd is None and self.pe is None and self.san is None:
            raise ValueError("Escolha entre PE e SAN ou apenas PD.")

        return self
