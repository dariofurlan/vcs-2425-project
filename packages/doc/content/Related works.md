# Related Works

Recent research has increasingly focused on integrating computer vision with privacy-preserving techniques, especially in sensitive environments such as hospitals, nursing homes, and eldercare centers. **Depth images** have also gained traction in the research community as a compelling privacy-aware alternative to conventional RGB images. They inherently lack fine-grained visual details—such as facial features or clothing patterns—while still capturing the spatial and structural cues necessary for recognition tasks. [1, 2, 7, 8] have demonstrated the effectiveness of low-resolution or depth-only data across tasks such as action recognition, pose estimation, and fall detection, highlighting its potential in real-world healthcare and surveillance settings.

**Encrypted image-based classification techniques**, such as block-wise scrambling, permutation encryption, and homomorphic encryption, have been used in [3, 4, 5, 10] to protect sensitive data during both training and inference. When combined with modern architectures like Vision Transformers or ConvMixers, these methods have been shown to effectively preserve privacy without compromising accuracy. 

**Hardware-based approaches** have also been proposed to enforce privacy directly at the sensing stage. For example, optical filters like phase masks [6] can limit facial detail capture, which allows privacy-preserving depth estimation at the point of image acquisition. Some approaches go further by anonymizing individuals in real time through avatars or abstract representations [9], addressing privacy concerns by **system-level architecture** rather than relying solely on data manipulation or model design.

Regarding the use of depth data for classification, several papers have proposed adaptations of models originally trained on RGB images. For example, [11] introduces a lightweight encoder that takes a single-channel depth input and transforms it into a three-channel RGB-like input, thereby making it compatible with pre-trained CNNs such as VGG-16. [12] augments VGG-16 with a single 3D convolution layer to enable depth-only inference without retraining on depth images. Similarly, [13] and [15] illustrate that applying simple color maps (e.g., Jet) to depth images allows standard models like ResNet-101 and ResNet-18 to achieve high classification accuracy in fruit sorting and animal posture recognition.

Depth-based methods have also proven effective in privacy-sensitive healthcare environments. [14] reviews **privacy-aware in-home monitoring** systems using depth sensors for tasks like fall detection and gait analysis (assessing walking patterns) in eldercare, offering a less privacy-invasive alternative to RGB-based solutions. Beyond human monitoring, [15] applies depth data to classify animal postures, illustrating the broader versatility of this modality where texture is unnecessary or unavailable.

Collectively, these studies reflect a growing consensus on the **technical viability** and **societal urgency** of privacy-preserving computer vision. However, many focus on specialized architectures, encrypted RGB inputs, or hardware solutions. By contrast, relatively few explore the **baseline performance of classification models on raw depth images**. In this paper, we address that gap by evaluating widely used image classification models (i.e., AlexNet, VGG19, ResNet50, and Inception-v3) on depth images, providing a foundation for future privacy-preserving systems.

====

This is a list of relevant studies exploring the use of depth images and computer vision techniques to preserve privacy in sensitive contexts such as hospitals and nursing homes:

## 1. Privacy-Preserving Action Recognition for Smart Hospitals using Low-Resolution Depth Images
[Paper Link](https://arxiv.org/abs/1811.09950)

This study proposes the use of low-resolution depth images to recognize actions in hospital environments, reducing sensitive visual information and improving patient privacy.

## 2. Human Pose Estimation on Privacy-Preserving Low-Resolution Depth Images
[Paper Link](https://arxiv.org/abs/2007.08340)

The authors present a method for estimating human poses using low-resolution depth images, combining a super-resolution network with a pose estimation network, while maintaining individual privacy.

## 3. Privacy-Preserving Image Classification Using ConvMixer with Adaptative Permutation Matrix and Block-Wise Scrambled Image Encryption
[Paper Link](https://www.mdpi.com/2313-433X/9/4/85)

This work introduces an image classification method that uses images encrypted through block scrambling and a modified ConvMixer network, protecting privacy without compromising accuracy.

## 4. Privacy-Preserving Image Classification Using Isotropic Network
[Paper Link](https://arxiv.org/abs/2204.07707)

The authors propose an image classification method that employs encrypted images and an isotropic network, such as Vision Transformer, to maintain high performance while preserving privacy.

## 5. Privacy-Preserving Vision Transformer on Permutation-Encrypted Images
[Paper Link](https://openreview.net/forum?id=eL1iX7DMnPI)

This study presents an image recognition model that uses permutation-encrypted images and a Vision Transformer, ensuring the privacy of visual data.

## 6. Learning Phase Mask for Privacy-Preserving Passive Depth Estimation
[Paper Link](https://zaidtas.github.io/privacymask/pdf/privacy_preserving_depth_estimation.pdf)

The authors develop an optical filter, implemented as a phase mask, that allows depth estimation while preserving privacy by preventing facial recognition.

## 7. Privacy Preserving Automatic Fall Detection for Elderly Using RGBD Cameras
[Paper Link](https://media-lab.ccny.cuny.edu/YLTCCNYHomepage/Publications/ICCHP12_Fall_Detection.pdf)

This work proposes an automatic fall detection system for the elderly using RGBD cameras, focusing on using depth information to ensure privacy.

## 8. Beyond Privacy of Depth Sensors in Active and Assisted Living Applications
[Paper Link](https://dl.acm.org/doi/fullHtml/10.1145/3529190.3534764)

The study examines applications of depth sensors in assisted living environments, discussing privacy implications and potential solutions to protect sensitive data.

## 9. AI-Driven Privacy in Elderly Care: Developing a Comprehensive Monitoring System
[Paper Link](https://www.mdpi.com/2076-3417/14/10/4150)

The authors present a monitoring system for elderly care that uses artificial intelligence to anonymize subjects in real-time, replacing them with 2D avatars to protect their privacy.

## 10. Efficient and Privacy-Preserving Image Classification Using Homomorphic Encryption
[Paper Link](https://journalofcloudcomputing.springeropen.com/articles/10.1186/s13677-023-00537-0)

## 11 2021 — “Convolution-Based Encoding of Depth Images for Transfer Learning in RGB-D Scene Classification,” Sensors
[paper Link] (https://www.mdpi.com/1424-8220/21/23/7950)

Presents a lightweight encoder that converts single-channel depth to 3-channel format for direct use with pre-trained RGB models like VGG-16, avoiding complex HHA encoding. Includes code and ablation on SUN RGB-D.

## 12 2017 — “RGB-D Object Recognition Using Deep CNNs (VGG3D),” ICCV-w
[paper Link](https://ieeexplore.ieee.org/document/8265318)

Adds a single 3D conv layer to VGG-16, initialized by replicating RGB filters along depth. Allows testing depth-only inputs while keeping the rest of the model frozen—no retraining needed.

## 13 2023 — “Fruit Classification Using Colorized Depth Images,” IJACSA
[paper Link](https://thesai.org/Publications/ViewPaper?Volume=14&Issue=5&Code=IJACSA&SerialNo=106)

Applies simple color maps (e.g., Jet) to depth images and feeds them into standard CNNs like ResNet-101, achieving up to 100% accuracy. Shows that colorized depth is an effective baseline.

## 14 — “In-Home Older Adults’ Activity Pattern Monitoring Using Depth Sensors: A Review,” Sensors
[paper Link](https://www.mdpi.com/1424-8220/22/23/9067)
Reviews elder-care systems using depth for activity monitoring and fall detection. Highlights how depth avoids capturing identifiable features and includes a helpful dataset summary.


## 15  — “Classification of Sow Postures Using CNN and Depth Images,” Biosystems Eng.
[paper Link](https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1921&context=biosysengfacpub)

Uses ResNet-18 on depth images to classify animal postures with 98.3% accuracy, showing that texture-free depth is sufficient for detailed recognition—relevant for privacy-focused human applications.


This study introduces an image classification method that combines homomorphic encryption with data partitioning, allowing secure image processing in cloud environments.

---

These studies highlight the growing importance of developing computer vision systems that respect privacy, especially in sensitive contexts.