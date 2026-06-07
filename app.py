import streamlit as st
import hashlib
import requests

st.set_page_config(page_title="Fyers Token Generator", page_icon="📈")

st.title("Fyers Auto-Login Setup")

# Aapki Streamlit app ka link
redirect_uri = "https://accesstokengenratorfyers-yqp7rcqjyu8phh5gaode43.streamlit.app/"

# User Inputs
client_id = st.text_input("Client ID (App ID)", placeholder="e.g., XXXXXX-100")
secret_key = st.text_input("Secret Key", type="password")

# STEP 1: Login Link Generate Karna
if st.button("Generate Login Link"):
    if not client_id or not secret_key:
        st.error("Please enter both Client ID and Secret Key.")
    else:
        # Save credentials in session state securely
        st.session_state['client_id'] = client_id
        st.session_state['secret_key'] = secret_key
        
        fyers_auth_url = f"https://api-t1.fyers.in/api/v3/generate-authcode?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code&state=dashboard_login"
        
        st.markdown(f"### 👉 [Click Here to Login with Fyers]({fyers_auth_url})")
        st.warning("Login karne ke baad, is page par wapas aane ka wait karein.")

# STEP 2: Catch URL Parameters and Generate Token
# Jab Fyers login ke baad wapas bhejega, toh URL me 'auth_code' hoga
query_params = st.query_params

if "auth_code" in query_params:
    auth_code = query_params["auth_code"]
    st.success("✅ Auth Code Received from Fyers!")
    
    # Session state se ID aur Secret wapas nikalna
    if 'client_id' in st.session_state and 'secret_key' in st.session_state:
        c_id = st.session_state['client_id']
        s_key = st.session_state['secret_key']
        
        with st.spinner("Fetching Final Access Token..."):
            # Hash generation
            hash_str = f"{c_id}:{s_key}"
            app_id_hash = hashlib.sha256(hash_str.encode()).hexdigest()

            # API Call
            url = "https://api-t1.fyers.in/api/v3/validate-authcode"
            headers = {"Content-Type": "application/json"}
            payload = {
                "grant_type": "authorization_code",
                "appIdHash": app_id_hash,
                "code": auth_code
            }

            try:
                response = requests.post(url, headers=headers, json=payload)
                data = response.json()
                
                if data.get("s") == "ok":
                    st.balloons()
                    st.success("🎉 Success! Access Token Generated")
                    st.code(data["access_token"], language="text")
                else:
                    st.error(f"Token Error: {data.get('message')}")
            except Exception as e:
                st.error(f"System Error: {str(e)}")
    else:
        st.info("Pehle apni details daal kar login link generate karein.")
