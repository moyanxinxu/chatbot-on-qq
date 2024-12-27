import botpy
from botpy.message import C2CMessage
from langchain_google_genai import ChatGoogleGenerativeAI

from config import GEMINI_CONFIG, CLIENT_CONFIG

llm_config = GEMINI_CONFIG().todict()
client_config = CLIENT_CONFIG().todict()

llm = ChatGoogleGenerativeAI(**llm_config)


class ChatBot(botpy.Client):
    async def on_c2c_message_create(self, message: C2CMessage):

        response = llm.invoke(message.content).content

        await message._api.post_c2c_message(
            openid=message.author.user_openid,
            msg_type=0,
            msg_id=message.id,
            content=f"{response}",
        )


if __name__ == "__main__":
    intents = botpy.Intents(public_messages=True)

    client = ChatBot(intents=intents)
    client.run(**client_config)
