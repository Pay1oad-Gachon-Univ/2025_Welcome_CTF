import os
import pymysql
from flask import Flask, request, redirect, render_template, g, abort

app = Flask(__name__)
app.secret_key = "testkey"

DB_HOST = os.getenv("DB_HOST", "db")
DB_USER = os.getenv("DB_USER", "ctfuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "ctfpass")
DB_NAME = os.getenv("DB_NAME", "ctfdb")

ADMIN_COOKIE_NAME = os.getenv("ADMIN_COOKIE_NAME", "ADMIN_TOKEN")
ADMIN_COOKIE_VALUE = os.getenv("ADMIN_COOKIE_VALUE", "SOME_SECRET")


def get_db():
    if not hasattr(g, 'db_conn'):
        g.db_conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            db=DB_NAME,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    return g.db_conn


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db_conn'):
        g.db_conn.close()


def is_admin():
    """특정 쿠키 값이 맞으면 관리자임."""
    cookie_val = request.cookies.get(ADMIN_COOKIE_NAME, None)
    return (cookie_val == ADMIN_COOKIE_VALUE)


@app.route("/")
def index():
    """메인 페이지: 전체 글 수와 열람된 글 수만 보여줌."""
    db = get_db()
    with db.cursor() as cur:
        cur.execute("SELECT COUNT(*) AS cnt FROM suggestions")
        total_count = cur.fetchone()['cnt']

        cur.execute("SELECT COUNT(*) AS cnt FROM suggestions WHERE viewed=1")
        viewed_count = cur.fetchone()['cnt']

    return render_template("index.html", total_count=total_count, viewed_count=viewed_count, is_admin=is_admin())


@app.route("/submit", methods=["GET", "POST"])
def submit():
    """익명 건의 글 작성."""
    if request.method == "POST":
        title = request.form.get("title", "")
        content = request.form.get("content", "")

        db = get_db()
        with db.cursor() as cur:
            cur.execute("INSERT INTO suggestions (title, content) VALUES (%s, %s)",
                        (title, content))
            db.commit()

        return redirect("/")

    return render_template("submit.html")


@app.route("/admin/list")
def admin_list():
    """관리자 전용: 전체 글 목록 조회."""
    if not is_admin():
        return abort(403, "관리자 전용 페이지입니다.")

    db = get_db()
    with db.cursor() as cur:
        cur.execute("SELECT * FROM suggestions WHERE viewed = 0 ORDER BY id DESC")
        rows = cur.fetchall()

    # list.html로 렌더링
    return render_template("list.html", suggestions=rows)


@app.route("/admin/suggestion/<int:sid>")
def admin_suggestion_detail(sid):
    if not is_admin():
        return abort(403, "관리자 전용 페이지입니다.")

    db = get_db()
    with db.cursor() as cur:
        cur.execute("SELECT * FROM suggestions WHERE id=%s", (sid,))
        row = cur.fetchone()

        if not row:
            return "존재하지 않는 글입니다."

        # 열람 완료 체크
        cur.execute("UPDATE suggestions SET viewed=1 WHERE id=%s", (sid,))
        db.commit()

    dict_var = {
        row['title']+"-meta": "image",  
        "alt": "Suggestion Image"
    }

    return render_template("detail.html", dict_var=dict_var, content=row['content'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
