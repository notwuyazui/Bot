import nonebot
from nonebot.adapters.console import Adapter as ConsoleAdapter  # 避免重复命名
from nonebot.adapters.onebot.v11 import Adapter as OneBotV11Adapter  # 新增适配器

# 初始化 NoneBot
nonebot.init(
    # 使用完整驱动路径
    driver="nonebot.drivers.fastapi:Driver",
    _env_file=".env",
    apscheduler_config={"apscheduler.timezone": "Asia/Shanghai"}
)


# 注册适配器
driver = nonebot.get_driver()
driver.register_adapter(OneBotV11Adapter)  # 注册OneBot V11协议适配器
# driver.register_adapter(ConsoleAdapter)

# 在这里加载插件
nonebot.load_builtin_plugins("echo")  # 内置插件
nonebot.load_plugin("nonebot_plugin_jmcomic")  # 第三方插件
# nonebot.load_plugins("awesome_bot/plugins")  # 本地插件

if __name__ == "__main__":
    nonebot.run(host="0.0.0.0", port=8080)