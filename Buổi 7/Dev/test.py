from PyQt6.QtWidgets import QApplication, QTextBrowser, QVBoxLayout, QWidget

app = QApplication([])

window = QWidget()
layout = QVBoxLayout(window)

text_browser = QTextBrowser()
layout.addWidget(text_browser)
temp = "ABC"
text = "DEF"

# Sử dụng HTML và CSS để đặt kích thước chữ khác nhau
html_content = f"""
# You

Với tư cách là một mô hình ngôn ngữ lớn, tôi có thể hỗ trợ bạn trong nhiều nhiệm vụ khác nhau, bao gồm:

**Xử lý ngôn ngữ:**
- Sinh văn bản: Tôi có thể tạo các văn bản tự nhiên giống như người viết, bao gồm bài viết, bài đăng trên mạng xã hội, tin tức, v.v.
- Trích xuất thông tin: Tôi có thể trích xuất thông tin và sự kiện quan trọng từ văn bản, bảng và trang web.
- Tóm tắt nội dung: Tôi có thể tóm tắt nội dung của một văn bản thành một tóm tắt ngắn gọn, nhấn mạnh các điểm chính.
- Dịch thuật: Tôi có thể dịch văn bản từ ngôn ngữ này sang ngôn ngữ khác.
- Nhận dạng ngôn ngữ: Tôi có thể xác định ngôn ngữ của một đoạn văn bản.
- Phân loại văn bản: Tôi có thể phân loại văn bản thành các danh mục như tin tức, thể thao, kinh doanh, giải trí, v.v.
- Khởi tạo văn bản: Tôi có thể tạo các đoạn văn bản dựa trên một chủ đề hoặc yêu cầu cụ thể.

**Viết nội dung sáng tạo:**
- Thơ: Tôi có thể tạo thơ ở nhiều thể loại khác nhau, như thơ trữ tình, thơ tự do, thơ Haiku, v.v.
- Câu chuyện: Tôi có thể tạo các câu chuyện ở nhiều thể loại khác nhau, như khoa học viễn tưởng, giả tưởng, lãng mạn, kinh dị, v.v.
- Kịch bản: Tôi có thể tạo các kịch bản phim, kịch sân khấu, v.v.
- Bài hát: Tôi có thể viết lời bài hát ở nhiều thể loại khác nhau, như nhạc Pop, Rock, Rap, Ballade, v.v.

**Kiến thức tổng quát:**
- Trả lời câu hỏi: Tôi có thể trả lời các câu hỏi về nhiều lĩnh vực khác nhau, dựa trên kiến thức được đào tạo của tôi.
- Xác minh thông tin: Tôi có thể xác minh thông tin bằng cách tham chiếu đến các nguồn đáng tin cậy.
- Tìm kiếm thông tin: Tôi có thể tìm kiếm thông tin trên Internet và trả lại kết quả liên quan.
- Đề xuất: Tôi có thể đề xuất các sản phẩm, dịch vụ, địa điểm, v.v. phù hợp với nhu cầu hoặc sở thích của bạn.

**Trò chuyện và tương tác:**
- Trò chuyện: Tôi có thể trò chuyện với bạn về nhiều chủ đề khác nhau, như thời tiết, tin tức, thể thao, giải trí, v.v.
- Hỗ trợ khách hàng: Tôi có thể cung cấp dịch vụ hỗ trợ khách hàng thông qua trò chuyện, giúp giải quyết các vấn đề hoặc thắc mắc của khách hàng.
- Trò chơi: Tôi có thể chơi nhiều trò chơi khác nhau với bạn, như đố vui, cờ vua, cờ caro, v.v.

**Các tác vụ khác:**
- Tạo mã: Tôi có thể tạo mã trong nhiều ngôn ngữ lập trình khác nhau.
- Dịch thuật ngôn ngữ lập trình: Tôi có thể dịch mã từ ngôn ngữ lập trình này sang ngôn ngữ lập trình khác.
- Tạo cơ sở dữ liệu: Tôi có thể tạo cơ sở dữ liệu và thực hiện các thao tác truy vấn, cập nhật, xóa dữ liệu.
- Phân tích dữ liệu: Tôi có thể phân tích dữ liệu và tạo ra các báo cáo, biểu đồ để thể hiện kết quả.
- Tạo hình ảnh: Tôi có thể tạo các hình ảnh, biểu đồ, sơ đồ bằng m- Phân tích dữ liệu: Tôi có thể phân tích dữ liệu và tạo ra các báo cáo, biểu đồ để thể hiện kết quả.
- Tạo hình ảnh: Tôi có thể tạo các hình ảnh, biểu đồ, sơ đồ bằng mã hoặc giao diện đồ họa.
"""

text_browser.setMarkdown(html_content)

window.show()
app.exec()
