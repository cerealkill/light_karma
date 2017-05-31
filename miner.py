# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

from plain import PDF, Cliente, Pedido, ItemPedido

import utils


class Miner:

    def __init__(self, pdf):
        assert isinstance(pdf, PDF)
        self._pdf = pdf

    def mine_all(self):
        """
        Minera todos os pedidos
        :return: Pedido
        :rtype:[Pedido]
        """
        return [self.mine(i) for i in range(len(self._pdf.header))]

    def mine(self, page_index):
        """
        Minera pedido de uma pagina
        :param page_index: Indice da Pagina
        :return: Pedido
        :rtype: karma.plain.Pedido
        """
        faturamento_re = '([0-9]{2}[\/][0-9]{2}[\/][0-9]{4})'
        cliente_re = '([0-9]{2}[\.][0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})'

        # Processando data emissão e faturamento
        emissao = utils.find_text(self._pdf.header[page_index], faturamento_re)
        dt_emissao = datetime.strptime(emissao, "%d/%m/%Y")
        estacao_do_ano = utils.season_in_BR(dt_emissao)
        faturamento = dt_emissao + timedelta(days=45)
        emissao = str(emissao)
        faturamento = faturamento.strftime("%d/%m/%Y")
        # Processando cliente
        cnpj_cliente = str(utils.find_text(self._pdf.header[page_index], cliente_re))
        cliente = Cliente(cnpj_cliente, '', '', '', '', '', '')
        # Processando Colunas da Tabela
        headers_text = [w for w in self._pdf.table_columns[page_index] if not (w == "" or w == "\f")]
        columns = ["Seq", "Código", "Descrição", "Embalagem", "Pr. F", "Dt Entr", "Qtde", "Vlr.", "I.P.I.", "IcmSubs",
                   "B.C. Subs", "Des.Com", "Des.Adi", "Vlr.Verba", "Inc", "Outros", "Peso Kg", "Plt"]
        # Pocessando Itens da Tabela
        table_itens_page = [w for w in self._pdf.table_items[page_index] if not (w == "" or w == "\f")]
        size = len(self._pdf.table_items_numbers[page_index])
        lines_list = map(list, map(None, *list(utils.chunks(table_itens_page, size))))
        itens = utils.process_tabular_data(headers_text, lines_list, columns, "", ItemPedido)
        # Processando totais
        columns = ["Produto:", "Pedido:", "Verba:", "Peso:"]
        totals = [w for w in self._pdf.totals[page_index] if not (w == "" or w == "\f")]
        w_dict = utils.process_columns(totals, columns)
        t_produtos, t_pedido, t_verba, t_peso = (totals[w_dict[k]+1] if k in w_dict.keys() else "" for k in columns)

        return Pedido(cliente, emissao, faturamento, t_produtos, t_pedido, t_verba, t_peso, itens, estacao_do_ano)
