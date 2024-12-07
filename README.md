# Discord-Bot-For-Checking-Server-Status

A Discord bot that monitors the status of a host and port, checking if they are live and updating the status accordingly.

---

**Steps to set this up in your discord server**

1. Connect to <a href="https://discord.com/developers/applications" target="_blank">the discord developer portal</a> and connect your discord account.
2. Navigate to the **Bot** tab on the left navigation bar and create a bot. Copy the bot's token (will be used for the env variable).
3. Navigate to the **OAuth2** page where you will configure a URL for your bot to join the server of choice. Select **bot** as scope and enable necessary permissions. When you input the URL, it will open Discord and prompt you to select a server.
4. **Important!** Under the **Bot** tab in the Discord Developer Portal, enable **Presence Intent**, **Server Members Intent**, and **Message Content Intent** to cover your bases.
5. The bot should now be added and have the necessary permissions to operate.

---

**main.py Configuration**

1. In `main.py`, ensure you configure the following:
   - Get your environment variable running with your bot's token (line 8).
   - Input the host IP or domain name (line 27).
   - Input the port number (line 28). This is set to `25565` by default since I am hosting a Minecraft server.

---

**Side Note:** Run `main.py` either on a hosted instance (recommended) or locally on your system (will only run while the script is running).





