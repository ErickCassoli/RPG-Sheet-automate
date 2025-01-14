import fitz  # PyMuPDF
from pathlib import Path

# Caminhos para templates e saídas
TEMPLATES_DIR = Path(__file__).parent.parent.parent / "templates" / "OPRPG"
OUTPUT_DIR = Path(__file__).parent.parent.parent / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)  # Cria o diretório de saída, se não existir


def preencher_ficha(character_data: dict) -> str:
    template_path = TEMPLATES_DIR / "OPRPGTemplate.pdf"
    output_path = OUTPUT_DIR / f"{character_data['personagem']}_Ficha.pdf"

    # Abre o template do PDF
    doc = fitz.open(str(template_path))
    page = doc[0]  # Primeira página

    # Mapeia os campos do PDF para os dados do personagem
    campos = {
        "Personagem": character_data["personagem"],
        "Jogador": character_data["jogador"],
        "Origem": character_data["origem"],
        "Classe": character_data["classe"],
        "PV": str(character_data["pv"]),
        "PE": str(character_data["pe"]) if character_data.get("pe") else "",
        "PD": str(character_data["pd"]) if character_data.get("pd") else "",
        "SAN": str(character_data["san"]) if character_data.get("san") else "",
        "Deslocamento": str(character_data["deslocamento"]),
        "Protecao": str(character_data["protecao"]),
        "Resistencia": str(character_data["resistencia"]),
        # Preenchendo atributos individuais
        "FOR": str(character_data["forca"]),
        "AGI": str(character_data["agilidade"]),
        "PRE": str(character_data["presenca"]),
        "INT": str(character_data["inteligencia"]),
        "VIG": str(character_data["vigor"]),
    }

    # Preenche os campos no PDF
    widgets = page.widgets()
    for widget in widgets:
        if widget.field_name and widget.field_name in campos:
            try:
                widget.field_value = campos[widget.field_name]  # Preenche com o valor correto
                widget.update()  # Atualiza a aparência
                print(f"Preenchido: {widget.field_name} -> {campos[widget.field_name]}")
            except Exception as e:
                print(f"Erro ao preencher {widget.field_name}: {e}")

    # Salva o PDF preenchido
    doc.save(str(output_path))
    doc.close()
    print(f"Ficha preenchida salva em: {output_path}")

    return str(output_path)
