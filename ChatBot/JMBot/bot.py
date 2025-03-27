import nonebot
from nonebot.adapters.console import Adapter as ConsoleAdapter  # 避免重复命名

# 初始化 NoneBot
nonebot.init()

# 加载插件
nonebot.run()

# 注册适配器
driver = nonebot.get_driver()
driver.register_adapter(ConsoleAdapter)

# 在这里加载插件
nonebot.load_builtin_plugins("echo")  # 内置插件

# 第三方插件
# nonebot.load_plugin("nonebot-plugin-deepseek")  # deekseek对话
# nonebot.load_plugin("nonebot-plugin-dingzhen")  # 丁真语音

# 本地插件
nonebot.load_plugins("plugins")  

if __name__ == "__main__":
    nonebot.run()