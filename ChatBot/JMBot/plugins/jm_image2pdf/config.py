from pydantic import BaseModel

class Config(BaseModel):
    """Plugin Config Here"""
    pass


from nonebot import on_command
from nonebot.rule import to_me
from nonebot.exception import MatcherException
from nonebot.adapters import Message, MessageTemplate
from nonebot.params import CommandArg
from nonebot.adapters.console import Message, MessageSegment 

jm_command = on_command("jm", rule=to_me(), aliases={"JM", "Jm", "jM"}, priority=10, block=True)

@jm_command.handle()
async def handle_function(args: Message = CommandArg()):
    msg_jmIds = args.extract_plain_text()
    jmIds = []
    for seg_jmid in msg_jmIds:
        jmIds.append(seg_jmid.extract_plain_text())
    run(jmIds)
    try:
        await jm_command.finish("本子已下载")
    except MatcherException:
        raise
    except Exception as e:
        pass # do something here