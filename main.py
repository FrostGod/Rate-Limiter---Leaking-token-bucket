import streamlit as st
from leaking_token_bucket import RateLimiter


my_instance = []

def authenticate(username, password, RL):
    # Replace these with your actual username and password
    valid_username = "user"
    valid_password = "password"
    return username == valid_username and password == valid_password

def get_or_create_instance():
    if not my_instance:
        st.session_state.my_instance = RateLimiter()
    my_instance.append(st.session_state.my_instance)
    return st.session_state.my_instance

def main():
    RL = get_or_create_instance()
    # RL.flush_cache()
    st.title("Authentication Page")
    # Input fields for username and password
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    # Button to trigger authentication
    if st.button("Login"):
        allow = RL.check_rate_limit(username)
        if not allow:
            st.error("Error 429: Too Many Requests. Please try again later.")
        if authenticate(username, password, RL):
            print(type(username))
            st.success("Authentication successful!")
            # Add your app logic or redirect to another page after successful authentication
        else:
            st.error("Authentication failed. Please try again.")


if __name__ == "__main__":
    print("hi")
    main()