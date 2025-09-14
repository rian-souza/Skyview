registro_externo = []

registro_sistemasolar = [{
    "nome": "Sol",
    "tipo": "Estrela",
    "gravidade": "274 m/s²",
    "posição orbital": "Centro do Sistema Solar",
    "temperatura": "5778 K",
    "atmosfera": "Hidrogênio e Hélio",
    "magnetosfera": "Ciclo de 11 anos",
    "rec_minerais": "Plasma rico em H e He"
}, {
    "nome": "Mercúrio",
    "tipo": "Planeta",
    "gravidade": "3.7 m/s²",
    "posição orbital": "1ª",
    "temperatura": "430 °C (dia), -180 °C (noite)",
    "atmosfera": "Exoesfera de Hélio e Oxigênio",
    "magnetosfera": "Fraca",
    "rec_minerais": "Silicatos, ferro"
}, {
    "nome": "Vênus",
    "tipo": "Planeta",
    "gravidade": "8.87 m/s²",
    "posição orbital": "2ª",
    "temperatura": "480 °C",
    "atmosfera": "Dióxido de carbono e ácido sulfúrico",
    "magnetosfera": "Ausente",
    "rec_minerais": "Basalto, silicatos"
}, {
    "nome": "Terra",
    "tipo": "Planeta",
    "gravidade": "9.8 m/s²",
    "posição orbital": "3ª",
    "temperatura": "15 °C média",
    "atmosfera": "Nitrogênio e Oxigênio",
    "magnetosfera": "Presente",
    "rec_minerais": "Ferro, Silício, Alumínio"
}, {
    "nome": "Marte",
    "tipo": "Planeta",
    "gravidade": "3.71 m/s²",
    "posição orbital": "4ª",
    "temperatura": "-60 °C média",
    "atmosfera": "Dióxido de carbono",
    "magnetosfera": "Ausente (remanescente local)",
    "rec_minerais": "Óxidos de ferro, silício"
}, {
    "nome": "Júpiter",
    "tipo": "Planeta",
    "gravidade": "24.79 m/s²",
    "posição orbital": "5ª",
    "temperatura": "-110 °C média",
    "atmosfera": "Hidrogênio e Hélio",
    "magnetosfera": "Extensa e poderosa",
    "rec_minerais": "Gases, gelo de amônia"
}, {
    "nome": "Saturno",
    "tipo": "Planeta",
    "gravidade": "10.44 m/s²",
    "posição orbital": "6ª",
    "temperatura": "-140 °C média",
    "atmosfera": "Hidrogênio e Hélio",
    "magnetosfera": "Presente",
    "rec_minerais": "Gelo, gases leves"
}, {
    "nome": "Urano",
    "tipo": "Planeta",
    "gravidade": "8.69 m/s²",
    "posição orbital": "7ª",
    "temperatura": "-195 °C média",
    "atmosfera": "Hidrogênio, Hélio e Metano",
    "magnetosfera": "Inclinação extrema",
    "rec_minerais": "Gelo de água, amônia, metano"
}, {
    "nome": "Netuno",
    "tipo": "Planeta",
    "gravidade": "11.15 m/s²",
    "posição orbital": "8ª",
    "temperatura": "-200 °C média",
    "atmosfera": "Hidrogênio, Hélio e Metano",
    "magnetosfera": "Presente",
    "rec_minerais": "Gelo, compostos voláteis"
}]

firmamento = sorted([
    "Andrômeda", "Antlia", "Apus", "Aquarius", "Aquila", "Ara", "Aries",
    "Auriga", "Boötes", "Caelum", "Camelopardalis", "Câncer", "Canes Venatici",
    "Canis Major", "Canis Minor", "Capricornus", "Carina", "Cassiopeia",
    "Centaurus", "Cepheus", "Cetus", "Chamaeleon", "Circinus", "Columba",
    "Coma Berenices", "Corona Australis", "Corona Borealis", "Corvus",
    "Crater", "Crux", "Cygnus", "Delphinus", "Dorado", "Draco", "Equuleus",
    "Eridanus", "Fornax", "Gemini", "Grus", "Hércules", "Horologium", "Hydra",
    "Hydrus", "Indus", "Lacerta", "Leo", "Leo Minor", "Lepus", "Libra",
    "Lupus", "Lynx", "Lyra", "Mensa", "Microscopium", "Monoceros", "Musca",
    "Norma", "Octans", "Ophiuchus", "Orion", "Pavo", "Pegasus", "Perseus",
    "Phoenix", "Pictor", "Pisces", "Piscis Austrinus", "Puppis", "Pyxis",
    "Reticulum", "Sagitta", "Sagittarius", "Scorpius", "Sculptor", "Scutum",
    "Serpens", "Sextans", "Taurus", "Telescopium", "Triangulum",
    "Triangulum Australe", "Tucana", "Ursa Major", "Ursa Minor", "Vela",
    "Virgo", "Volans", "Vulpecula"
])

class Constelacao:

  def __init__(self, nome, hemisferio, estrelas_principais, area, familia,
               tipo, mitologia, magnitude_limite, observavel_em, coordenadas,
               obj_celestes, historia):

    self.nome = nome
    self.hemisferio = hemisferio
    self.estrelas_principais = estrelas_principais
    self.area = area
    self.familia = familia
    self.tipo = tipo
    self.mitologia = mitologia
    self.magnitude_limite = magnitude_limite
    self.observavel_em = observavel_em
    self.coordenadas = coordenadas
    self.obj_celestes = obj_celestes
    self.historia = historia

  def __str__(self):
    return f"Constelação: {self.nome}\nHistória: {self.historia}\nHemisfério: {self.hemisferio}\nEstrelas Principais: {self.estrelas_principais}\nÁrea: {self.area}\nFamília: {self.familia}\nTipo: {self.tipo}\nMitologia: {self.mitologia}\nMagnitude Limite: {self.magnitude_limite}\nObservável em: {self.observavel_em}\nCoordenadas: {self.coordenadas}\nObjetos Celestes: {self.obj_celestes}\nHistória: {self.historia}"