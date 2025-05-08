# Raspberry Pi Display Setup

This setup configures a Raspberry Pi to automatically load and refresh a website from a Netlify server.

## Prerequisites

- Raspberry Pi with Raspberry Pi OS
- Chromium browser installed
- Python 3.x installed
- Internet connection

## Setup Instructions

1. Install required Python packages:
   ```bash
   pip3 install requests
   ```

2. Create a directory for the display files:
   ```bash
   mkdir -p /home/pi/display
   ```

3. Copy all files to the display directory:
   ```bash
   cp pi_config.json startup_script.py /home/pi/display/
   ```

4. Edit the `pi_config.json` file with your specific settings:
   - Update `server_url` with your Netlify site URL
   - Set a secure `static_password`
   - Adjust `refresh_interval_hours` as needed

5. Install the systemd service:
   ```bash
   sudo cp pi-display.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable pi-display
   sudo systemctl start pi-display
   ```

6. Check the service status:
   ```bash
   sudo systemctl status pi-display
   ```

## Logging

Logs are stored in `/home/pi/display/pi_display.log`

## Troubleshooting

- Check the log file for errors
- Ensure the Raspberry Pi has internet connectivity
- Verify the server URL and authentication credentials
- Check if Chromium is installed: `sudo apt-get install chromium-browser`

## Security Notes

- Keep the `static_password` secure
- Regularly update the password
- Consider using HTTPS for all communications 