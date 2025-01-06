# IoT: Wi-Fi Sensing and Diagnostic for Customer Premises Equipment using Transfer Learning and USP.
This paper presents a lightweight deep transfer learning based human activity
detection and diagnostic recognition approach using WiFi sensing. In our method,
the amplitude matrix of each WiFi Channel State Information (CSI) stream is reorganized
as an image. Therefore, WiFi based human activity recognition is transformed into
an image classification task. Leveraging the high potential of Convolutional Neural
Networks in image processing, a CNN-based transfer learning model is employed to
reduce the need for extensive network training and to extract features more suited
to the CSI matrix. The proposed methods are trained and tested on a public CSI dataset, 
demonstrating an accuracy of approximately 94% to 99% across six activities. 
This performance outperforms the state-of-the-art in Human Activity Recognition 
for Customer Premises Equipment (CEP).

We integrate the transfer learning model that demonstrated the best performance
into CPE and deploy it on a Raspberry Pi 4 for local detection applications. 
The User Services Platform (USP) serves as the standard for remote manipulation 
of connected CPE. Utilizing the USP protocol, end-users can independently manage 
and monitor their CPE through one or more Controllers.
