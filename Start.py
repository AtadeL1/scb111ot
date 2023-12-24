import asyncio
import logging
import subprocess
from Worker.config import *

# Полные пути к скриптам
worker_script_path = 'Worker/bot.py'
arbitrage_script_path = 'ArbitrageBot/bot.py'
casino_script_path = 'Casino/bot.py'
trade_script_path = 'Trade/bot.py'

# Запуск скриптов в отдельных процессах
async def run_bot(script_path):
    try:
        process = await asyncio.create_subprocess_exec('python', script_path,
                                                       stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = await process.communicate()
        if process.returncode != 0:
            logging.error(f"Error starting {script_path}: {stderr.decode()}")
    except Exception as e:
        logging.error(f"Unexpected error starting {script_path}: {e}")

async def main():
    await asyncio.gather(
        run_bot(worker_script_path),
        run_bot(arbitrage_script_path),
        run_bot(casino_script_path),
        run_bot(trade_script_path),
    )

# Настройка логгирования
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    asyncio.run(main())
