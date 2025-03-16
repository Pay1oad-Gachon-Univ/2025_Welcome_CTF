import os
from flask import Flask, render_template, request, redirect
import re
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

FLAG = os.getenv("FLAG", "CTF{default_flag}")

# User-Agent 기반 모바일 탐지
MOBILE_USER_AGENTS = re.compile(
    "android|iphone|ipad|ipod|blackberry|windows phone", re.IGNORECASE
)

@app.route('/')
def index():
    host = request.host.lower()
    user_agent = request.headers.get('User-Agent', '').lower()
    is_mobile = bool(MOBILE_USER_AGENTS.search(user_agent))
    
    if "m.opensearch.kr" in host and is_mobile:
        return render_template('mobile.html', flag=FLAG)
    elif is_mobile:
        return redirect('http://m.opensearch.kr')
    elif "m.opensearch.kr" in host:
        return redirect('http://www.opensearch.kr')
    return render_template('index.html')

@app.route('/sitemap.xml')
def sitemap():
    sitemap_content = """<?xml version=\"1.0\" encoding=\"UTF-8\"?>
    <urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">
        <url>
            <loc>http://www.opensearch.kr/</loc>
        </url>
        <url>
            <loc>http://m.opensearch.kr/</loc>
            <changefreq>weekly</changefreq>
        </url>
    </urlset>"""
    return sitemap_content, 200, {'Content-Type': 'application/xml'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)