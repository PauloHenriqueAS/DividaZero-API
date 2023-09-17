
"""
app/services/term_service.py

This module contains term-methods.
"""

from app.repositorys.term_repository import term_repository
from app.repositorys.lender_repository import lender_repository
from app.repositorys.debt_repository import debt_repository
from app.repositorys.debtor_repository import debtor_repository
from app.repositorys.address_repository import address_repository
from app.repositorys.parcels_repository import parcels_repository
from app.services.render_template_service import render
from app.models import Credor, Devedor, Divida, Endereco, TermoDivida, Parcela, Parcelamento
from datetime import date, timedelta

def adicionar_meses(data, n):
    # Adicionar n meses à data fornecida
    novo_ano = data.year + (data.month + n - 1) // 12
    novo_mes = (data.month + n - 1) % 12 + 1

    # Garantir que o dia não ultrapasse o último dia do novo mês
    ultimo_dia_do_mes = (data.replace(year=novo_ano, month=novo_mes, day=1) + timedelta(days=31)).replace(day=1) - timedelta(days=1)
    novo_dia = min(data.day, ultimo_dia_do_mes.day)

    nova_data = data.replace(year=novo_ano, month=novo_mes, day=novo_dia)
    return nova_data

class TermService:
    """
    Term Service
    """
    def get_term_by_id(self, id_termo:int):
        """
        Get data term by id
        """
        return term_repository.get_term_by_id(id_termo)
    
    def get_dados(self):
        """
        Get data term by id
        """
        return {'nome':'John Doe', 'cpf':'225.815.220-89', 'nacionalidade': 'Brasileira', 'estado_civil':'Solteiro', 'endereco': 'Avenida João Naves de Ávila, 2121, Santa Mônica, Uberlândia', 'num_contrato':'3127313921', 
                'data_divida': '2023-09-16', 'data_renegociacao':'2023-09-17', 'produto':'Internet 5G', 'montante_valor':'500.00', 'montante_atrasado': '500.00'}
    

    def get_all_term_by_id(self, id_user: str):
        """
        Get data term by id
        """
        return term_repository.get_all_term_by_id(id_user)

    def post_term(self, termo:TermoDivida, parcela:Parcelamento):
        """
        Insert new data term
        """
        divida = debt_repository.get_debt_by_id(termo.id_divida)
        devedor = lender_repository.get_lerder_by_id(divida.id_devedor)
        credor = debtor_repository.get_debtor_by_id(divida.id_credor)
        end_cred = address_repository.get_address_by_id(credor.id_endereco)
        end_dev = address_repository.get_address_by_id(devedor.id_endereco)
        
        data = date(date.today().year,date.today().month,10)
        
        parcelasDb = []
    
        for i in range(parcela.qtd):
            parcelasDb.append(Parcela(id_parcela = parcels_repository.generate_id_parcela()+i,
                                id_termo = termo.id_termo,
                                valor_parcela = parcela.valor,
                                data_vencimento = adicionar_meses(data,i+1),
                                parcela_paga=False))

        render(devedor,credor, divida, end_dev, end_cred,termo)


        ret = term_repository.post_term(termo)

        for i in parcelasDb:
            parcels_repository.post_parcels(i)            

        return ret

    def update_term(self):
        """
        Update term data
        """
        return term_repository.update_term()

term_service = TermService()
