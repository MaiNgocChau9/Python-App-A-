"""
Temperature = Mức độ sáng tạo
Top_p = Mức độ kiểm soát
Top_k = Mức độ chi tiết
"""

import google.generativeai as genai

genai.configure(api_key="AIzaSyDf_CTLM3mIPCx5n7fmNAtEQW5QeT2jgI0")
check_generation_config = {"temperature": 1,"top_p": 1,"top_k": 1,"max_output_tokens": 5,}
check_model = genai.GenerativeModel(model_name="gemini-pro",generation_config=check_generation_config)
check_generation_config = ["System: Nếu câu hỏi có yêu cầu liên quan đến việc đọc tất cả nội dung ghi chú hãy trả lời \"true\", không thì trả lời \"false\"", "Câu hỏi:" + str(input("User: ")),]
response = check_model.generate_content(check_generation_config)
print("AI:",response.text)