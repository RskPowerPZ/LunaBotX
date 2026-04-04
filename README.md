# LunaBotX

# 🔥 NSFW Killer Bot - Auto Delete 18+ Content

**Advanced Telegram Bot** jo group mein aane wali har photo, video, GIF, sticker, animation aur document ko real-time scan karta hai aur NSFW (porn, nude, hentai, sexy) content ko turant delete kar deta hai.

Built with **aiogram 3.x** + Falcon's NSFW model + NudeNet (optional)

---

## ✨ Features

- Real-time NSFW detection on **photos, videos, GIFs, stickers, documents**
- Colored premium buttons with custom emoji support
- Auto delete + optional auto-mute / auto-ban
- Adjustable NSFW threshold
- Admin commands with beautiful HTML + emoji UI
- Easy deployment on **VPS** or **Railway / Render / Koyeb** (Heroku free tier dead in 2026)
- Zero cost local ML model (no API calls)

---

## 📋 Requirements

- Python 3.11+
- Telegram Bot Token
- API_ID & API_HASH (my.telegram.org)
- VPS ya cloud (minimum 1GB RAM recommended for video scanning)

---

## 🚀 Quick Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/nsfw-killer-bot.git
cd nsfw-killer-bot
2. Install Dependencies
pip install -r requirements.txt
3. Configure Bot
config.py file banao aur yeh daal do:
API_ID = 12345678
API_HASH = "your_api_hash_here"
BOT_TOKEN = "123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11"

NSFW_THRESHOLD = 0.65          # 0.0 to 1.0 (higher = stricter)
AUTO_MUTE = True
AUTO_BAN = False
MUTE_DURATION = 3600           # seconds (1 hour)
4. Run the Bot
python bot.py
🛠️ Deployment Guides
VPS (Ubuntu 22.04/24.04) - Recommended
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python & dependencies
sudo apt install python3.11 python3-pip python3-venv git -y

# Clone & setup
git clone https://github.com/yourusername/nsfw-killer-bot.git
cd nsfw-killer-bot
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run in background with pm2 or screen
screen -S nsfwbot
python bot.py
Permanent run with PM2 (best):
npm install -g pm2
pm2 start bot.py --name "nsfw-killer" --interpreter python3
pm2 save
pm2 startup
