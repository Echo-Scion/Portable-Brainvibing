# Micro-Canons (Domain Cheat-Sheets)

## Konsep The Knowledge Shim
Model Premium (Opus/Sonnet) memiliki *world-knowledge* yang luas dan *pre-trained data* dari jutaan dokumentasi framework. Namun, Model Budget (Flash/Haiku) sering halusinasi jika berhadapan dengan API *framework* modern (misal Next.js App Router terbaru, Flutter 3.24, dll).

**Micro-Canons** adalah file "Cheat Sheet" (*Maksimal 30-50 baris*) yang dirancang khusus untuk mem-by-pass kelemahan Model Kecil. File ini adalah pengganti RAG (Retrieval-Augmented Generation) yang berat, menyuntikkan *world-knowledge* esensial ke dalam file teks statis yang super ringan.

## Aturan Pemakaian (Untuk Budget Model)
1. Jika eksekusi tugas meliputi teknologi baru/spesifik (misal: Flutter, FastAPI).
2. Agen **WAJIB** membaca file `canons/micro/<framework>.md` terkait (jika ada) sebelum memulai *planning*.
3. Pengetahuan dari Micro-Canon menjadi Hukum Tertinggi *(Override)* atas pengetahuan bawaan LLM yang mungkin sudah basi *(cutoff data)*.

## Aturan Pembuatan Micro-Canon
- Dilarang membuat Micro-Canon melebihi 50 baris.
- Harus berbentuk poin telegrafis (Format: DO / DONT / SYNTAX).
- Hindari kalimat prosa/narasi. Gunakan instruksi deterministik.