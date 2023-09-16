
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

class TermService:
    """
    Term Service
    """
    def get_term_by_id(self):
        """
        Get data term by id
        """
        return term_repository.get_term_by_id()

    def post_term(self, termo:TermoDivida, parcelas:Parcelamento):
        """
        Insert new data term
        """
        divida = debt_repository.get_debt_by_id(termo.id_divida)
        devedor = lender_repository.get_lerder_by_id(divida.id_devedor)
        credor = debtor_repository.get_debtor_by_id(divida.id_credor)
        end_cred = address_repository.get_address_by_id(credor.id_endereco)
        end_dev = address_repository.get_address_by_id(devedor.id_endereco)

        render(devedor,credor, divida, end_dev, end_cred,termo)

        # TODO: assinatura

        return term_repository.post_term(termo)

    def update_term(self):
        """
        Update term data
        """
        return term_repository.update_term()

term_service = TermService()
