class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self,ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.ai_settings.ship_limit
        with open('score.txt','r+') as file_object:
            self.high_score = int(file_object.read())
        self.score = 0
        self.level = 1