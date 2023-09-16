import pdfkit
from app.services.template_termo_service import termo_algar
from app.models import Devedor, Credor, Divida, Endereco, TermoDivida, Parcelamento
from datetime import date
from num2words import num2words
 

def render(devedor: Devedor, credor: Credor, divida: Divida, end_dev: Endereco, end_cre: Endereco, termo: TermoDivida):
    termo_pre = termo_algar.format(
        credorNome = credor.nome,
        credorCNPJ = credor.cnpj,
        credorLogradouro = end_cre.logradouro,
        credorNum = end_cre.numero,
        credorBairro = end_cre.bairro,
        credorCidade = end_cre.cidade,
        credorUF = end_cre.estado,
        credorCEP = end_cre.cep,
        devedorNome = devedor.nome,
        devedorCPF = devedor.cpf,
        devedorLogradouro = end_dev.logradouro,
        devedorNum = end_dev.numero,
        devedorBairro = end_dev.bairro,
        devedorCidade = end_dev.cidade,
        devedorUF = end_dev.estado,
        devedorCEP = end_dev.cep,
        dividaValor = divida.montante_atrasado,
        dividaExt = num2words(divida.montante_atrasado, lang='pt_Br'),
        dividaDoc = divida.num_contrato,
        parcelas = termo.num_parcela,
        termoData = date.today()
    )
    pdfkit.from_string(termo_pre,output_path=f'Termo_{devedor.nome}.pdf')
