# bot.py
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from utilities.http_client import ApiClient

API_BASE_URL = "http://localhost:8000"
BOT_TOKEN = '8664447680:AAHWl9_aPtPn5wda2do6UZgLBShN1biDXc0'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
api_client = ApiClient(base_url=API_BASE_URL)


def format_locations(locations: list) -> str:
    if not locations:
        return "Локации не найдены"
    result = "Доступные локации:\n\n"
    for loc in locations:
        name = loc.get('location', 'Без названия')
        result += f"- {name}\n"
    return result


def format_detectives(detectives: list) -> str:
    if not detectives:
        return "Детективы не найдены"
    result = "Информация о детективах:\n\n"
    for det in detectives:
        name = det.get('detective name', 'Неизвестный')
        clues = det.get('clue count', 0)
        result += f"- Детектив {name}, улики — {clues} шт.\n"
    return result


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Команды:\n/locations\n/detectives")


@dp.message(Command('locations'))
async def cmd_locations(message: types.Message):
    response = await api_client.get_locations()
    if response.status == 200:
        data = await response.json()
        locations = data[0] if isinstance(data, list) else data
        await message.answer(format_locations(locations))
    else:
        await message.answer(f"⚠️ Ошибка API: статус {response.status}")


@dp.message(Command('detectives'))
async def cmd_detectives(message: types.Message):
    response = await api_client.get_detectives()
    if response.status == 200:
        data = await response.json()
        detectives = data[0] if isinstance(data, list) else data
        await message.answer(format_detectives(detectives))
    else:
        await message.answer(f"⚠️ Ошибка API: статус {response.status}")


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    finally:
        await api_client.close()  # Обязательно закрываем сессию


if __name__ == "__main__":
    asyncio.run(main())