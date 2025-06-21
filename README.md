# StegoSafeCLI 🕵️‍♂️

A beginner-friendly command-line tool that lets you **hide secret messages inside images** and **retrieve them later**. Perfect for learning about steganography and cybersecurity!

## What is Steganography?
Steganography is the art of hiding information in plain sight. This tool hides your secret messages inside image files (PNG/BMP) without anyone knowing the message is there!

## ✨ Features
- 📸 Hide secret messages inside PNG/BMP images
- 🔐 Optional AES encryption for extra security (128-bit or 256-bit)
- 💻 Simple command-line interface
- 📝 Automatically logs all operations
- 🎓 Perfect for cybersecurity students and enthusiasts

## 🚀 Quick Start Guide

### Step 1: Install Python
Make sure you have Python 3.7 or newer installed on your computer.
- Download from: https://www.python.org/downloads/
- During installation, check "Add Python to PATH"

### Step 2: Download the Code
1. Download or clone this project to your computer
2. Open Command Prompt (Windows) or Terminal (Mac/Linux)
3. Navigate to the project folder:
   ```
   cd path/to/StegoSafe
   ```

### Step 3: Install Required Libraries
Run this command to install the needed libraries:
```
pip install -r requirements.txt
```

## 📋 How to Use

### 🔒 Hide a Secret Message in an Image

**Basic hiding (no encryption):**
```
python main.py hide -i "path/to/your/image.png" -o "path/to/output.png" -m "Your secret message"
```

**Hide with encryption (more secure):**
```
python main.py hide -i "path/to/your/image.png" -o "path/to/output.png" -m "Your secret message" --encrypt --key "yourpassword"
```

**Hide a message from a text file:**
```
python main.py hide -i "path/to/your/image.png" -o "path/to/output.png" -f "path/to/message.txt" --encrypt --key "yourpassword"
```

### 🔓 Reveal a Hidden Message from an Image

**Basic reveal (no decryption):**
```
python main.py reveal -i "path/to/stego-image.png"
```

**Reveal with decryption:**
```
python main.py reveal -i "path/to/stego-image.png" --decrypt --key "yourpassword"
```

## 💡 Example Walkthrough

Let's say you have an image called `vacation.png` on your desktop:

1. **Hide a secret message:**
   ```
   python main.py hide -i "C:\Users\YourName\Desktop\vacation.png" -o "C:\Users\YourName\Desktop\secret_vacation.png" -m "The treasure is buried under the old oak tree!"
   ```

2. **Share the `secret_vacation.png` image** - it looks exactly like the original!

3. **Later, reveal the message:**
   ```
   python main.py reveal -i "C:\Users\YourName\Desktop\secret_vacation.png"
   ```

## 🛠️ Command Arguments Explained

### For Hiding Messages:
- `-i` or `--input`: Path to your original image file
- `-o` or `--output`: Where to save the image with hidden message
- `-m` or `--message`: The secret message to hide
- `-f` or `--file`: Text file containing the message to hide
- `--encrypt`: Add this to encrypt your message (optional)
- `--key`: Password for encryption (required if using --encrypt)

### For Revealing Messages:
- `-i` or `--input`: Path to the image with hidden message
- `--decrypt`: Add this if the message was encrypted
- `--key`: Password for decryption (required if using --decrypt)

## 📝 Important Notes
- ✅ Supported formats: PNG and BMP images only
- 🔍 The tool automatically adds '####' as a message delimiter
- 📊 All operations are logged in `stegosafe.log`
- 🖼️ The output image looks identical to the original
- 📏 Very long messages might not fit in small images

## 🎯 Tips for Beginners
1. Start with simple messages without encryption
2. Use PNG files for best results
3. Keep your encryption passwords safe!
4. The larger the image, the longer the message you can hide
5. Check the log file to see your operation history

## 🔧 Troubleshooting
- **"Command not found"**: Make sure Python is installed and added to PATH
- **"pip not found"**: Install pip or use `python -m pip` instead
- **"Image too small"**: Use a larger image or shorter message
- **"Wrong password"**: Double-check your decryption key

---
**Developed by Ayaan❤️**
