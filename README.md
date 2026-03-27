# ⚡ Fyers API v3 Auto-Token Generator (Web-Based)

A professional, client-side utility tool designed to automate the **OAuth 2.0 authentication flow** for the Fyers API v3. This tool eliminates the manual hassle of copying auth codes from URLs and provides a seamless way to generate daily Access Tokens for algorithmic trading.

---

## 🚀 Overview
Most traders struggle with the daily manual process of generating access tokens. This project provides a clean, interactive **HTML5/JavaScript** interface that handles the entire handshake between your browser and Fyers servers, ensuring you get your `access_token` in seconds.

### ✨ Key Features
- **Zero Backend Required:** Runs entirely in the browser (Client-side).
- **Automated OAuth Flow:** Redirects to Fyers login and captures the `auth_code` automatically on return.
- **SHA-256 Hashing:** Built-in logic to generate the `appIdHash` as per Fyers' mandatory security protocol.
- **Persistence:** Uses `localStorage` to remember your Client ID and Secret Key (stored locally on your machine only).
- **One-Click Copy:** Integrated clipboard support to copy the final token instantly.
- **Modern UI:** Dark/Light compatible, responsive design for a premium feel.

---

## 🛠️ Technical Stack
- **Frontend:** HTML5, CSS3 (Modern UI).
- **Logic:** Vanilla JavaScript (ES6+).
- **Security:** Web Crypto API (for SHA-256 hashing).
- **Protocol:** OAuth 2.0 Authorization Code Grant.

---

## 📖 How to Setup & Use

### 1. Fyers API Dashboard Configuration
Before using this tool, ensure your app settings on [Fyers API Dashboard](https://myapi.fyers.in/) are:
- **Redirect URI:** `http://127.0.0.1:5500/accessToken.html` (If using VS Code Live Server).
- **App Type:** Web / Personal.

### 2. Running the Tool
1. Clone this repository:
   ```bash
   git clone [https://github.com/your-username/fyers-token-generator.git](https://github.com/your-username/fyers-token-generator.git)
