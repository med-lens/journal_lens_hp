# Journal Lens

医学雑誌の格（IF・SJR・H index）をスマホでサクッと調べられる検索サイトです。

**[→ サイトを開く](https://med-lens.github.io/journal_lens_hp/)**

---

## 機能

- **全文検索**：雑誌名・略称で AND 検索（例: `plastic surgery`）
- **分野フィルター**：Medicine など分野ボタンで絞り込み
- **MedIF 降順**：検索結果は MedIF の高い順に表示
- **スマホ対応**：モバイルファーストのレイアウト

## 表示データ

| 項目 | 説明 |
|------|------|
| MedIF | PubMed 掲載誌の Impact Factor |
| Est.IF | SJR データから推定した IF |
| SJR | Scimago Journal Rank のクォータイル（Q1〜Q4） |
| H index | H 指数 |

## データソース

- 雑誌リスト・MedIF：[NLM Catalog](https://www.ncbi.nlm.nih.gov/nlmcatalog)
- SJR・H index・引用数：[Scimago Journal & Country Rank](https://www.scimagojr.com/journalrank.php)（非商用利用）

## 技術構成

- フロントエンド：HTML / CSS / JavaScript（フレームワークなし）
- データ：CSV → JSON に変換してブラウザで全件検索
- ホスティング：GitHub Pages
