import asyncio

from bots.main.bot import dp, bot


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
