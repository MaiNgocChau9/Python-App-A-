"""
Temperature = Mức độ sáng tạo
Top_p = Mức độ kiểm soát
Top_k = Mức độ chi tiết
"""

import google.generativeai as genai
user = "Câu hỏi:" + str(input("User: "))
genai.configure(api_key="AIzaSyDf_CTLM3mIPCx5n7fmNAtEQW5QeT2jgI0")
generation_config = {"temperature": 0.5,"top_p": 1,"top_k": 1,"max_output_tokens": 50,}
# safety_settings = [{"category": "HARM_CATEGORY_HARASSMENT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},{"category": "HARM_CATEGORY_HATE_SPEECH","threshold": "BLOCK_MEDIUM_AND_ABOVE"},{"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},{"category": "HARM_CATEGORY_DANGEROUS_CONTENT","threshold": "BLOCK_MEDIUM_AND_ABOVE"},]
model = genai.GenerativeModel(model_name="gemini-pro",generation_config=generation_config) # ,safety_settings=safety_settings
# prompt_parts = ["System: Nếu để trả lời câu hỏi 1 cách chính xác mà cần đến việc đọc tất cả nội dung ghi chú hãy trả lời \"true\", không thì trả lời \"false\"", "Câu hỏi:" + str(input("User: ")),]
prompt_parts = ["System: Lưu ý: Đọc kĩ câu hỏi người dùng. Nếu người dùng yêu cầu action liên quan đến Spotify như \"mở nhạc, mở bài {tên bài hát} của {tên nghệ sĩ}, nhạc của {tên nghệ sĩ}, ...\" hãy trả lời \"true - spotify - {từ khóa tìm kiếm ở tiếng Anh}\", không thì trả lời \"false\"", user,]
response = model.generate_content(prompt_parts)
print("AI:",response.text)
prompt_parts = ["System: Lưu ý: Đọc kĩ câu hỏi người dùng. Nếu người dùng yêu cầu action liên quan đến Youtube như \"mở video, tìm kiếm video,...\" hãy trả lời \"true - youtube - {từ khóa tìm kiếm theo ngôn ngữ của câu hỏi, tránh bắt đầu bằng những từ như \"mở, phát,...\"}\", không thì trả lời \"false\"", user,]
response = model.generate_content(prompt_parts)
print("AI:",response.text)