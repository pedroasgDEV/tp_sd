document.addEventListener("DOMContentLoaded", function() {
    if (document.getElementById('personas')) {
        fetch('http://localhost:3000/person')
            .then(response => response.json())
            .then(data => {
                const personasList = document.getElementById('personas');
                data.forEach(persona => {
                    const li = document.createElement('li');
                    li.textContent = `${persona.name} - ${persona.cpf}`;
                    personasList.appendChild(li);
                });
            })
            .catch(error => console.error('Error:', error));
    }

    const personaForm = document.getElementById('personaForm');
    if (personaForm) {
        personaForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const formData = new FormData(personaForm);
            const jsonData = {};
            formData.forEach((value, key) => jsonData[key] = value);

            fetch('http://localhost:3000/person', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(jsonData)
            })
            .then(response => response.json())
            .then(data => {
                alert('Persona criada com sucesso!');
                window.location.href = 'index.html';
            })
            .catch(error => console.error('Error:', error));
        });
    }
});
