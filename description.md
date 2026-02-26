# Online Sales Data Pipeline & Visualization Project

## Repository Outline

Repository ini berisi file–file yang digunakan untuk membangun end-to-end data pipeline serta visualisasi data penjualan online.

```
1. description.md                                 - Dokumentasi dan penjelasan project
2. P2M3_Nur_Cahyo_Widodo_data_raw.csv             - Dataset mentah (raw data)
3. P2M3_Nur_Cahyo_Widodo_data_clean.csv           - Dataset hasil data cleaning
4. P2M3_Nur_Cahyo_Widodo_ddl.txt                  - DDL & DML untuk PostgreSQL
5. P2M3_Nur_Cahyo_Widodo_DAG.py                   - Script DAG Apache Airflow
6. P2M3_Nur_Cahyo_Widodo_DAG_graph.jpg            - Screenshot graph DAG
7. P2M3_Nur_Cahyo_Widodo_GX.ipynb                 - Notebook validasi data (Great Expectations)
8. P2M3_Nur_Cahyo_Widodo_conceptual.txt           - Jawaban soal conceptual
9. images/                                        - Folder berisi screenshot dashboard & insight
```

---

## Problem Background

Perusahaan dengan sistem penjualan online menghasilkan data transaksi dalam jumlah besar setiap harinya. Data tersebut tidak dapat langsung digunakan untuk analisis apabila masih berupa data mentah, tidak tervalidasi, dan belum terstruktur dengan baik. Selain itu, proses pengolahan data yang dilakukan secara manual berpotensi menimbulkan kesalahan serta tidak efisien.

Oleh karena itu, diperlukan sebuah sistem yang mampu mengotomatisasi proses pengambilan data, pembersihan data, validasi kualitas data, hingga penyajian data dalam bentuk visualisasi yang mudah dipahami. Project ini dibuat untuk menjawab kebutuhan tersebut dengan membangun pipeline data terintegrasi dan dashboard visualisasi guna mendukung proses Exploratory Data Analysis (EDA).

---

## Project Output

Output dari project ini adalah:

* Dataset bersih (clean data) yang telah melalui proses data cleaning dan validasi
* Pipeline data otomatis menggunakan Airflow
* Dashboard visualisasi interaktif menggunakan Kibana
* Insight eksploratif dari data penjualan online

---

## Data

Dataset yang digunakan merupakan dataset online sales yang diperoleh dari platform Kaggle dengan detail sebagai berikut:

Sumber dataset: https://www.kaggle.com/datasets/yusufdelikkaya/online-sales-dataset

* Terdiri dari lebih dari 10 kolom
* Memiliki kombinasi data kategorikal dan numerikal
* Berisi informasi transaksi seperti kategori produk, negara, channel penjualan, quantity, metode pembayaran, dan pengiriman
* Data diproses untuk menghilangkan duplikasi, menormalkan nama kolom, serta menangani missing values sebelum digunakan untuk analisis

---

## Method

Metode yang digunakan dalam project ini adalah **Exploratory Data Analysis (EDA)** dengan pendekatan data pipeline terotomatisasi. Tahapan utama meliputi:

* Extract data dari PostgreSQL
* Transform data melalui proses data cleaning
* Validate data menggunakan Great Expectations
* Load data ke Elasticsearch
* Visualisasi data menggunakan Kibana untuk menggali insight bisnis

---

## Stacks

Berikut adalah teknologi dan tools yang digunakan dalam project ini:

* **Bahasa Pemrograman**: Python
* **Database**: PostgreSQL
* **Workflow Orchestration**: Apache Airflow
* **Data Validation**: Great Expectations
* **NoSQL Database**: Elasticsearch
* **Data Visualization**: Kibana
* **Environment**: Docker

---

## Reference

* Dataset sumber: Online Sales Dataset (Kaggle)
https://www.kaggle.com/datasets/yusufdelikkaya/online-sales-dataset
* Dokumentasi Apache Airflow: [https://airflow.apache.org/](https://airflow.apache.org/)
* Dokumentasi Great Expectations: [https://greatexpectations.io/](https://greatexpectations.io/)
* Dokumentasi Elasticsearch & Kibana: [https://www.elastic.co/](https://www.elastic.co/)

---

Project ini dibuat sebagai bagian dari **Milestone 3 Hacktiv8 Data Science Fulltime Program (Phase 2)** dan bertujuan untuk menunjukkan pemahaman mengenai data pipeline, data validation, NoSQL, serta visualisasi data.
