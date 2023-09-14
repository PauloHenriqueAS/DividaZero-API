from models import Devedor, Credor, Divida, TermoDivida


termo_de_confissao = '''
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

# Segue abaixo uma pessima pratica
# TODO: Corrigir

def render(devedor: Devedor, credor: Credor, divida: Divida, termo: TermoDivida):
    termo_preenchido = termo_de_confissao.format(
        ClieteNome = devedor.nome,
        produto = divida.produto,
        clienteNacionalidade = '',
        devedorCPF = devedor.cpf,
        credorNome = credor.nome,
        credorCNPJ = credor.cnpj,
        credorEndereco = '',
        
    )
