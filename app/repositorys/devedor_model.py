from sqlalchemy import Column, Integer, String, Text, Enum
from app.repositorys.configDb import Base
from app.repositorys.model import UserDb

class devedorDB(UserDb):
    cpf = Column(String,index=True,nullable=False)
    nome = Column(String,index=True)
    endereco = Column(Integer,ForeignKey('endereco.id_endereco'))
    estado_civil = Column(Enum('solteiro','casado','separado','divorciado','viúvo'))
    nacionalidade = Column(Enum(' Argentino', 'Afegão', 'Alemã', 'Americano', 'Angolano', 'Antiguano', 'Argélia', 'Armeno', 'Australiano', 'Austríac', 'Bahamense', 'Bangladesh', 'Bechuano', 'Belga', 'Belizenho', 'Boliviano', 'Brasileiro', 'Camaronense', 'Canadense', 'Chileno', 'Chinês', 'Cingalês', 'Colombiano', 'Comorense', 'Costarriquenho', 'Croata', 'Cubano', 'Dinamarquês', 'Dominicana', 'Dominicano', 'Egípcio', 'Equatoriano', 'Escocês', 'Eslovaco', 'Esloveno', 'Espanhol', 'Filipina', 'Francês', 'Galês', 'Ganés', 'Granadino', 'Grego', 'Guatemalteco', 'Guianense', 'Guianês', 'Haitiano', 'Holandês', 'Hondurenho', 'Húngaro', 'Iemenita', 'Indiano', 'Indonésio', 'Inglês', 'Iraniano', 'Iraquiano', 'Irlandês', 'Israelita', 'Italiano', 'Jamaicano', 'Japonês', 'Líbio', 'Malaio', 'Marfinense', 'Marroquino', 'Mexicano', 'Moçambicano', 'Namibiana', 'Neozelandês', 'Nepalês', 'Nicaraguense', 'Nigeriano', 'Norte-coreano', 'Noruego', 'Omanense', 'Palestino', 'Panamenho', 'Paquistanês', 'Paraguaio', 'Peruano', 'Polonês', 'Portorriquenho', 'Portuguesa', 'Qatarense', 'Queniano', 'Romeno', 'Ruandês', 'Russo', 'Salvadorenho', 'Santa-lucense', 'Saudita', 'Somali', 'Sueco', 'Sul-Africano', 'Sul-africano', 'Sul-coreano', 'Surinamês', 'Suíço', 'São-cristovense', 'São-vicentino', 'Sérvio', 'Sírio', 'Tailandês', 'Timorense', 'Trindadense', 'Turco', 'Ucraniano', 'Ugandense', 'Uruguaio', 'Venezuelano', 'Vietnamita', 'Zimbabuense', 'Zimbabweano', 'barbadense', 'Árabe'))
