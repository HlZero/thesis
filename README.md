# IoT: Wi-Fi Sensing and Diagnostic for Customer Premises Equipment using Transfer Learning and USP
This paper presents a lightweight deep transfer learning based human activity detection and diagnostic recognition approach using WiFi sensing. In our method, the amplitude matrix of each WiFi Channel State Information (CSI) stream is reorganized as an image. Therefore, WiFi based human activity recognition is transformed into an image classification task. Leveraging the high potential of Convolutional Neural Networks in image processing, a CNN-based transfer learning model is employed to reduce the need for extensive network training and to extract features more suited to the CSI matrix. The proposed methods are trained and tested on a public CSI dataset, demonstrating an accuracy of approximately 94% to 99% across six activities. This performance outperforms the state-of-the-art in Human Activity Recognition for Customer Premises Equipment (CEP).

We integrate the transfer learning model that demonstrated the best performance into CPE and deploy it on a Raspberry Pi 4 for local detection applications. The User Services Platform (USP) serves as the standard for remote manipulation of connected CPE. Utilizing the USP protocol, end-users can independently manage and monitor their CPE through one or more Controllers.
# General Pipeline
## Overall framework of transfer learning model building:
![model_framework](https://github.com/user-attachments/assets/785835a4-4054-49ca-91cb-0019e7eca21f)

## CSI images of each class (Classes a and b are merged to class Down, classes c and d are merged to class Fall, classes e and f are merged to class Move):
<img width="573" alt="截屏2025-01-06 下午4 42 39" src="https://github.com/user-attachments/assets/a2078dee-9cf3-4b6b-8e41-b5b95418b0f7" />

# Experimental Environment (Employ Nexmon CSI Tool and collect CSI data for seven daily human activities, including walk, run, fall, lie down, sit down, stand up, and bend):
![image](https://github.com/user-attachments/assets/328634e2-6c5b-4e54-a085-3368a071c108)

# Proposed Methodologies & Evaluation
## Comparison of the original VGG16 and proposed VGG16-based transfer learning model (model I):
<img width="494" alt="截屏2025-01-06 下午4 50 11" src="https://github.com/user-attachments/assets/e8f92b48-c5f5-46de-a18b-7ce457985e3b" />

## Comparison of the original MobileNetV3-Large and proposed MobileNetV3-Large based transfer learning model (model II):
<img width="614" alt="截屏2025-01-06 下午4 52 11" src="https://github.com/user-attachments/assets/5512bf3b-291d-4d3c-8767-fac79a7691e6" />

## Hyperparameters used for the proposed model I and II: 
<img width="418" alt="截屏2025-01-06 下午5 01 39" src="https://github.com/user-attachments/assets/6ec7ecd2-7f45-42ae-b685-7389635d1958" />

## Hyperparameters used for the proposed model III -- model II with Fine-Tuning: 
<img width="421" alt="截屏2025-01-06 下午5 02 07" src="https://github.com/user-attachments/assets/8fb00cc5-4f05-4418-90a6-378ad58909b9" />

## Model Evaluation (Accuracy and Loss are refer to validation accuracy and validation loss. Bach size are the same, result in same amount of data in one epoch):
<img width="668" alt="截屏2025-01-06 下午5 03 38" src="https://github.com/user-attachments/assets/f93310b9-557e-4d42-83c8-e227f26f6430" />

# Deployment of Machine Learning Models in Local Environments
## USP framework:
![USP_framework](https://github.com/user-attachments/assets/ee75860d-b1a6-4091-a188-93e3c193e9e6)

## Notifications reach Controller as User Services Platform Notify messages like this:
header {
  msg_id: "ValueChange-2024-07-14T17:14:44Z-2"
  msg_type: NOTIFY
}
body {
  request {
    notify {
      subscription_id: "WiFiSensing"
      send_resp: false
      value_change {
        param_path: "Device.Services.WiFiSensing.CSI.Value"
        param_value: "{"moving":"0.949602","cpu_time_used":"0.611123"}"
      }
    }
  }
}

## Model prediction result:
{"action": "move","consumed time":"0.611123"}

This message informs the Controller a person is moving within the detection range, with the model execution time being 0.611123 seconds.
