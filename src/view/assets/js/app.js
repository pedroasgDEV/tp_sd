document.addEventListener('DOMContentLoaded', () => {
    const form = document.createElement('form');

    const numberLabel = document.createElement('label');
    numberLabel.textContent = 'Qual o número de personas desejados?*';
    form.appendChild(numberLabel);

    const numberInput = document.createElement('input');
    numberInput.setAttribute('type', 'number');
    numberInput.setAttribute('placeholder', 'Número de Personas');
    numberInput.setAttribute('required', 'true');
    numberInput.setAttribute('min', '1');
    form.appendChild(numberInput);

    const regionLabel = document.createElement('label');
    regionLabel.textContent = 'Escolha a região:';
    form.appendChild(regionLabel);

    const regionSelect = document.createElement('select');
    const regions = ['', 'Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul'];
    regions.forEach(region => {
        const option = document.createElement('option');
        option.value = region;
        option.text = region;
        regionSelect.appendChild(option);
    });
    form.appendChild(regionSelect);

    const stateLabel = document.createElement('label');
    stateLabel.textContent = 'Escolha o estado:';
    form.appendChild(stateLabel);

    const stateSelect = document.createElement('select');
    form.appendChild(stateSelect);

    regionSelect.addEventListener('change', () => {
        const selectedRegion = regionSelect.value;
        const states = {
            'Norte': ['Acre', 'Amapá', 'Amazonas', 'Pará', 'Rondônia', 'Roraima', 'Tocantins'],
            'Nordeste': ['Alagoas', 'Bahia', 'Ceará', 'Maranhão', 'Paraíba', 'Pernambuco', 'Piauí', 'Rio Grande do Norte', 'Sergipe'],
            'Centro-Oeste': ['Distrito Federal', 'Goiás', 'Mato Grosso', 'Mato Grosso do Sul'],
            'Sudeste': ['Espírito Santo', 'Minas Gerais', 'Rio de Janeiro', 'São Paulo'],
            'Sul': ['Paraná', 'Rio Grande do Sul', 'Santa Catarina']
        };

        while (stateSelect.firstChild) {
            stateSelect.removeChild(stateSelect.firstChild);
        }

        if (selectedRegion) {
            states[selectedRegion].forEach(state => {
                const option = document.createElement('option');
                option.value = state;
                option.text = state;
                stateSelect.appendChild(option);
            });
        }
    });

    const submitButton = document.createElement('button');
    submitButton.type = 'submit';
    submitButton.textContent = 'Gerar Personas';
    form.appendChild(submitButton);

    const resultDiv = document.createElement('div');
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const response = await fetch('/api/personas', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'seu_token_unico'
            },
            body: JSON.stringify({
                number: numberInput.value,
                region: regionSelect.value,
                state: stateSelect.value
            })
        });
        const data = await response.json();
        resultDiv.textContent = data.message;
    });

    document.getElementById('app').appendChild(form);
    document.getElementById('app').appendChild(resultDiv);
});
