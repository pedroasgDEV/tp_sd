document.getElementById('createPersonaForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    const personaData = {};
    formData.forEach((value, key) => {
        personaData[key] = value;
    });

    try {
        const response = await fetch('/personas/save', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'meu-token-secreto'
            },
            body: JSON.stringify(personaData)
        });
        const result = await response.json();
        alert(result.message);
        window.location.href = '/personasGeradas';
    } catch (error) {
        console.error('Erro:', error);
    }
});
