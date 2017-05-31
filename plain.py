class PDF:
    def __init__(self, header, table_columns, table_items, table_items_numbers, totals):
        self.header = header
        self.table_columns = table_columns
        self.table_items = table_items
        self.table_items_numbers = table_items_numbers
        self.totals = totals


class Cliente():
    def __init__(self, cnpj, loja, estado, municipio, bairro, endereco, cep):
        self.loja = loja
        self.endereco = endereco
        self.bairro = bairro
        self.municipio = municipio
        self.estado = estado
        self.cep = cep
        self.cnpj = cnpj

    def __eq__(self, other):
        return self.cnpj == other.cnpj


class Pedido():
    def __init__(self, cliente, dt_emissao, dt_faturamento, total_produtos, total_pedido, total_verba, total_peso,
                 itens, estacao_do_ano):
        self.dt_emissao = dt_emissao
        self.cliente = cliente
        self.dt_faturamento = dt_faturamento
        self.total_produtos = total_produtos
        self.total_pedido = total_pedido
        self.total_verba = total_verba
        self.total_peso = total_peso
        self.itens = itens
        self.estacao_do_ano = estacao_do_ano


class ItemPedido():
    def __init__(self, sequencia, codigo, descricao, embalagem, prf, dt_entrega, quantidade, valor, ipi, icmsubs,
                 bcsubs, descom, desadi, valor_verba, inc, outros, peso, pit):
        self.sequencia = sequencia
        self.codigo = codigo
        self.descricao = descricao
        self.embalagem = embalagem
        self.prf = prf
        self.dt_entrada = dt_entrega
        self.quantidade = quantidade
        self.valor = valor
        self.ipi = ipi
        self.icmsubs = icmsubs
        self.bcsubs = bcsubs
        self.descom = descom
        self.desadi = desadi
        self.valor_verba = valor_verba
        self.inc = inc
        self.outros = outros
        self.peso = peso
        self.pit = pit