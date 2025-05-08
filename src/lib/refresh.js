export default async function triggerRefresh() {
    const button = document.querySelector('.refresh-button');
    const status = document.getElementById('status');

    button.disabled = true;
    status.textContent = 'Refreshing...';

    try {
        const response = await fetch(`http://${PI_IP}:8080/refresh`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                token: REFRESH_TOKEN
            })
        });

        if (response.ok) {
            status.textContent = 'Refresh triggered successfully!';
            status.style.color = '#4CAF50';
        } else {
            throw new Error('Refresh failed');
        }
    } catch (error) {
        status.textContent = 'Error: Could not connect to Raspberry Pi';
        status.style.color = '#f44336';
        console.error('Error triggering refresh:', error);
    } finally {
        button.disabled = false;
        setTimeout(() => {
            status.textContent = '';
        }, 3000);
    }
}