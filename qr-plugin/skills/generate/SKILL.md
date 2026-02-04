---
name: generate
description: Generate QR codes from text, URLs, or data.
---

# QR Code Generator Skill

Create QR codes from text, URLs, or data.

## Methods

### Option 1: Python (most cross-platform)
```bash
# Install qrcode library
pip install qrcode[pil]

# Generate
python -c "import qrcode; qrcode.make('{data}').save('qr.png')"
```

### Option 2: qrencode CLI (Linux/Mac)
```bash
# Install
brew install qrencode  # Mac
apt install qrencode   # Linux

# Generate PNG
qrencode -o qr.png "{data}"

# Generate ASCII (terminal)
qrencode -t ASCII "{data}"
```

### Option 3: PowerShell with online API
```powershell
Invoke-WebRequest "https://api.qrserver.com/v1/create-qr-code/?size=200x200&data={data}" -OutFile qr.png
```

## Output Format
```
## QR Code Generated

Data: {input}
Size: 200x200 pixels
File: qr.png

[Preview if ASCII]
```

## Example Usage
- `/qr:generate "https://example.com"`
- `/qr:generate "Hello World" --output qr.png`
- `/qr:generate "WIFI:T:WPA;S:MyNetwork;P:password123;;"` (WiFi)
