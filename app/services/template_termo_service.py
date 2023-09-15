from models import Devedor, Credor, Divida, TermoDivida


termo1 = '''
<!DOCTYPE html>
<html>
    <head>
        <meta charset='UTF-8'>
        <title>Termo de renegociação e confissão de Dívidas</title>
    </head>
    <body>
        <h1>TERMO DE RENEGOCIAÇÃO CONTRATUAL E CONFISSÃO DE DÍVIDAS</h1>
        <strong>Cliente: {clienteNome}</strong><br>
        <strong>Produto: {produto}</strong><br>
        <p>{clienteNome},{clienteNacionalidade}, inscrito(a) no CPF sob nº {devedorCPF}, {devedorEstadoCivil},residente à {devedor.endereco.logradouro},{devedor.endereco.numero}, Bairro {devedor.endereco.bairro}, {devedor.endereco.cidade} - {devedor.endereco.estado}, doravante denominado CONFIDENTE DEVEDOR, e</p>
        <p>{credorNome} - CNPJ: {credorCNPJ}, localizada na {credorEndereco}, {credorEnderecoNmr}, bairro {credorBairro}, na cidade {credorCidade} - {credorEstado}, doravante denominada CREDORA</p>
        <p>E todos, em conjunto, denomindos PARTES, têm justo e acordado o presente "Termo de Renegociação Contratual e Confissão de Dívida", que se regerá pelos termos, clausulas e condições abaixo:</p>
        <p>Considerando que:</p>
        <p>{dividaTermo}</p>
        <h2>CLÁUSULA PRIMEIRA</h2>
        <p>Pelo presente, o CONFIDENTE DEVEDOR, reconhece perante a CREDORA a dívida originária do restante do saldo devedor referente ao produto e demais adicionais, se houver, conforme objeto e valor(es) abaixo especificados:</p>
        <ol>
            <li><p>A importancia de R$ {dividaAtraso} ({dividaAtraso}), referente ao restante do saldo devedor correspondente ao produto descrito no considerando, acima, a ser paga na seguionte forma de financiamento</p></li>
            {dividaParcelas}
        </ol>

        <h2>CLÁUSULA TERCEIRA</h2>
        <p>Caso verificado o inadimplento do CONFIDENTE DEVEDOR, o presente "Termo de Renegociação Contratual e Confissão de Dívida", em conformidade com o que dispõem os artigos 566, inciso I e 585, inciso II, ambos do Código de Processo Civil Brasileiro, será, nos termos da legislação competente, considerado titulo executivo extrajudicial.</p>

        <h2>CLÁUSULA QUARTA</h2>
        
        <h2>CLÁUSULA QUINTA</h2>
        <p>As PARTES elegem o foro da comarca a masma da cidade {credor.endereco.cidade}, para diminuir quaisquer controvérsias oriunds de sua interpretação, bom como de seus respectivos aditamentos e/ou de quaisquer outros instrumentos porventura já firmados entre as PARTES, em prejuizo de qualquer outro foro, por mais privilegiado que possa ser, raificado ou retificado, nesta oportunidade, a opção ajustada no "Contrato particular de Promessa de Compra e Venda".</p>
        <p>E por estarem justas e acertadas, assinam as PARTES o presente instumento.</p>
        <p>{credor.endereco.cidade}, {termo.data}</p>

        <strong>CONFIDENTE DEVEDOR:</strong>
        <strong>CREDOR:</strong>

    </body>
</html>
'''

termo_algar = '''
<html>
    <head>
        <meta charset='UTF8'>
        <title>INSTRUMENTO PARTICULAR DE ACORDO E CONFISSÃO DE DÍVIDA</title>
    </head>
    <body>
        <h1>INSTRUMENTO PARTICULAR DE ACORDO E CONFISSÃO DE DÍVIDA</h1>
        <p>Pelo presente Contrato, de um lado <strong>{credorNome}</strong> prestadora de serviços, inscrita no CNPJ n.º <strong>{credorCNPJ}</strong>, com sede na {credorLogradouro}, n.º {credorNum}, Bairro {credorBairro}, na cidade de {credorCidade} - {credorUF}, CEP {credorCEP}, doravante deominado <strong>CREDOR</strong>, neste ato por seus representantes legais, e de outro lado, {devedorNome} - CPF n.º {devedorCPF}, residente na {devedorLogradouro}, Nº {devedorNum} – B. {devedorBairro} - Cidade: {devedorCidade} – {devedorUF} , CEP {devedorCEP}, doravante denominado <strong>DEVEDOR</strong>.</p>

        <p><strong>CONSIDERANDO</strong> que o <strong>DEVEDOR</strong> deve ao <strong>CREDOR</strong> a importância de descrita na Cláusula Terceira deste instrumento, doravante denominada simplesmente “Dívida”;
        <strong>CONSIDERANDO</strong> que o <strong>DEVEDOR</strong>, por livre iniciativa, solicitou ao <strong>CREDOR</strong> a repactuação das condições de pagamento da Dívida;
        <strong>CONSIDERANDO</strong> que é do interesse das partes contratantes o acerto de novas condições para a quitação da Dívida;
        <strong>RESOLVEM</strong> as partes celebrar o presente contrato, de comum acordo, segundo as cláusulas e condições: </p>

        <h2>CLÁUSULA PRIMAEIA - OBJETO</h2>
        <ol>
            <li><p>Constitui objeto do presente contrato a confissão e o reconhecimento, pelo <strong>DEVEDOR</strong>, de sua dívida para com o <strong>CREDOR</strong>.</p></li>
        </ol>

        <h2>CLÁUSULA SEGUNDA - CONFISSÃO E RECONHECIMENTO DE DÍVIDA</h2>
        <ol>
            <li><p>Pelo presente instrumento o <strong>DEVEDOR</strong> confessa ser devedor do <strong>CREDOR</strong> da quantia de importância <strong>R$ {dividaValor} ({dividaExt})</strong>. Incluso nessa negociação a fatura: {dividaDoc}.</p></li>
        </ol>

        <h2>CLÁUSULA TERCEIRO - PAGAMENTO</h2>
        <ol>
            <li><p>Em decorrência do reconhecimento e confissão da dívida mencionada na Cláusula Segunda, o <strong>DEVEDOR</strong> pagará ao <strong>CREDOR</strong> a importância <strong>R$ {dividaValor} ({dividas})</strong> da seguinte forma: </p>
            <ol>
                {parcelas}
            </ol></li>
            <li>Todos os pagamentos a serem efetuados pelo <strong>DEVEDOR</strong> ao <strong>CREDOR</strong>, conforme o item anterior, serão feitos em moeda nacional.</li>
        </ol>

        <h2>CLÁUSULA QUARTA – INADIMPLEMENTO</h2>
        <ol>
            <li>No caso de não pagamento da dívida, no tempo e modo estabelecidos na Cláusula Terceira, incorrerá o DEVEDOR, independentemente de qualquer interpelação ou notificação judicial ou extrajudicial:
            <ol>
                <li>Vencimento antecipado das demais prestações descritas na Cláusula Terceira;</li>
                <li>Multa de 2% (dois por cento) sobre o valor devido;</li>
                <li>Juros de 1% (um por cento), calculados pro rata die; </li>
                <li>Correção do débito pelo IGP-M calculado pela Fundação Getúlio Vargas;</li>
                <li>Bloqueio e/ou cancelamento imediato, sem prévio comunicado e/ou notificação, de todos os serviços prestados pelo CREDOR</li>
            </ol>
            </li>
            <li>A manutenção do acordo fica condicionada ao pagamento em dia das parcelas e das faturas dos meses correntes, sendo que atrasos ocasionarão o bloqueio imediato de todos os serviços relacionados neste termo, sem prévia notificação;</li>
        <ol>

        <h2>CLÁUSULA QUINTA - LIQUIDEZ E CERTEZA DA DÍVIDA</h2>
        <ol>
            <li>As importâncias devidas pelo DEVEDOR à ALGAR TELECOM S/A, nos termos deste instrumento, constituem dívidas líquidas, certas e exigíveis, consubstanciando o presente contrato título executivo extrajudicial na forma do art. 585, II, do Código de Processo Civil Brasileiro. As partes acordam e reconhecem que não descaracterizará a liquidez e a certeza do título o simples fato de a determinação dos valores importar prévio cálculo aritmético.</li>
        </ol>

        <h2>CLÁUSULA SEXTA – FORO</h2>
        <ol>
            <li> As partes elegem o foro da comarca de Uberlândia, Estado de Minas Gerais, para dirimir quaisquer dúvidas oriundas deste instrumento, com renúncia expressa a qualquer outro, por mais privilegiado que seja.</li>
        </ol>

        <p>E, por estarem assim justas e contratadas, firmam as partes o presente instrumento em duas vias de igual teor e forma, na presença das testemunhas abaixo assinadas.</p>
        <p>{credoCidade} - {credorUF}, {termoData}</p>

        <strong>CONFIDENTE DEVEDOR:</strong><br>
        <strong>CREDOR:</strong>

    </body>
</html>
'''