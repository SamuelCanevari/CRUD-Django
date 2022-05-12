const urlEstados = "https://servicodados.ibge.gov.br/api/v1/localidades/estados";
const estado = document.getElementById("input-estado");
const cidade = document.getElementById("input-cidade");


window.addEventListener('load', async () => {
    const request = await fetch(urlEstados);
    const response = await request.json();

    const options = document.createElement("optgroup");
    options.setAttribute('label', 'Estados');

    var arrayEstados = [];
    response.forEach(function (uf) {
        arrayEstados.push(uf.nome);
    })
    var arrayEstadosOrdenados = arrayEstados.sort();

    options.innerHTML += "<option value='' disabled selected>- Selecione -</option>"
    arrayEstadosOrdenados.forEach(function (nome) {
        response.forEach(function (uf) {
            if (uf.nome == nome) {
                options.innerHTML += "<option value='" + nome + "'>" + nome + "</option>"
            }
        })
    })
    estado.append(options);
})

estado.addEventListener('change', async function () {

    var ConverterEstados = function (val) {
        var data;

        switch (val.toUpperCase()) {
            case "ACRE": data = "AC"; break;
            case "ALAGOAS": data = "AL"; break;
            case "AMAZONAS": data = "AM"; break;
            case "AMAPÁ": data = "AP"; break;
            case "BAHIA": data = "BA"; break;
            case "CEARÁ": data = "CE"; break;
            case "DISTRITO FEDERAL": data = "DF"; break;
            case "ESPÍRITO SANTO": data = "ES"; break;
            case "GOIÁS": data = "GO"; break;
            case "MARANHÃO": data = "MA"; break;
            case "MINAS GERAIS": data = "MG"; break;
            case "MATO GROSSO DO SUL": data = "MS"; break;
            case "MATO GROSSO": data = "MT"; break;
            case "PARÁ": data = "PA"; break;
            case "PARAÍBA": data = "PB"; break;
            case "PERNAMBUCO": data = "PE"; break;
            case "PIAUÍ": data = "PI"; break;
            case "PARANÁ": data = "PR"; break;
            case "RIO DE JANEIRO": data = "RJ"; break;
            case "RIO GRANDE DO NORTE": data = "RN"; break;
            case "RONDÔNIA": data = "RO"; break;
            case "RORAIMA": data = "RR"; break;
            case "RIO GRANDE DO SUL": data = "RS"; break;
            case "SANTA CATARINA": data = "SC"; break;
            case "SERGIPE": data = "SE"; break;
            case "SÃO PAULO": data = "SP"; break;
            case "TOCANTINS": data = "TO"; break;
        }
        return data;
    };

    const urlCidades = 'https://servicodados.ibge.gov.br/api/v1/localidades/estados/' + ConverterEstados(estado.value) + '/municipios';
    const request = await fetch(urlCidades);
    const response = await request.json();

    const options = document.createElement("optgroup");
    options.setAttribute('label', 'Cidades');

    var arrayCidades = [];
    response.forEach(function (cidade) {
        arrayCidades.push(cidade.nome);
    })

    var arrayCidadesOrdenadas = arrayCidades.sort();
    cidade.innerHTML = ""
    cidade.innerHTML = "<option value='' disabled selected>- Selecione -</option>"

    arrayCidadesOrdenadas.forEach(function (cidade) {
        options.innerHTML += "<option>" + cidade + "</option>"
    })

    cidade.append(options)
})




