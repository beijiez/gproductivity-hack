import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.connectors.ai.open_ai import (
    OpenAIChatCompletion,
    OpenAITextEmbedding,
    AzureChatCompletion,
    AzureTextEmbedding,
)
import email_client
import asyncio

COLLECTION_NAME = "SKoutlook"
MAX_TOKEN_LENGTH = 8000

async def find_in_emails(user_input):
    kernel = sk.Kernel()

    useAzureOpenAI = True

    # Configure AI service used by the kernel
    if useAzureOpenAI:
        deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
        azure_text_service = AzureChatCompletion(
            deployment_name="tutorial", endpoint=endpoint, api_key=api_key
        )  # set the deployment name to the value of your text model
        # an embedding is required to use the memory store
        azure_text_embedding = AzureTextEmbedding(deployment_name="text-embedding", endpoint=endpoint, api_key=api_key)
        kernel.add_text_completion_service("dv", azure_text_service)
        kernel.add_text_embedding_generation_service("ada", azure_text_embedding)
    else:
        api_key, org_id = sk.openai_settings_from_dot_env()
        oai_text_service = AzureChatCompletion(ai_model_id="gpt-3.5-turbo-instruct", api_key=api_key, org_id=org_id)
        # an embedding is required to use the memory store
        oai_text_embedding = OpenAITextEmbedding(ai_model_id="text-embedding-ada-002", api_key=api_key, org_id=org_id)
        kernel.add_text_completion_service("dv", oai_text_service)
        kernel.add_text_embedding_generation_service("ada", oai_text_embedding)
        
    contents_dict = email_client.get_contents()
    kernel.register_memory_store(memory_store=sk.memory.VolatileMemoryStore())
    kernel.import_plugin(sk.core_plugins.TextMemoryPlugin())
    
    count = 0
    for k, v in contents_dict.items():
        if v and k:
            v = v[:MAX_TOKEN_LENGTH]
            k = k[:MAX_TOKEN_LENGTH]
            await kernel.memory.save_information_async(
                    collection=COLLECTION_NAME,
                    description=v,
                    text=v,
                    id=k,
            )
            count += 1
    print(user_input)
    ask = f"Look for the following information from {user_input} in your saved email contents. Return the email SUBJECT and email description and answer to the question if a such email is found. Otherwise return 'No info found for such email'"
    memories = await kernel.memory.search_async(COLLECTION_NAME, ask, limit=3, min_relevance_score=0.5)
    response = []
    for memory in memories:
        result = "Subject: " + memory.id + "\n" + "Body: " + memory.description + "\n" + "Relevance: " + str(memory.relevance) + "\n"
        response.append(result)
    return response


if __name__ == "__main__":
    import sys

    # Accept input from command line arguments
    input_from_cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    result = asyncio.run(find_in_emails(input_from_cmd))
    sanitized_result = []
    
    for r in result:
        sanitized_result.append(r.encode('utf-8'))
    print(sanitized_result)