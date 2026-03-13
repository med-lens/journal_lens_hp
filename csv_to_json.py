"""
csv_to_json.py
J_Medline_pseudoIF.csv を読み込んで、
GitHub Pages 用の data.json に変換するスクリプト。

使い方：
    python csv_to_json.py
    または
    uv run csv_to_json.py

出力：
    data.json（gitignore済み）
"""

import csv
import json

# ── 入出力ファイル名 ──────────────────────────────────
INPUT_CSV = "J_Medline_pseudoIF.csv"
OUTPUT_JSON = "data.json"


def parse_number(s):
    """
    文字列を float に変換する。
    空文字や変換できない値は None を返す。
    （HTML側では None → "-" と表示される）
    """
    if s is None or s.strip() == "":
        return None
    try:
        return float(s)
    except ValueError:
        return None


def main():
    data = []

    # CSV を UTF-8 で開いて1行ずつ読む
    # DictReader は1行目のヘッダを自動でキーにしてくれる
    with open(INPUT_CSV, encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        for row in reader:
            # ── UI で使う7列だけ抽出 ──
            # Index.html の masterData の並び：
            #   [0] JournalTitle      ジャーナルの正式名称
            #   [1] MedAbbr           PubMed 略称
            #   [2] MedIF             MedLine IF（数値、なければ None）
            #   [3] PseudoIF          推定 IF（数値、なければ None）
            #   [4] SJR Best Quartile SJR クォータイル（"Q1"〜"Q4" or ""）
            #   [5] H index           H 指数（数値、なければ None）
            #   [6] Areas             分野名（セミコロン区切り文字列）
            entry = [
                row["JournalTitle"],                   # 0
                row["MedAbbr"],                        # 1
                parse_number(row["MedIF"]),             # 2
                parse_number(row["PseudoIF"]),          # 3
                row["SJR Best Quartile"].strip(),      # 4  前後の空白を除去
                parse_number(row["H index"]),           # 5
                row["Areas"],                          # 6
            ]
            data.append(entry)

    # ── JSON として書き出す ─────────────────────────────
    # separators=(",", ":") でスペースを省略 → ファイルサイズを最小化
    # ensure_ascii=False で日本語をそのまま書く（\uXXXX にしない）
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))

    # 完了メッセージ
    size_kb = OUTPUT_JSON and __import__("os").path.getsize(OUTPUT_JSON) // 1024
    print(f"完了！ {len(data):,} 件を {OUTPUT_JSON} に出力したで（{size_kb:,} KB）")


if __name__ == "__main__":
    main()
