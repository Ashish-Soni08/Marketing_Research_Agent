from dotenv import dotenv_values

from llama_index.llms.nvidia import NVIDIA
from llama_index.embeddings.nvidia import NVIDIAEmbedding
from llama_index.core.postprocessor.nvidia_rerank import NVIDIAReRank
from llama_index.core.llms import ChatMessage, MessageRole

from constants import (EMBEDDING_MODEL,
                       LLM_MODEL,
                       RERANK_MODEL
                       )

config = dotenv_values(".env")

llm = NVIDIA(base_url=config["NVIDIA_URL"],
             api_key=config["LLM_API_KEY"],
             model=LLM_MODEL)

messages = [
    ChatMessage(
        role=MessageRole.SYSTEM, content=("You are a helpful assistant.")
    ),
    ChatMessage(
        role=MessageRole.USER,
        content=("What is your name?"),
    ),
]

response = llm.stream_chat(messages)
print(response)

last_element = None
for last_element in response:
    pass

print(last_element)

def get_embeddings():

    
    return None

embedding_model = NVIDIAEmbedding(base_url=config["NVIDIA_URL"], 
                                  api_key=config["EMBED_MODEL_API_KEY"],
                                  model=EMBEDDING_MODEL,
                                  truncate="NONE"
                                  )

rerank_model = NVIDIAReRank(base_url=config["NVIDIA_RERANK_URL"],
                            api_key=config["RERANK_MODEL_API_KEY"],
                            model=RERANK_MODEL
                            )
