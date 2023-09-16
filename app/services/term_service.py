
"""
app/services/term_service.py

This module contains term-methods.
"""

from app.models import User
from app.repositorys.term_repository import term_repository
from app.repositorys.lender_repository import lender_repository
from app.repositorys.debt_repository import debt_repository
from app.repositorys.debtor_repository import debtor_repository
from app.repositorys.address_repository import address_repository
from app.models import Credor, Devedor, Divida, Endereco, TermoDivida, Parcela, Parcelamento
from datetime import date

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
    def get_term_by_id(self):
        """
        Get data term by id
        """
        return term_repository.get_term_by_id()

    def post_term(self, termo:TermoDivida, parcelas:[Parcelamento]):
        """
        Insert new data term
        """
        divida = debt_repository.get_debt_by_id(termo.id_divida)
        devedor = lender_repository.get_lerder_by_id(divida.id_devedor)
        credor = debtor_repository.get_debtor_by_id(divida.id_credor)
        end_cred = address_repository.get_address_by_id(credor.id_endereco)
        end_dev = address_repository.get_address_by_id(devedor.id_endereco)
        
        data = data.today()
        
        for parcela in parcelas:
            for i in range(parcela.qtd):
                parcelaDb = Parcela(valor_parcela=parcela.valor,
                                    data_vencimento = adicionar_meses(data,i+1),
                                    parcela_paga=False)

        render(devedor,credor, divida, end_dev, end_cred,termo)


        # TODO: assinatura

        return term_repository.post_term(termo)

    def update_term(self):
        """
        Update term data
        """
        return term_repository.update_term()

term_service = TermService()
