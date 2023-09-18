# Test Bot

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 -m bot
```
Docker 
```
docker build -t test-bot .
docker run -d --restart on-failure --name test-bot test-bot
```

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/template/Q03brk?referralCode=umbdWf)
