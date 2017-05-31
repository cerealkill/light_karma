# -*- coding: utf-8 -*-
import os
from glob import glob
from datetime import datetime
from loader import ClientesLoader
from miner import Miner
from writer import XlsxWriter

import utils


KARMA = "livro_sagrado/karma_pickle.pkl"
PEDIDOS = "livro_sagrado/pedidos_pickle.pkl"
PDFS = "livro_sagrado/pdf_pickle.pkl"
CLIENTES = "livro_sagrado/filiais_pickle.pkl"
SENHA_PDF_PEDIDOS = ""
LOCAL_PDFS_PEDIDOS = "historico/*.pdf"
PLANILHA_EXCEL_PEDIDOS = "temp/vendas_" + datetime.now().strftime("%d.%m.%y_%H:%M") + ".xlsx"
PLANILHA_FILIAIS = "filiais.xlsx"
PLANILHA_FILIAIS_ABA_CLIENTES = 0


def main():
    karma, karma_a_pagar = avalia_karma()
    lista_impuros = []
    # Passa pelo crivo da alma
    dicionario_almas = avalia_almas(karma_a_pagar, lista_impuros)
    # Passa pelo crivo do ego
    entoa_mantra(dicionario_almas, karma, karma_a_pagar, lista_impuros)

    if len(lista_impuros) > 0:
        print("\n\nKarma impossível de limpar nessa vida:")
        print(lista_impuros)

    print("\nNamasté")


def avalia_karma():
    """
    Descobre quantos arquivos serão enviados para planilha excel
    """
    if os.path.exists(KARMA):
        karma = utils.get_pickle(KARMA)
    else:
        karma = {}
    this_life = {}
    for file_name in glob(LOCAL_PDFS_PEDIDOS):
        this_life[hash(file_name)] = file_name
    actions = set(this_life.keys()) - set(karma.keys())
    karma_a_pagar = {action: this_life[action] for action in actions}
    if len(karma_a_pagar) < 1:
        print("Busque o Nirvana. Namasté")
        exit()
    print("Muito karma dessas almas:")
    for k in karma_a_pagar.values():
        print(k)
    return karma, karma_a_pagar


def avalia_almas(karma_a_pagar, lista_impuros):
    """
    Carrega texto dos PDFs na memória
    """
    if os.path.exists(PDFS):
        pdf_dict = utils.get_pickle(PDFS)
    else:
        pdf_dict = {}
    # Extrai objetos de texto dos PDFs
    novas_almas = [k for k in karma_a_pagar if k not in pdf_dict]
    for k in novas_almas:
        file_name = karma_a_pagar[k]
        try:
            # Carrega PDF de pedidos, recorta e transforma em texto
            pdf_loader = PDFLoader(file_name, SENHA_PDF_PEDIDOS)
            pdf_dict[k] = pdf_loader.pdf
            utils.save_pickle(pdf_dict, PDFS)
        except Exception as err:
            # Salva PDF na lista de rejeitados
            lista_impuros.append({file_name, err.message})
    return pdf_dict


def entoa_mantra(dicionario_almas, karma, karma_a_pagar, lista_impuros):
    """
    Minera os dados dos objetos de texto estruturado e tranforma em Pedidos
    """
    if os.path.exists(PEDIDOS):
        dicionario_pedidos = utils.get_pickle(PEDIDOS)
    else:
        dicionario_pedidos = {}
    novas_almas = [k for k in karma_a_pagar if k not in dicionario_pedidos]
    for k in novas_almas:
        file_name = karma_a_pagar[k]
        try:
            # Recebe os textos e transforma em pedidos usando magia
            miner = Miner(dicionario_almas[k])
            pedidos = miner.mine_all()
            # Limpa o karma dessa vida
            karma[hash(file_name)] = file_name
            # Salva alterações
            dicionario_pedidos[k] = pedidos
            utils.save_pickle(karma, KARMA)
            utils.save_pickle(dicionario_pedidos, PEDIDOS)
        except Exception as err:
            # Salva PDF na lista de rejeitados
            lista_impuros.append({file_name, err.message})
        finally:
            # Limpa o karma
            print(next(utils.MANTRA))
    lista_pedidos = utils.flatten(dicionario_pedidos.values())
    # Carrega o XLS de filiais, extrai os clientes e atualiza os pedidos
    clientes_loader = ClientesLoader(PLANILHA_FILIAIS, PLANILHA_FILIAIS_ABA_CLIENTES, CLIENTES)
    clientes_loader.update_pedidos(lista_pedidos)
    # Escreve os pedidos na planilha excel
    xlsx_writer = XlsxWriter(lista_pedidos, PLANILHA_EXCEL_PEDIDOS)
    xlsx_writer.create_worksheet()
    return dicionario_pedidos


if __name__ == '__main__':
        main()
