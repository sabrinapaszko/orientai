def generate_recommendations(answers_text):
    # Mock simples para teste
    if "computação" in answers_text.lower():
        return ["Ciência da Computação", "Engenharia de Software"]
    elif "biologia" in answers_text.lower():
        return ["Biomedicina", "Ciências Biológicas"]
    else:
        return ["Administração", "Engenharia de Produção"]