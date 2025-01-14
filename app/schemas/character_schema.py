from pydantic import BaseModel, model_validator
from typing import Optional
from enum import Enum


# Enum para "origem"
class Origem(str, Enum):
    agente_saude = "Agente De Saúde"
    amigo_dos_animais = "Amigo Dos Animais"
    aminesico = "Aminésico"
    artista = "Artista"


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
    pv: int
    pe: Optional[int] = None
    pd: Optional[int] = None
    san: Optional[int] = None
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
