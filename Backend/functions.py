import networkx as nx
import matplotlib.pyplot as plt


grafo_dirigido = {
    "D1": ["EN"],
    "D2": ["P3"],
    "D3": ["P10"],
    "D4": ["P15"],
    "D5": ["P15"],
    "D6": ["P16"],
    "D7": ["P41"],
    "D8": ["P42"],
    "EN": ["P1"],
    "O": ["P12"],
    "P1": ["EP", "P2", "P10"],
    "P2": ["P3"],
    "P3": ["P4"],
    "P4": ["S1", "P5"],
    "P5": ["S2", "P6"],
    "P6": ["P7"],
    "P7": ["S3", "P8"],
    "P8": ["P9"],
    "P9": ["S4"],
    "P10": ["P11"],
    "P11": ["E1", "P12", "Z1"],
    "P12": ["P13"],
    "P13": ["P14", "P17"],
    "P14": ["P15"],
    "P15": ["P16"],
    "P16": ["S5"],
    "P17": ["P18"],
    "P18": ["S6", "P19"],
    "P19": ["Z2", "P20"],
    "Z2": ["E2"],
    "P20": ["P21", "P22"],
    "P21": ["S7"],
    "P22": ["S8", "P23"],
    "P23": ["P24", "P26"],
    "P24": ["P25"],
    "P25": ["S9", "E3"],
    "P26": ["P27"],
    "P27": ["P28", "P29"],
    "P28": ["Z3"],
    "P29": ["EC"],
    "S10": ["EC"],
    "P30": ["EC", "Z4"],
    "S11": ["P30"],
    "P31": ["P30", "P32"],
    "P32": ["Z4"],
    "S12": ["P31"],
    "S13": ["P32"],
    "P33": ["P31"],
    "P34": ["P33"],
    "Z5": ["P34"],
    "P35": ["P34"],
    "Z6": ["P35"],
    "P36": ["P29"],
    "P37": ["P36", "P38"],
    "EE": ["P38"],
    "P39": ["P28"],
    "S14": ["P39"],
    "P40": ["P39"],
    "P41": ["P40"],
    "Z8": ["P41"],
    "P42": ["P41"],
    "Z9": ["P42"],
    "P43": ["P42"],
    "P44": ["P43"],
    "P45": ["P44", "Z10"],
    "P46": ["P45"],
    "Z11": ["P46"],
    "P47": ["P46", "P"],
    "Z12": ["P47"],
    "P48": ["P47", "Z13"],
    "P49": ["P48", "Z14"],
    "P50": ["P49"],
    "Z15": ["P50"],
    "GM": ["P50"],
    "P51": ["GM"],
    "P52": ["P51"],
    "Z16": ["P52"],
    "P53": ["P52", "P38"],
    "BP": ["P53"],
    "TB": ["P52"],
    "P54": ["P51", "P55"],
    "P55": ["E4", "P56"],
    "Z17": ["P56"],
    "BS": ["P56"],
    "P56": ["P57"],
    "D9": ["P57"],
    "P57": ["P58"],
    "EA": ["P58"]
}

def dfs(grafo=grafo_dirigido, inicio="", objetivo="", visitados=None, camino=None, caminos_encontrados=None):
    if visitados is None:
        visitados = set()
    if camino is None:
        camino = []
    if caminos_encontrados is None:
        caminos_encontrados = []

    if inicio not in grafo:
        return caminos_encontrados

    camino.append(inicio)
    visitados.add(inicio)

    if inicio == objetivo:
        caminos_encontrados.append(camino.copy())
    else:
        for vecino in grafo[inicio]:
            if vecino not in visitados:
                dfs(grafo, vecino, objetivo, visitados, camino, caminos_encontrados)

    camino.pop()
    visitados.remove(inicio)

    return caminos_encontrados
