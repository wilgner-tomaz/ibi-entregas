from flask import Flask, request, redirect, send_file
import qrcode

app = Flask(__name__)

ANDROID_LINK = "https://play.google.com/store/apps/details?id=br.com.client.ibientregas"
IOS_LINK = "https://apps.apple.com/br/app/ibi-entregas/id6743942785"

FIXED_URL = "https://ibi-entregas.onrender.com/app"


@app.route("/")
def home():
    return send_file("qrcode_fixo.png", mimetype="image/png")


@app.route("/app")
def smart_redirect():
    ua = request.headers.get("User-Agent", "").lower()

    if "android" in ua:
        return redirect(ANDROID_LINK, code=302)

    if any(x in ua for x in ["iphone", "ipad", "ipod"]):
        return redirect(IOS_LINK, code=302)

    return "<h2>Abra este QR Code no celular 📱</h2>"


def generate_static_qrcode():
    img = qrcode.make(FIXED_URL)
    img.save("qrcode_fixo.png")
    print("QR Code gerado: qrcode_fixo.png")


if __name__ == "__main__":
    generate_static_qrcode()
    app.run(host="0.0.0.0", port=5000)
