import os
from app.models import Credor, Devedor, Divida, Endereco, TermoDivida, Parcelamento
from app.services.render_template_service import render


def test_render():
    devedor = Devedor(nome='John Doe', cpf='123456789')
    credor = Credor(nome='Algar Telecom', cnpj='987654321')
    divida = Divida(montante_atrasado=3000, num_contrato='12345')
    termo = TermoDivida(num_parcela=3)
    parcela = Parcelamento(valor=1000,qtd=3)
    end1 = Endereco(
        logradouro="Avenida Central",
        bairro="Centro",
        numero=100,
        cep="38000-001",
        complemento="Sala 101",
        cidade="Uberlândia",
        estado="MG"
    )
    end2 = Endereco(
        logradouro="Rua Principal",
        bairro="Bairro 2",
        numero=200,
        cep="38100-002",
        cidade="Uberaba",
        estado="MG"
    )

    render(devedor,credor,divida,end2,end1,termo,parcela)
    assert os.path.exists(f'Termo_{devedor.nome}.pdf')

