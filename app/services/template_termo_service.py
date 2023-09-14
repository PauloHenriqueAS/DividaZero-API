termo_de_confissao = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset='UTF-8'>
    <title>Termo de renegociação e confissão de Dívidas</title>
</head>
<body>
    <h1>TERMO DE RENEGOCIAÇÃO CONTRATUAL E CONFISSÃO DE DÍVIDAS</h1>
    <strong>Cliente: {cliente.nome}</strong><br>
    <strong>Produto: {divida.produto}</strong><br>
    <p>{cliente.nome},{cliente.nacionalidade}, inscrito(a) no CPF sob nº {devedor.cpf}, {devedor.estado_civil},residente à {devedor.endereco.logradouro},{devedor.endereco.numero}, Bairro {devedor.endereco.bairro}, {devedor.endereco.cidade} - {devedor.endereco.uf}, doravante denominado CONFIDENTE DEVEDOR, e</p>
    <p>{credor.nome} - CNPJ: {credor.cnpj}, localizada na {credor.endereco.logradouro}, {credor.endereco.numero}, bairro {credor.endereco.bairro}, na cidade {credor.endereco.cidade} - {credor.endereco.uf}, doravante denominada CREDORA</p>
    <p>E todos, em conjunto, denomindos PARTES, têm justo e acordado o presente "Termo de Renegociação Contratual e Confissão de Dívida", que se regerá pelos termos, clausulas e condições abaixo:</p>
    <p>Considerando que:</p>
    <p>{dividas.termo}</p>
    <h2>CLÁUSULA PRIMEIRA</h2>


</body>
</html>
'''