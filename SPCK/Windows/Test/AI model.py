import google.generativeai as genai

genai.configure(api_key="AIzaSyDf_CTLM3mIPCx5n7fmNAtEQW5QeT2jgI0")

# Set up the model
generation_config = {"temperature": 0.9,"top_p": 1,"top_k": 1,"max_output_tokens": 100000}

model = genai.GenerativeModel(model_name="gemini-1.0-pro", generation_config=generation_config)

convo = model.start_chat(history=[])
while True:
    convo.send_message(input(">>> "))
    print(convo.last.text)