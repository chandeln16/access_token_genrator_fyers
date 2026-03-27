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

## 🛠️ Getting Started

Follow these simple steps to run the tool on your local machine:

1. **Open the Project:** Open the project folder in **VS Code**.
2. **Launch Live Server:** Right-click on `accessToken.html` and select **"Open with Live Server"** (Ensure your port matches your Fyers Redirect URI).
3. **Enter Details:** Input your `Client ID`, `Secret Key`, and the matching `Redirect URI` from your Fyers Dashboard.
4. **Authorize:** Click the **"Login with Fyers"** button and follow the official Fyers login prompts.

---

## 🔒 Security & Privacy

Security is a top priority when handling financial API credentials:

* **Local Processing Only:** This tool **does not send** your API Secret or Client ID to any external server or database.
* **Client-Side Execution:** All hashing and token exchange logic happens 100% locally within your browser.
* **Safe Storage:** Your credentials are saved in your browser's `localStorage` for convenience (so you don't have to type them every day) and **never leave your machine**.

---


## 🤝 Contributing

Contributions, issues, and feature requests are welcome! 
If you have ideas to improve this tool, feel free to:
1. Fork the project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Open a **Pull Request**.

Check out the [Issues Page](https://github.com/your-username/repo-name/issues) to report bugs.

---

### Developed with ❤️ by [Narendra]
*Passionate about **Financial Data Analytics** & **Web Automation**.* 🚀
