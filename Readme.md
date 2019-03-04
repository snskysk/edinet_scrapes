##内容１　⇒　あらかじめCSV形式でリスト化された企業の名前を基に、その企業の有価証券報告書が掲載されているURLを会社情報とともにCSV形式で排出

##内容２　⇒　回収したURL情報を基に、PDFファイルを自動ダウンロードする（二段階にすることで、NULL値などの対策をしやすくした）

##起動コマンド1　⇒　python edinet_scrape.py

##起動コマンド2　⇒　python pdf_download.py

--1

--※pythonの部分は環境で変化

--pyfile内で保存するファイル名の指定が必要  output_filename="hogehoge.csv"

--defalt → "yu-kasho-ken.csv"

--2

--pyfile内で読み込むファイル名の指定が必要  filename="hogehoge.csv"

