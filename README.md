# Automated Detection of Diabetic Retinopathy 🩺👀

![image](https://github.com/user-attachments/assets/9d772125-8b4e-486f-a2f3-817bdb0b085c)

## What's Inside? 📦
- **Data Acquisition**: Collecting eye pics from Kaggle's Diabetic Retinopathy dataset. 📸
- **Data Preprocessing**: Teaching the images some good manners by resizing, normalizing, and augmenting them. 🎨
- **Model Development**: Crafting a CNN that can spot diabetic retinopathy like a pro ophthalmologist. 🧠
- **Model Evaluation**: Making sure our model is not just good, but awesome! 📊
- **Web Interface**: Giving users an interface to upload their images and get instant analysis. 🌐

## How to Use? 🚀

1. **Get the Data**:
   ```sh
   kaggle competitions download -c diabetic-retinopathy-detection
   unzip diabetic-retinopathy-detection.zip -d diabetic_retinopathy_dataset

1. **Preprocess like a Pro**:
   ```sh
   python preprocess_images.py

1. **Train the Model**:
   ```sh
   python train_model.py

1. **Run the Web App**:
   ```sh
   python app.py

## My Results 🔬

![image](https://github.com/user-attachments/assets/92702d36-8bef-4a61-8cc5-0ce31b8ca596)

![image](https://github.com/user-attachments/assets/50a76063-4462-4ee2-94b9-e7e9e2f329be)

![image](https://github.com/user-attachments/assets/0a1a9842-a927-4cb0-bd82-221ffc01a946)

![image](https://github.com/user-attachments/assets/caf54963-8980-4c1b-8fd5-e856d3d96e9e)

![image](https://github.com/user-attachments/assets/69d59665-0768-407a-968e-1424e33c1683)

![image](https://github.com/user-attachments/assets/bd73dfbe-6def-42f2-bd62-fdf113b4c26a)

![image](https://github.com/user-attachments/assets/bb2d9003-967a-4650-b0de-a47baa64f5cf)

## Acknowledgements 🙏
Big thanks to all the datasets and research papers that made this project possible, especially to the visionaries at Kaggle and the authors of "Development and Validation of a Deep Learning Algorithm for Detection of Diabetic Retinopathy in Retinal Fundus Photographs." 🎉

Gulshan V, Peng L, Coram M, Stumpe MC, Wu D, Narayanaswamy A, Venugopalan S, Widner K, Madams T, Cuadros J, Kim R, Raman R, Nelson PC, Mega JL, Webster DR. Development and Validation of a Deep Learning Algorithm for Detection of Diabetic Retinopathy in Retinal Fundus Photographs. JAMA. 2016 Dec 13;316(22):2402-2410. doi: 10.1001/jama.2016.17216. PMID: 27898976.

## Disclaimer 🛑
This project is for educational purposes only. Do not use it to make real-life medical decisions. 

Consult a healthcare professional for serious matters. Stay healthy and keep your eyes in check! 👀❤️
