import os
import json
import requests
import zipfile
import shutil

# CTFd 서버 정보
CTFD_URL = "https://ctf.pay1oad.com"
API_TOKEN = "ctfd_357340bc9cbaa224da0c98af3be2a48b4e796192eb9edd58f0ca028d8acb0f3f"
HEADERS = {"Authorization": f"Token {API_TOKEN}", "Content-Type": "application/json"}

# 문제 디렉터리 경로
BASE_DIR = r"D:\git_temp\2025_Welcome_CTF"
CATEGORIES = ["digitalforensic", "misc", "pwnable", "reversing", "web"]

def create_challenge(title, description, points, flag, category):
    """CTFd에 문제를 생성하는 함수"""
    challenge_data = {
        "name": title,
        "category": category.upper(),
        "description": description,
        "value": points,
        "type": "standard",
        "state": "visible"
    }
    
    response = requests.post(f"{CTFD_URL}/api/v1/challenges", json=challenge_data, headers=HEADERS)
    
    if response.status_code == 200:
        challenge_id = response.json()["data"]["id"]
        print(f"[+] Created challenge {title} (ID: {challenge_id})")
        return challenge_id
    else:
        print(f"[-] Failed to create challenge {title}: {response.text}")
        return None

def add_flag(challenge_id, flag):
    """문제에 플래그 추가"""
    flag_data = {
        "challenge_id": challenge_id,
        "type": "static",
        "content": flag,
        "data": "case_insensitive"
    }
    
    response = requests.post(f"{CTFD_URL}/api/v1/flags", json=flag_data, headers=HEADERS)
    
    if response.status_code == 200:
        print(f"    [+] Added flag: {flag}")
    else:
        print(f"    [-] Failed to add flag: {response.text}")

def upload_file(challenge_id, file_path):
    """
    문제 파일 업로드 함수
    파일 업로드 시 POST 데이터에 'challenge'와 'type' 정보를 포함하여
    파일이 해당 챌린지에 자동 연결되도록 합니다.
    """
    url = f"{CTFD_URL}/api/v1/files"
    form_data = {
        'challenge': challenge_id,
        'type': 'challenge'
    }
    
    with open(file_path, "rb") as f:
        files = {"file": f}
        file_headers = HEADERS.copy()
        # 파일 업로드 시 Content-Type 헤더는 제거합니다.
        file_headers.pop("Content-Type", None)
        response = requests.post(url, headers=file_headers, files=files, data=form_data)
    
    if response.status_code == 200:
        print(f"    [+] Uploaded file: {file_path}")
    else:
        print(f"    [-] Failed to upload file: {response.text}")

def process_challenge(folder, category):
    """문제 폴더를 처리하고 CTFd에 업로드"""
    config_path = os.path.join(folder, "config.json")
    user_folder = os.path.join(folder, "user")

    if not os.path.exists(config_path):
        print(f"[-] No config.json in {folder}, skipping...")
        return

    # config.json 읽기
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    
    for challenge in config["challenges"]:
        title = challenge["title"]
        description = challenge["description"]
        points = challenge["point"]
        flag = challenge["flag"]
        port = challenge["port"]

        # 포트가 있을 경우 카테고리별 접속 정보 추가
        if port:
            if category in ["misc", "pwnable"]:
                description += f"<br><br>접속 정보: `nc dh.challenges.pay1oad.com {port}`"
            else:
                description += f"<br><br>접속 정보: [http://dh.challenges.pay1oad.com:{port}]"

        challenge_id = create_challenge(title, description, points, flag, category)
        
        if challenge_id:
            add_flag(challenge_id, flag)

            # user 폴더 내 파일이 실제로 있을 때만 압축 후 업로드 (.gitkeep만 있을 경우 생략)
            if os.path.exists(user_folder) and os.listdir(user_folder) != [".gitkeep"]:
                zip_path = os.path.join(folder, "user.zip")
                shutil.make_archive(os.path.splitext(zip_path)[0], 'zip', user_folder)
                upload_file(challenge_id, zip_path)
                os.remove(zip_path)  # 압축 파일 삭제하여 정리



def main():
    """모든 문제를 찾아 업로드"""
    for category in CATEGORIES:
        category_path = os.path.join(BASE_DIR, category)
        if os.path.exists(category_path):
            for challenge_folder in os.listdir(category_path):
                challenge_path = os.path.join(category_path, challenge_folder)
                if os.path.isdir(challenge_path):
                    process_challenge(challenge_path, category)

if __name__ == "__main__":
    main()
