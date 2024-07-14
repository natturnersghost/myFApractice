document.getElementById('jobForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    const formData = {
        location: document.getElementById('location').value,
        starttime: document.getElementById('starttime').value,
        stoptime: document.getElementById('stoptime').value,
        travel: parseFloat(document.getElementById('travel').value),
        rate: parseInt(document.getElementById('rate').value),
        number_of_movers: parseInt(document.getElementById('number_of_movers').value),
        mileage: parseInt(document.getElementById('mileage').value),
        uhaul: document.getElementById('uhaul').checked,
        loadSwap: document.getElementById('loadSwap').checked,
        other: document.getElementById('other').checked,
        fullService: document.getElementById('fullService').checked
    };

    try {
        const response = await fetch('http://localhost:8000/new_job', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(formData)
        });

        if (response.ok) {
            const jsonResponse = await response.json();
            console.log('Job created successfully:', jsonResponse);
        } else {
            console.error('Failed to create job:', response.statusText);
        }
    } catch (error) {
        console.error('Error:', error);
    }
});
