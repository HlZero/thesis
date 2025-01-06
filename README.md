# IoT: Wi-Fi Sensing and Diagnostic for Customer Premises Equipment using Transfer Learning and USP
## Overview
This paper presents a lightweight deep transfer learning based human activity detection and diagnostic recognition approach using WiFi sensing. In our method, the amplitude matrix of each WiFi Channel State Information (CSI) stream is reorganized as an image. Therefore, WiFi based human activity recognition is transformed into an image classification task. Leveraging the high potential of Convolutional Neural Networks in image processing, a CNN-based transfer learning model is employed to reduce the need for extensive network training and to extract features more suited to the CSI matrix. The proposed methods are trained and tested on a public CSI dataset, demonstrating an accuracy of approximately 94% to 99% across six activities. This performance outperforms the state-of-the-art in Human Activity Recognition for Customer Premises Equipment (CEP).

We integrate the transfer learning model that demonstrated the best performance into CPE and deploy it on a Raspberry Pi 4 for local detection applications. The User Services Platform (USP) serves as the standard for remote manipulation of connected CPE. Utilizing the USP protocol, end-users can independently manage and monitor their CPE through one or more Controllers.
## General Pipeline
### Overall framework of transfer learning model building:
<img width="300" alt="截屏2025-01-06 下午5 23 38" src="https://github.com/user-attachments/assets/20eb5f02-1ab2-44d5-9ee3-b34b1c42c490" />

### CSI images of each class (Classes a and b are merged to class Down, classes c and d are merged to class Fall, classes e and f are merged to class Move):
<img width="297" alt="截屏2025-01-06 下午5 22 17" src="https://github.com/user-attachments/assets/89261f17-5719-45d3-92fe-60f60fa3c3a3" />

## Experimental Environment (Employ Nexmon CSI Tool and collect CSI data for seven daily human activities, including walk, run, fall, lie down, sit down, stand up, and bend):
<img width="233" alt="截屏2025-01-06 下午5 21 43" src="https://github.com/user-attachments/assets/4bc1e2c2-4721-453f-a2a2-514c8b14af91" />

## Proposed Methodologies & Evaluation
### Comparison of the original VGG16 and proposed VGG16-based transfer learning model (model I):
<img width="459" alt="截屏2025-01-06 下午5 31 01" src="https://github.com/user-attachments/assets/7995beb6-2f05-4f13-8a2f-fb5f92879edd" />

### Comparison of the original MobileNetV3-Large and proposed MobileNetV3-Large based transfer learning model (model II):
<img width="452" alt="截屏2025-01-06 下午5 31 23" src="https://github.com/user-attachments/assets/2ad0b01a-7167-4d14-a875-e8a2e68b8bb7" />

### Hyperparameters used for the proposed model I and II: 
<img width="418" alt="截屏2025-01-06 下午5 01 39" src="https://github.com/user-attachments/assets/6ec7ecd2-7f45-42ae-b685-7389635d1958" />

### Hyperparameters used for the proposed model III -- model II with Fine-Tuning: 
<img width="421" alt="截屏2025-01-06 下午5 02 07" src="https://github.com/user-attachments/assets/8fb00cc5-4f05-4418-90a6-378ad58909b9" />

### Model Evaluation (Accuracy and Loss are refer to validation accuracy and validation loss. Bach size are the same, result in same amount of data in one epoch):
<img width="668" alt="截屏2025-01-06 下午5 03 38" src="https://github.com/user-attachments/assets/f93310b9-557e-4d42-83c8-e227f26f6430" />

## Deployment of Machine Learning Models in Local Environments
### USP framework:
<img width="292" alt="截屏2025-01-06 下午5 23 05" src="https://github.com/user-attachments/assets/80c6d60e-78a6-433a-95d9-1d03bff40446" />

### Notifications reach Controller as User Services Platform Notify messages like this:
<img width="482" alt="截屏2025-01-06 下午5 20 46" src="https://github.com/user-attachments/assets/4e46d481-072e-4003-82b3-59003c963029" />

### Model prediction result:
{"action": "move","consumed time":"0.611123"}

This message informs the Controller a person is moving within the detection range, with the model execution time being 0.611123 seconds.
