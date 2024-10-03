import streamlit as st
from src.authenticate import login, register, guest_login
import src.sidebar as sidebar

def main():
    sidebar.show_sidebar()

    # Kiểm tra trạng thái đăng nhập.
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False  # Khởi tạo trạng thái đăng nhập là False.

    # Nếu chưa đăng nhập, hiển thị giao diện đăng nhập.
    if not st.session_state.logged_in:
        with st.expander('**LANNY - SCHOOL CHATBOT**', expanded=True):
            # Tạo các tab cho đăng nhập, tạo tài khoản, và đăng nhập với tư cách khách.
            login_tab, create_tab, guest_tab = st.tabs(
                [
                    "Đăng nhập",  # Tab đăng nhập.
                    "Tạo tài khoản",  # Tab tạo tài khoản mới.
                    "Khách"  # Tab đăng nhập với tư cách khách.
                ]
            )
            with create_tab:
                register()  # Gọi hàm đăng ký tài khoản mới.
            with login_tab:
                login()  # Gọi hàm đăng nhập.
            with guest_tab:
                guest_login()  # Gọi hàm đăng nhập với tư cách khách.
    else:
        st.switch_page("pages\Chat.py")  # Chuyển trang đến chức năng chat.

        # Hiển thị lời chào và thông báo chào mừng người dùng đã đăng nhập thành công.
        st.success(f'Chào mừng {st.session_state.username}, tôi mong rằng bạn sẽ có trải nghiệm tuyệt vời!', icon="🎉")

if __name__ == "__main__":
    main()
