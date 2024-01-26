import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion, AzureChatCompletion
import email_client

def detect_tone(input_text):
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

    emailToneDetectionFunction = productivityFunctions["DetectTone"]

    inputEmail = input_text
    return emailToneDetectionFunction.invoke(inputEmail) 

if __name__ == "__main__":
    import sys

    # Accept input from command line arguments
    input_from_cmd = sys.argv[1] if len(sys.argv) > 1 else ""

    result = detect_tone(input_from_cmd)
    print(result)

