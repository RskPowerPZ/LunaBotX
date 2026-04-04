<h1 align="center">🚀 LunaBotX</h1>
<h3 align="center">Advanced NSFW Protection Bot for Telegram Groups</h3>

<p align="center">
  <img src="https://img.shields.io/badge/AI-Powered-blue?style=for-the-badge&logo=openai">
  <img src="https://img.shields.io/badge/Telegram-Bot-2CA5E0?style=for-the-badge&logo=telegram">
  <img src="https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge">
</p>

---

## 🔥 Overview

**LunaBotX** is a high-performance Telegram moderation bot designed to automatically detect and remove NSFW content in real-time.

It scans incoming media such as images, videos, GIFs, stickers, animations, and documents — instantly identifying inappropriate content and taking action without delay.

Built for reliability, speed, and zero API dependency.

---

## ✨ Key Features

- ⚡ Real-time NSFW detection  
- 🖼️ Supports photos, videos, GIFs, stickers & documents  
- 🎯 Adjustable detection sensitivity  
- 🧠 AI-based local model (no external API required)  
- 🚫 Auto-delete unsafe content instantly  
- 🔇 Optional auto-mute system  
- 🔨 Optional auto-ban system  
- 🎛️ Clean admin commands with rich UI  
- 🌈 Custom emoji & styled buttons  
- 💸 Completely free to run (local inference)

---

## 🧩 Tech Stack

- **aiogram 3.x** — Telegram bot framework  
- **Falcon NSFW Model** — Core detection engine  
- **NudeNet** *(optional)* — Additional filtering layer  
- **Python 3.11+**

---

## 📋 Requirements

- Python **3.11 or higher**
- Telegram Bot Token
- `API_ID` & `API_HASH` from Telegram
- VPS or Cloud environment *(recommended: 1GB+ RAM for video processing)*

---

## 🚀 Quick Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/nsfw-killer-bot.git
cd nsfw-killer-bot
2️⃣ Install Dependencies
Bash
pip install -r requirements.txt
3️⃣ Configuration
Create a config.py file:
Python
API_ID = 12345678
API_HASH = "your_api_hash_here"
BOT_TOKEN = "your_bot_token_here"

NSFW_THRESHOLD = 0.65   # Range: 0.0 – 1.0 (higher = stricter)
AUTO_MUTE = True
AUTO_BAN = False
MUTE_DURATION = 3600    # seconds
4️⃣ Run the Bot
Bash
python bot.py
🛠️ Deployment Guide
💻 VPS (Recommended)
Bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install dependencies
sudo apt install python3.11 python3-pip python3-venv git -y

# Clone project
git clone https://github.com/yourusername/nsfw-killer-bot.git
cd nsfw-killer-bot

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip install -r requirements.txt
▶️ Run with Screen
Bash
screen -S lunabotx
python bot.py
⚡ Run with PM2 (Best for Production)
Bash
npm install -g pm2
pm2 start bot.py --name "lunabotx" --interpreter python3
pm2 save
pm2 startup
⚙️ Configuration Tips
Setting
Description
NSFW_THRESHOLD
Higher = stricter filtering
AUTO_MUTE
Enable/disable auto mute
AUTO_BAN
Enable/disable auto ban
MUTE_DURATION
Duration of mute (in seconds)
📌 Notes
Works entirely offline after setup
No API cost involved
Optimized for group moderation
Lightweight but powerful detection system
🤝 Contributing
Pull requests are welcome. For major changes, open an issue first to discuss your ideas.
📄 License
This project is open-source and available under the MIT License.
�
⭐ If you find this useful, consider starring the repository 
```
