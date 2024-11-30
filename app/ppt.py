from ppt import Presentation
from ppt.util import Inches

# Initialize presentation
ppt = Presentation()

# 1. Slide 1 - Title Slide
slide = ppt.slides.add_slide(ppt.slide_layouts[0])
title = slide.shapes.title
subtitle = slide.placeholders[1]
title.text = "Stroke Prediction System"
subtitle.text = "Tugas Besar KS-RPL - Desember 2024"

# 2. Slide 2 - Pendahuluan
slide = ppt.slides.add_slide(ppt.slide_layouts[1])
title = slide.shapes.title
title.text = "Pendahuluan"
content = slide.placeholders[1]
content.text = (
    "• Latar Belakang:\n"
    "Stroke adalah salah satu penyebab utama kematian di dunia. Prediksi dini "
    "membantu pencegahan risiko.\n\n"
    "• Tujuan:\n"
    "Mengembangkan sistem prediksi stroke berbasis machine learning."
)

# 3. Slide 3 - Dataset
slide = ppt.slides.add_slide(ppt.slide_layouts[1])
title = slide.shapes.title
title.text = "Dataset"
content = slide.placeholders[1]
content.text = (
    "• Dataset diambil dari Kaggle:\n"
    "https://www.kaggle.com/fedesoriano/stroke-prediction-dataset\n\n"
    "• Deskripsi:\n"
    "10 atribut (usia, jenis kelamin, BMI, dll.) dan 1 target (stroke).\n\n"
    "• Total Data:\n"
    "5110 data pasien."
)

# 4. Slide 4 - Proses Pengerjaan
slide = ppt.slides.add_slide(ppt.slide_layouts[1])
title = slide.shapes.title
title.text = "Proses Pengerjaan"
content = slide.placeholders[1]
content.text = (
    "• Langkah-langkah:\n"
    "1. Mengunduh dataset dari Kaggle.\n"
    "2. Melakukan eksplorasi dan preprocessing data.\n"
    "3. Melatih model machine learning.\n"
    "4. Membuat aplikasi prediksi menggunakan Streamlit.\n"
    "5. Melakukan deploy aplikasi."
)

# 5. Slide 5 - Modifikasi Kode
slide = ppt.slides.add_slide(ppt.slide_layouts[1])
title = slide.shapes.title
title.text = "Modifikasi Kode"
content = slide.placeholders[1]
content.text = (
    "• Penyesuaian preprocessing data:\n"
    "- Mengimputasi nilai BMI yang kosong.\n"
    "- Menambahkan encoding pada variabel kategorikal.\n\n"
    "• Pemilihan model:\n"
    "- Awalnya menggunakan Logistic Regression.\n"
    "- Diganti dengan Random Forest untuk akurasi yang lebih tinggi."
)

# 6. Slide 6 - Hasil dan Analisis
slide = ppt.slides.add_slide(ppt.slide_layouts[1])
title = slide.shapes.title
title.text = "Hasil dan Analisis"
content = slide.placeholders[1]
content.text = (
    "• Akurasi model:\n"
    "Random Forest menghasilkan akurasi 85% pada data validasi.\n\n"
    "• Screenshot aplikasi:\n"
    "Lihat hasil prediksi pada aplikasi Streamlit."
)

# 7. Slide 7 - Kesimpulan
slide = ppt.slides.add_slide(ppt.slide_layouts[1])
title = slide.shapes.title
title.text = "Kesimpulan"
content = slide.placeholders[1]
content.text = (
    "• Sistem prediksi stroke berhasil dikembangkan.\n"
    "• Dataset Kaggle dimanfaatkan untuk membangun model yang cukup akurat.\n"
    "• Aplikasi prediksi berbasis web mempermudah penggunaan oleh user.\n"
    "• Deployment Streamlit Cloud memungkinkan aksesibilitas luas."
)

# Save the presentation
ppt.save("/mnt/data/Tugas_Besar_KS_RPL_Stroke_Prediction.pptx")
"/mnt/data/Tugas_Besar_KS_RPL_Stroke_Prediction.pptx dibuat!"
