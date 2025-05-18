import {
    PUBLIC_N8N_PROD_URL,
    PUBLIC_N8N_TEST_URL,
    PUBLIC_N8N_USER,
    PUBLIC_N8N_PASS
} from '$env/static/public';

export async function n8nSheetsReq(params) {
    try {
        const response = await fetch(sheetsRequest);
        const data = await response.json();
        jsonData = data; // Store the data
        console.log('Sheets data:', jsonData);
        return data;
    } catch (error) {
        console.error('Failed to get sheet data:', error);
        return null;
    } finally {
    }
}