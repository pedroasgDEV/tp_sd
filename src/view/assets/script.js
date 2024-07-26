document.getElementById('region').addEventListener('change', function() {
    const stateSelect = document.getElementById('state');
    stateSelect.innerHTML = '<option value="">Selecione um estado</option>';
    stateSelect.disabled = !this.value;

    const states = {
        norte: ['am', 'pa', 'ro', 'rr', 'ap', 'to'],
        nordeste: ['ba', 'ce', 'ma', 'pi', 'se', 'pb', 'rn', 'al'],
        'centro-oeste': ['go', 'mt', 'ms', 'df'],
        sudeste: ['sp', 'rj', 'es', 'mg'],
        sul: ['pr', 'sc', 'rs']
    };

    if (this.value) {
        states[this.value].forEach(state => {
            const option = document.createElement('option');
            option.value = state;
            option.textContent = state.toUpperCase();
            stateSelect.appendChild(option);
        });
    }
});

document.getElementById('personaForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const numPersonas = parseInt(document.getElementById('numPersonas').value, 10);
    const region = document.getElementById('region').value;
    const state = document.getElementById('state').value;
    
    fetch('/personas/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': 'meu-token-secreto'
        },
        body: JSON.stringify({ numPersonas, region, state })
    })
    .then(response => response.json())
    .then(data => {
        window.location.href = '/personasGeradas';
    })
    .catch(error => console.error('Error:', error));
});
