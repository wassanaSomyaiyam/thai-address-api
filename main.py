from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def parse_address(text):
    zip_match = re.search(r'\d{5}', text)
    zipcode = zip_match.group() if zip_match else ""
    prov_match = re.search(r'(?:จ\.|จังหวัด)\s*([^\s\d,]+)', text)
    province = prov_match.group(1) if prov_match else ""
    return {
        "full_address": text,
        "province": province,
        "zipcode": zipcode,
        "status": "success"
    }

@app.route('/')
def home():
    return "Thai Address API is Running!"

@app.route('/parse', methods=['GET'])
def api_parse():
    address_input = request.args.get('text', '')
    if not address_input:
        return jsonify({"error": "Please provide 'text' parameter"}), 400
    return jsonify(parse_address(address_input))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
