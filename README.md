
<h1 align="center">
  <span style="color:#6C63FF;">LunaBotX</span>
</h1>

<p align="center">
  <b style="font-size:16px;">Advanced NSFW Protection Engine for Telegram</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/AI-Detection-6C63FF?style=for-the-badge">
  <img src="https://img.shields.io/badge/Real--Time-Processing-00C897?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-3.11+-FFD43B?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Stable-success?style=for-the-badge">
</p>

---

<div align="center">

<table>
<tr>
<td align="center" width="220">

<b>⚡ Fast Detection</b><br>
<span style="color:gray;">Processes media instantly</span>

</td>
<td align="center" width="220">

<b>🧠 AI Powered</b><br>
<span style="color:gray;">Local ML models, no API</span>

</td>
<td align="center" width="220">

<b>🛡️ Auto Moderation</b><br>
<span style="color:gray;">Delete • Mute • Ban</span>

</td>
</tr>
</table>

</div>

---

## <span style="color:#6C63FF;">Overview</span>

LunaBotX is a high-performance Telegram moderation system designed to automatically detect and eliminate NSFW content in real time.

It actively scans incoming media including images, videos, GIFs, stickers, animations, and documents — ensuring your community stays clean without manual intervention.

---

## <span style="color:#00C897;">Core Capabilities</span>

<div>

<ul>
<li><b style="color:#6C63FF;">Real-time media scanning</b></li>
<li><b style="color:#6C63FF;">Multi-format support</b> — images, videos, GIFs, stickers</li>
<li><b style="color:#6C63FF;">Adjustable sensitivity threshold</b></li>
<li><b style="color:#6C63FF;">Instant deletion system</b></li>
<li><b style="color:#6C63FF;">Automated mute & ban controls</b></li>
<li><b style="color:#6C63FF;">Stylish admin interface</b></li>
<li><b style="color:#6C63FF;">Zero external API dependency</b></li>
</ul>

</div>

---

## <span style="color:#FFD43B;">Technology Stack</span>

<table>
<tr>
<td><b>Framework</b></td>
<td>aiogram 3.x</td>
</tr>
<tr>
<td><b>Detection Engine</b></td>
<td>Falcon NSFW Model</td>
</tr>
<tr>
<td><b>Optional Layer</b></td>
<td>NudeNet</td>
</tr>
<tr>
<td><b>Language</b></td>
<td>Python 3.11+</td>
</tr>
</table>

---

## <span style="color:#6C63FF;">Setup Guide</span>

### <span style="color:#00C897;">Clone Repository</span>

```bash
git clone https://github.com/yourusername/nsfw-killer-bot.git
cd nsfw-killer-bot
Install Dependencies
Bash
pip install -r requirements.txt
Configuration
Python
API_ID = 12345678
API_HASH = "your_api_hash_here"
BOT_TOKEN = "your_bot_token_here"

NSFW_THRESHOLD = 0.65
AUTO_MUTE = True
AUTO_BAN = False
MUTE_DURATION = 3600
Run Bot
Bash
python bot.py
Production Deployment
VPS Setup
Bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3.11 python3-pip python3-venv git -y

git clone https://github.com/yourusername/nsfw-killer-bot.git
cd nsfw-killer-bot

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Run in Background
Bash
screen -S lunabotx
python bot.py
PM2 (Recommended)
Bash
npm install -g pm2
pm2 start bot.py --name "lunabotx" --interpreter python3
pm2 save
pm2 startup
Configuration Reference
�
ParameterDescriptionNSFW_THRESHOLDControls strictness levelAUTO_MUTEEnable or disable mutingAUTO_BANEnable or disable banningMUTE_DURATIONMute duration in seconds
Additional Notes
Runs completely offline after setup
No subscription or API costs
Designed for high-traffic groups
Efficient and lightweight
Contributing
Contributions are welcome. Open an issue before submitting major changes.
License
MIT License
�
If this project helps you, consider giving it a star 
```
