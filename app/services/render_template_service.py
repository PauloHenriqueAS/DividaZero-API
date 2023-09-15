import pdfkit
from template_termo_service import termo_algar
from models import Devedor, Credor, Divida
from datetime import date

def render(devedor: Devedor, credor: Credor, divida: Divida):
    termo_pre = termo_algar.format(
        credorNome = credor.nome,
        credorCNPJ = credor.cnpj,
        credorLogradouro = '',
        credorNum = 0,
        credorBairro = '',
        credoCidade = '',
        credorUF = '',
        credorCEP = '',
        devedorNome = devedor.nome,
        devedorCPF = devedor.cpf,
        devedorLogradouro = '',
        devedorNum = 0,
        devedorBairro = '',
        devedorCidade = '',
        devedorUF = '',
        devedorCEP = '',
        dividaValor = divida.montante_atrasado,
        dividaExt = '',
        dividaDoc = divida.num_contrato,
        parcelas = '',
        termoData = date.now()
    )
    pdfkit.from_string(termo_pre,output_path=f'Termo_{devedor.nome}.pdf')
