from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>NABİ HACKED</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                background: #0a0a0a;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                font-family: 'Courier New', monospace;
                overflow: hidden;
            }
            .glitch-box {
                text-align: center;
                border: 3px solid #00ff41;
                padding: 60px 80px;
                background: rgba(0, 255, 65, 0.05);
                box-shadow: 0 0 50px rgba(0, 255, 65, 0.3), inset 0 0 50px rgba(0, 255, 65, 0.1);
                animation: flicker 3s infinite;
                position: relative;
            }
            .glitch-box::before {
                content: '';
                position: absolute;
                top: -5px; left: -5px; right: -5px; bottom: -5px;
                border: 2px solid #00ff41;
                animation: borderPulse 1.5s infinite;
            }
            h1 {
                font-size: 72px;
                color: #00ff41;
                text-shadow: 0 0 30px #00ff41, 0 0 60px #00ff41;
                letter-spacing: 8px;
                animation: glitch 2s infinite;
            }
            p {
                font-size: 28px;
                color: #00ff41;
                margin-top: 30px;
                text-shadow: 0 0 20px #00ff41;
                animation: glitch 2.5s infinite reverse;
                letter-spacing: 3px;
            }
            .cursor {
                display: inline-block;
                width: 15px; height: 30px;
                background: #00ff41;
                animation: blink 0.8s infinite;
                margin-left: 5px;
                vertical-align: middle;
            }
            @keyframes glitch {
                0% { transform: skew(0deg); }
                20% { transform: skew(2deg); opacity: 0.9; }
                40% { transform: skew(-2deg); opacity: 1; }
                60% { transform: skew(1deg); opacity: 0.8; }
                80% { transform: skew(-1deg); }
                100% { transform: skew(0deg); }
            }
            @keyframes flicker {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.95; }
            }
            @keyframes borderPulse {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.3; }
            }
            @keyframes blink {
                0%, 100% { opacity: 1; }
                50% { opacity: 0; }
            }
            .matrix {
                position: fixed;
                top: 0; left: 0;
                width: 100%; height: 100%;
                pointer-events: none;
                background: repeating-linear-gradient(0deg, 
                    rgba(0,255,65,0.02) 0px, 
                    rgba(0,255,65,0.02) 2px, 
                    transparent 2px, 
                    transparent 6px);
            }
            .subtext {
                color: #00ff41;
                font-size: 14px;
                margin-top: 40px;
                opacity: 0.5;
                letter-spacing: 5px;
            }
        </style>
    </head>
    <body>
        <div class="matrix"></div>
        <div class="glitch-box">
            <h1>NABİ HACKED</h1>
            <p>Rinex ananı bacını sikim<br>nabi babandır<span class="cursor"></span></p>
            <div class="subtext">● SYSTEM COMPROMISED ●</div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
