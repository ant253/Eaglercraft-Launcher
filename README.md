# Eaglercraft Launcher

Eaglercraft Launcher is a modern and easy-to-use launcher for Eaglercraft, a Minecraft client that runs in the browser. This launcher has a sleek, rounded UI powered by Flask, making it simple to access various versions of Eaglercraft. The launcher currently supports multiple clients, including:

- **Resent Client**
- **Astra Client**
- **Eaglercraft 1.8.8**
- **Eaglercraft 1.5.2**
- **Eaglercraft Mobile**

The application provides a seamless experience for users to launch their favorite Eaglercraft versions directly from a browser.

## Features

- **Modern, Rounded UI**: A clean, modern, and visually appealing user interface powered by Flask.
- **Multiple Client Support**: Easily switch between different Eaglercraft versions (1.8.8, 1.5.2, Mobile, Resent, and Astra clients).
- **Self-Hosting**: You can host the launcher yourself on GitHub Codespaces or any server by following a few simple steps.
- **Easy Setup**: Simple installation steps to get started with minimal configuration.

## Demo

You can view the live demo of the self-hosted Eaglercraft Launcher here:  
[Eaglercraft Launcher - Demo](https://eaglermaths.uk.to/) (https://eaglermaths.uk.to/)

## Setup Instructions

### Self-Hosting via GitHub Codespaces

1. **Fork the Repository**:  
   Fork the repository to your GitHub account.

2. **Create a New Codespace**:  
   Navigate to your forked repository and click on the green `Code` button. Select `Open with Codespaces` and create a new codespace.

3. **Install Dependencies**:  
   Open the terminal in GitHub Codespaces and run the following command to install the required dependencies:
   ```bash
   pip install -r requirements.txt
3. **Run the Website**: 
   ```bash
   python app.py
