# -*- coding: utf-8 -*-
"""
>>> pl = PDFLoader("historico/Pedidos Atacadão 10 Junho 2015.pdf", "", "temp/pdf_pickle.pkl")
>>> m = Miner(pl.pdf)
>>> pedido0 = m.mine(0)
>>> r = ClientesLoader("../filiais.xls", 0, "temp/filiais_pickle.pkl")
>>> r.update_pedidos([pedido0])
>>> xlsx = "temp/vendas_" + datetime.now().strftime("%d.%m.%y_%H:%M") + ".xlsx"
>>> w = XlsxWriter([pedido0], xlsx)
>>> w.create_worksheet()
>>> os.remove("temp/pdf_pickle.pkl")
"""

if __name__ == "__main__":
    import os
    import doctest
    from datetime import datetime
    from loader import PDFLoader, ClientesLoader
    from miner import Miner
    from writer import XlsxWriter
    doctest.testmod()
