from bot import Bot
from riot import Riot

if __name__ == '__main__':
    # bot = Bot()
    # bot.run_bot()
    bot = Riot('na1', 'iiihaltz')
    print(bot.get_puuid())

