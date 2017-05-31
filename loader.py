# -*- coding: utf-8 -*-
import os
import utils
from miner import Cliente
from xlrd import open_workbook


class ClientesLoader:
    def __init__(self, xlsx_file, filiais_sheet_index, pkl_file):
        self._xlsx_file = xlsx_file
        self._pkl_file = pkl_file
        if os.path.exists(pkl_file):
            self._clientes = utils.get_pickle(pkl_file)
        else:
            self._clientes = self._read_filiais(filiais_sheet_index)

    def _read_filiais(self, filiais_sheet_index):

        book = open_workbook(self._xlsx_file)
        filiais_sheet = book.sheet_by_index(filiais_sheet_index)

        headers = [h.value.upper().encode('utf-8') for h in filiais_sheet.row(0)]
        lines_list = [[cell.value for cell in filiais_sheet.row(i)] for i in range(1, filiais_sheet.nrows)]
        wanted_list = ["CNPJ", "LOJAS", "ESTADO", "MUNICÍPIO", "BAIRRO", "END", "CEP"]
        replacement = ''
        clientes = utils.process_tabular_data(headers, lines_list, wanted_list, replacement, Cliente)

        utils.save_pickle(clientes, self._pkl_file)
        return clientes

    def update_pedidos(self, pedidos):
        for pedido in pedidos:
            for cliente in self._clientes:
                a, b = pedido.cliente.cnpj, cliente.cnpj.encode('utf-8')
                if a == b:
                    pedido.cliente = cliente
                    break

PLANILHA = './controle.xlsx'

class Loader:
    def __init__(self, xlsx_file, sheet_index=0):
        self._xlsx_file = xlsx_file
        self._clientes = self._read(sheet_index)

    def _read(self, sheet_index):

        book = open_workbook(self._xlsx_file)
        sheet = book.sheet_by_index(sheet_index)

        print(sheet.row(0))
        print(sheet.row(1))
        print(sheet.row(2))

    #     headers = [h.value.upper().encode('utf-8') for h in filiais_sheet.row(0)]
    #     lines_list = [[cell.value for cell in filiais_sheet.row(i)] for i in range(1, filiais_sheet.nrows)]
    #     wanted_list = ["CNPJ", "LOJAS", "ESTADO", "MUNICÍPIO", "BAIRRO", "END", "CEP"]
    #     replacement = ''
    #     clientes = utils.process_tabular_data(headers, lines_list, wanted_list, replacement, Cliente)
    #
    #     utils.save_pickle(clientes, self._pkl_file)
    #     return clientes
    #
    # def update_pedidos(self, pedidos):
    #     for pedido in pedidos:
    #         for cliente in self._clientes:
    #             a, b = pedido.cliente.cnpj, cliente.cnpj.encode('utf-8')
    #             if a == b:
    #                 pedido.cliente = cliente
    #                 break