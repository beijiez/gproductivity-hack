import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, AzureChatCompletion
import email_client


kernel = sk.Kernel()

useAzureOpenAI = True

# Configure AI service used by the kernel
if useAzureOpenAI:
    deployment, api_key, endpoint = sk.azure_openai_settings_from_dot_env()
    azure_text_service = AzureChatCompletion(
        deployment_name="tutorial", endpoint=endpoint, api_key=api_key
    )  # set the deployment name to the value of your text model
    kernel.add_text_completion_service("dv", azure_text_service)
else:
    api_key, org_id = sk.openai_settings_from_dot_env()
    oai_text_service = AzureChatCompletion(ai_model_id="gpt-3.5-turbo-instruct", api_key=api_key, org_id=org_id)
    kernel.add_text_completion_service("dv", oai_text_service)
    
plugins_directory = "../semantic_kernel/plugins" # use "./plugins" if executing from hack/semantic_kernel/ directly

productivityFunctions = kernel.import_semantic_plugin_from_directory(plugins_directory, "ProductivityPlugin")

replyEmailFunction = productivityFunctions["ReplyEmail"]

inputEmail = "Hi folks, We have been piloting the \"Sync Day\" concept for the past 3 months in the UK. Now the pilot has concluded, we are reflecting on the three meetings with a view to drawing recommendations for Sync Days going forward both within the UK and beyond. Your open and honest feedback via this anonymous survey will be an important signal feeding into these recommendations if you can spare a few minutes to complete it. https://forms.office.com/r/ThREXBiRZL Regards Martin Kearn"

print(replyEmailFunction.invoke(inputEmail)) 

# TODO:
# - tone analysis
# - sample Front end  https://medium.com/uptake-tech/how-to-create-a-simple-frontend-api-and-model-with-python-vue-js-a51841c66f8a
# - follow up reminder

