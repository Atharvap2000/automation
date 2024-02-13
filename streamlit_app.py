import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

def openWebsite():
    chromedriver_autoinstaller.install()  
    chrome_options = webdriver.ChromeOptions()
    # service = Service(executable_path="chromedriver.exe")
    # options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options = chrome_options)
    driver.maximize_window()
    driver.get("https://capgemini-technology-3.us10.hcs.cloud.sap/dwaas-ui/index.html")
    
def authenticate(username, password):
    # Add your authentication logic here
    # For simplicity, let's check if username and password match predefined values
    return username == "user" and password == "password"

def main():
    st.title("Test Automation")

    # Get or create session_state
    session_state = st.session_state
    if "user_authenticated" not in session_state:
        session_state.user_authenticated = False

    if not session_state.user_authenticated:
        # Login
        st.sidebar.subheader("Login")
        username = st.sidebar.text_input("Username:")
        password = st.sidebar.text_input("Password:", type="password")
        login_button = st.sidebar.button("Login")

        if login_button:
            if authenticate(username, password):
                session_state.user_authenticated = True
            else:
                st.sidebar.error("Invalid username or password. Please try again.")
    else:
        # Provide user with different options after successful login
        options = ["", "Migration", "Object Creation", "Documentation"]
        selected_option = st.selectbox("Select an option:", options)

        # Perform different functions based on the selected option
        if selected_option == "Migration":
            st.write("Migration selected")
            openWebsite()
        elif selected_option == "Object Creation":
             st.write("Object creation selected")
        elif selected_option == "Documentation":
            st.write("RD selected")

        # Logout
        logout_button = st.sidebar.button("Logout")
        if logout_button:
            session_state.user_authenticated = False

# Your authentication and input functions go here

if __name__ == "__main__":
    main()
