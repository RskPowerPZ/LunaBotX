
<div align="center">

  <!-- Neon Header with Glow -->
  <h1 align="center">
    <span style="background: linear-gradient(90deg, #6C63FF, #00C897, #FFD43B); 
                 -webkit-background-clip: text; 
                 -webkit-text-fill-color: transparent; 
                 font-size: 3.5em; 
                 text-shadow: 0 0 30px rgba(108, 99, 255, 0.8);">
      🌙 LunaBotX
    </span>
  </h1>

  <p align="center">
    <b style="font-size: 18px; color: #FFFFFF; text-shadow: 0 0 15px #6C63FF;">
      Advanced NSFW Protection Engine for Telegram
    </b>
  </p>

  <!-- Shields with Neon Style -->
  <p align="center">
    <img src="https://img.shields.io/badge/AI-Detection-6C63FF?style=for-the-badge&logo=ai&logoColor=white" alt="AI Detection">
    <img src="https://img.shields.io/badge/Real--Time-Processing-00C897?style=for-the-badge&logo=rocket&logoColor=white" alt="Real-Time">
    <img src="https://img.shields.io/badge/Python-3.11+-FFD43B?style=for-the-badge&logo=python&logoColor=black" alt="Python">
    <img src="https://img.shields.io/badge/Status-Stable-00FF88?style=for-the-badge&logo=check-circle&logoColor=black" alt="Stable">
  </p>

  <img src="https://img.shields.io/github/stars/RskPowerPZ/LunaBotX?style=social" alt="Stars">
  <img src="https://img.shields.io/github/forks/RskPowerPZ/LunaBotX?style=social" alt="Forks">

</div>

---

<div align="center" style="background: linear-gradient(135deg, #1a0033, #000033); padding: 30px; border-radius: 20px; border: 2px solid #6C63FF; box-shadow: 0 0 40px rgba(108, 99, 255, 0.6);">

  <table>
    <tr>
      <td align="center" width="220" style="padding: 20px;">
        <h3 style="color: #00C897; margin: 0;">⚡ Fast Detection</h3>
        <p style="color: #BBBBFF; margin: 8px 0 0;">Processes media instantly</p>
      </td>
      <td align="center" width="220" style="padding: 20px;">
        <h3 style="color: #6C63FF; margin: 0;">🧠 AI Powered</h3>
        <p style="color: #BBBBFF; margin: 8px 0 0;">Local ML models, no API</p>
      </td>
      <td align="center" width="220" style="padding: 20px;">
        <h3 style="color: #FFD43B; margin: 0;">🛡️ Auto Moderation</h3>
        <p style="color: #BBBBFF; margin: 8px 0 0;">Delete • Mute • Ban</p>
      </td>
    </tr>
  </table>

</div>

---

## <span style="color:#6C63FF; text-shadow: 0 0 10px #6C63FF;">🌌 Overview</span>

**LunaBotX** ek high-performance Telegram moderation system hai jo **real-time** mein NSFW content ko detect karke automatically remove kar deta hai.

Yeh images, videos, GIFs, stickers, animations aur documents sab ko scan karta hai — bina manual intervention ke aapki community clean rakhta hai.

---

## <span style="color:#00C897; text-shadow: 0 0 10px #00C897;">🔥 Core Capabilities</span>

<div style="background: #0a0022; padding: 25px; border-radius: 15px; border-left: 6px solid #00C897;">

- **<span style="color:#6C63FF;">Real-time media scanning</span>**
- **<span style="color:#6C63FF;">Multi-format support</span>** — images, videos, GIFs, stickers
- **<span style="color:#6C63FF;">Adjustable sensitivity threshold</span>**
- **<span style="color:#6C63FF;">Instant deletion system</span>**
- **<span style="color:#6C63FF;">Automated mute & ban controls</span>**
- **<span style="color:#6C63FF;">Stylish admin interface</span>**
- **<span style="color:#6C63FF;">Zero external API dependency</span>**

</div>

---

## <span style="color:#FFD43B; text-shadow: 0 0 10px #FFD43B;">🛠️ Technology Stack</span>

<table style="background: #1a0033; border-collapse: collapse; width: 100%; border-radius: 12px; overflow: hidden;">
  <tr style="background: #2a0055;">
    <th style="padding: 15px; color: #FFD43B; text-align: left;">Component</th>
    <th style="padding: 15px; color: #FFD43B; text-align: left;">Technology</th>
  </tr>
  <tr>
    <td style="padding: 15px; color: #BBBBFF;">Framework</td>
    <td style="padding: 15px; color: #FFFFFF;"><b>aiogram 3.x</b></td>
  </tr>
  <tr style="background: #220044;">
    <td style="padding: 15px; color: #BBBBFF;">Detection Engine</td>
    <td style="padding: 15px; color: #FFFFFF;"><b>Falcon NSFW Model</b></td>
  </tr>
  <tr>
    <td style="padding: 15px; color: #BBBBFF;">Optional Layer</td>
    <td style="padding: 15px; color: #FFFFFF;"><b>NudeNet</b></td>
  </tr>
  <tr style="background: #220044;">
    <td style="padding: 15px; color: #BBBBFF;">Language</td>
    <td style="padding: 15px; color: #FFFFFF;"><b>Python 3.11+</b></td>
  </tr>
</table>

---

## <span style="color:#6C63FF; text-shadow: 0 0 10px #6C63FF;">🚀 Setup Guide</span>

### 1. Clone Repository

```bash
git clone https://github.com/RskPowerPZ/LunaBotX.git
cd LunaBotX
2. Install Dependencies
pip install -r requirements.txt
3. Configuration
Apne config.py ya environment mein yeh values daal do:
API_ID = 12345678
API_HASH = "your_api_hash_here"
BOT_TOKEN = "your_bot_token_here"

NSFW_THRESHOLD = 0.65      # 0.0 to 1.0 (higher = stricter)
AUTO_MUTE = True
AUTO_BAN = False
MUTE_DURATION = 3600       # seconds
4. Run the Bot
python bot.py
Production Deployment (VPS)
# Update system
sudo apt update && sudo apt upgrade -y
sudo apt install python3.11 python3-pip python3-venv git screen -y

# Clone & Setup
git clone https://github.com/RskPowerPZ/LunaBotX.git
cd LunaBotX
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Background mein chalane ke liye:
screen -S lunabotx
python bot.py
PM2 (Recommended):
npm install -g pm2
pm2 start bot.py --name "lunabotx" --interpreter python3
pm2 save
pm2 startup
