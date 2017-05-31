import xlsxwriter

UNDESIRED = ['sequencia', 'itens', 'cliente']

class XlsxWriter:
    def __init__(self, pedidos, xlsx_file, undesired = UNDESIRED):
        self._pedidos = pedidos
        self._xlsx_file = xlsx_file
        self._undesired = undesired

    def create_worksheet(self):
        workbook = xlsxwriter.Workbook(self._xlsx_file)
        worksheet = workbook.add_worksheet()

        bold = workbook.add_format({'bold': True})

        check_desired = lambda x: True if x not in self._undesired else False
        pedido_keys = filter(check_desired, [k for k in self._pedidos[0].__dict__])
        item_keys = filter(check_desired, [k for k in self._pedidos[0].itens[0].__dict__])
        cliente_keys = filter(check_desired, [k for k in self._pedidos[0].cliente.__dict__])
        headers = pedido_keys + item_keys + cliente_keys

        columns = [i for i in range(len(headers))]
        headers_dict = {}
        for c, h in zip(columns, headers):
            worksheet.write(0, c, h, bold)
            headers_dict[h] = c

        row = 1
        for pedido in self._pedidos:
            for item in pedido.itens:
                for att in item_keys:
                    worksheet.write(row, headers_dict[att], item.__dict__[att])
                for att in pedido_keys:
                    worksheet.write(row, headers_dict[att], pedido.__dict__[att])
                for att in cliente_keys:
                    worksheet.write(row, headers_dict[att], pedido.cliente.__dict__[att])
                row += 1

        workbook.close()
