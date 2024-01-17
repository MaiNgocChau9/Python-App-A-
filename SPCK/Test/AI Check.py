"""
Temperature = Mức độ sáng tạo
Top_p = Mức độ kiểm soát
Top_k = Mức độ chi tiết
"""

import google.generativeai as genai

genai.configure(api_key="AIzaSyDf_CTLM3mIPCx5n7fmNAtEQW5QeT2jgI0")
generation_config = {"temperature": 1,"top_p": 1,"top_k": 1,"max_output_tokens": 5,}
safety_settings = [{"category": "HARM_CATEGORY_HARASSMENT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},{"category": "HARM_CATEGORY_HATE_SPEECH","threshold": "BLOCK_MEDIUM_AND_ABOVE"},{"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},{"category": "HARM_CATEGORY_DANGEROUS_CONTENT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},]
model = genai.GenerativeModel(model_name="gemini-pro",generation_config=generation_config,safety_settings=safety_settings)
prompt_parts = ["System: Nếu câu hỏi có yêu cầu liên quan đến việc đọc tất cả nội dung ghi chú hãy trả lời \"true\", không thì trả lời \"false\"", "Câu hỏi:" + str(input("User: ")),]
response = model.generate_content(prompt_parts)
print("AI:",response.text)