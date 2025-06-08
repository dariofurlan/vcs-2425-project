## Abstract

As privacy concerns grow, computer vision must move beyond RGB—but can depth-only data compete? While most research focuses on encrypted color images or custom architectures, we ask: _**Can off-the-shelf models classify objects using just depth?**_

We evaluate four standard CNNs—AlexNet, VGG19, ResNet50, and Inception-v3—on depth-only inputs from two datasets: depth estimations generated from a subset of **ImageNet dataset** using the **Marigold model**, and real-world depth scans from the **Washington RGB-D** dataset.

After fine-tuning with an 80/20 train-validation split, we observed the following results: 
- On the **ImageNet depth-estimation dataset** (1,000 classes, 50k images), ResNet50 and Inception-v3 achieved **top-1 accuracies of 70% and 75%**.
- Accuracy improved to **78% and 81% **respectively on a **200-class subset** of ImageNet.
- On the **Washington RGB-D dataset** (51 classes, 40k images), all models **exceeded 90% top-1 accuracy**, due to reduced complexity from fewer classes.

These findings challenge the typical reliance on RGB data and specialized architectures for privacy-preserving vision. Depth data—whether approximated or raw—can enable strong classification performance using widely available **off-the-shelf models**. This opens the door to a broad range of applications, including **object detection** and **anomaly detection**, which share similar foundational architectures.