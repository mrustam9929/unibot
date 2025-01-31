import asyncio

from bots.main.bot import bot

from bots.main.dispatcher import dispatcher


async def main() -> None:
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
