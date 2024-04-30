from collections import defaultdict
from collections import Counter

texto1 = """
    Thanksgiving Day is one of the favorite holidays in the USA and Canada.
    This is a day for the family to gather.
    Grandparents come for a visit.
    Or grownup children visit their parents.
    Kids at school usually have a play dedicated to this day.
    Thanksgiving is celebrated on the fourth Thursday of November in the US.
    And on the second Monday of October in Canada.
    This day starts a holiday season finishing with Christmas and New Year.
    Originally this holiday was a day to thank God.
    People celebrated it at the end of fall after gathering in the harvest.
"""

texto2 = """
    Learning a foreign language is a challenge.
    You have to know what your final aim is.
    Whether you want to get basic vocabulary to explain at the reception that the air-conditioner in your room is broken.
    Or you'd like to be fluent and read Shakespeare or Dumas in the original.
    Also you need to get motivated. You must concentrate and learn something new every day.
    No matter what methods you use - the thing is you should do it non-stop.
    There are a lot of necessary principles of learning: reading, writing, listening, speaking.
    You might get really good at it but never forget about practicing.
    You can't be good enough without using your skills in real life, make it your daily routine.
    There's no limit to perfection. But practice makes you a bit perfect every single day.
"""

print(texto1)
print('------------------------------------------------------------------------------------------------------------')
print(texto2)

def analisa_letras_de_um_texto(texto):
    aparicoes_de_palavras = Counter(texto.lower())
    total_de_caracteres_do_texto = sum(aparicoes_de_palavras.values())
    proporcao = [(letra, frequencia / total_de_caracteres_do_texto) for letra, frequencia in aparicoes_de_palavras.items()]
    proporcao = Counter(dict(proporcao))
    mais_comuns = proporcao.most_common(10)
    for caractere, proporcoes in mais_comuns:
        print(f"{caractere}  ==>>  {proporcoes * 100:.1f}%")


analisa_letras_de_um_texto(texto1)
analisa_letras_de_um_texto(texto2)
