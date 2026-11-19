# 大学受験・日本史 日中関係史年表（縄文〜平成）

日本史の大学受験に向けた **137項目** の日中関係史インタラクティブ年表です。元の `rekishi` プロジェクトとは独立した、このフォルダ内だけで動作する教材です。

## 使い方
- `index.html` をブラウザで開く（依存ライブラリ・外部API不要）。
- 時代・テーマ・重要度による絞り込み、キーワード検索、暗記モード、保存、CSVダウンロードを利用できます。
- GitHub Pages がこのリポジトリの `main` ブランチのルートを公開している場合、`/rekishi/japan-china-history/` でアクセスできます。

## 編集・再生成
- `events.json`：137件の元データ。出来事・年代・要点などはこちらで修正してください。
- `template.html`：レイアウトと機能。
- `build.py`：両ファイルから `index.html` と `timeline.csv` を再生成します。
- `timeline.csv`：Excel/Googleスプレッドシート等で閲覧できます。

```bash
python3 build.py
```

## 記述上の注意
- 縄文・弥生期の年代・文化の伝播経路には研究上の幅があります。近代的な国家間外交とは区別しています。
- 日中関係には中国各王朝に加え、朝鮮半島・琉球・台湾を介する交流や東アジア情勢も含みます。
- 入試学習用に編集した資料です。実際の授業や入試問題で扱う際は教科書・原史料とも照合してください。

## 参考資料・調査先
- [国立歴史民俗博物館](https://www.rekihaku.ac.jp/)
- [国立公文書館](https://www.archives.go.jp/)
- [アジア歴史資料センター](https://www.jacar.go.jp/)
- [日中関係資料集](https://worldjpn.net/documents/indices/JPCH/)
- [在中国日本国大使館 日中関係年表](https://www.cn.emb-japan.go.jp/itpr_ja/nenpyo.html)
