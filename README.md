# face_recognition_facenet
Just for homework

我該學程式，這個是別人寫的程式碼，我只負責每一種功能，都拿來抄拿來用。

實作步驟: 

一. 在D槽開一個資料夾，叫facenet
二. 我們分別有以下資料夾與內容

1. aligned_img
   1.1 你的資料夾名稱(可以多個)
      1.1.1 你的照片(可以多張)

2. train_img
   2.1 你的資料夾名稱(可以多個)
      2.1.1 你的照片(可以多張)

3. class 
   3.1 classifier.pkl

4. npy
   4.1 det1.npy
   4.2 det2.npy
   4.3 det3.npy

5. model 
   5.1 120180402-114759.qb
   P.S 因為檔案過大，無法放上github，連結如下
https://www.mediafire.com/file/j1m8sz2uqaokgk3/20180402-114759.zip/file

6. Facenet_Tensorflow-main (主要程式都在裡面)
   6.1 preprocess.py
   6.2 data_preprocess.py
   6.3 detect_face.py
   6.4 Facenet.py
   6.5 Train_main.py
   6.6 Recognition.py
   6.7 Autocontrol.py
   6.8 Savefiles.py
   6.9 LineMessage.py

注意檔案放置的位置，放錯就會出錯。

建置環境 : 
1. python = 3.6.8
2. tensorflow = 2.6.2 (最新版本)
注意:如果裝有Keras會造成與tensorflow版本衝突。
3. 安裝相關套件 如下
   3.1 opencv-contrib-python
   3.2 imageio
   3.3 tensorflow
   3.4 scipy
   3.5 scikit-learn
注意:如果缺少套件報錯，請自行pip install相關模組。

使用方式:

一. 人臉辨識
1. 運行 Data_process.py
2. 運行 Train_main.py
3. 運行 Recognition.py

二. 自動點擊
1. 運行 Autocontrol.py

三. 儲存
1. 運行 Savefiles.py

四. Line Notify
1. LineMessage.py
