document.addEventListener('DOMContentLoaded', () => {
    const cropForm = document.getElementById('cropForm');
    const cropDetails = document.getElementById('cropDetails');

    cropForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const cropName = document.getElementById('cropName').value;
        
        try {
            console.log('Sending request to server...');
            const response = await fetch('http://localhost:5000/crop-details', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name: cropName }),
            });
            
            console.log('Response status:', response.status);
            console.log('Response headers:', response.headers);

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            console.log('Received data:', data);
            displayCropDetails(data);
        } catch (error) {
            console.error('Error:', error);
            cropDetails.innerHTML = `<p>Error fetching crop details: ${error.message}</p>`;
        }
    });

    function displayCropDetails(data) {
        cropDetails.innerHTML = `
            <h2>${data.name}</h2>
            <p><strong>Climate:</strong> ${data.climate}</p>
            <p><strong>Temperature:</strong> ${data.temperature}</p>
            <p><strong>Soil Type:</strong> ${data.soil_type}</p>
            <p><strong>Growing Method:</strong> ${data.growing_method}</p>
        `;
    }
});