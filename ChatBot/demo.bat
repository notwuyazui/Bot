python -m pip install --user pipx
python -m pipx ensurepath
pipx install nb-cli
cd JMBot/
python -m venv .venv --prompt nonebot2
.venv/Scripts/activate
pip install 'nonebot2[fastapi]'
pip install nonebot-adapter-console
pip install nonebot-plugin-jmcomic
nb plugin install nonebot-plugin-deepseek
python bot.py