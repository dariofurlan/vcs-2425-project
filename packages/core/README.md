# Hello World


Resnet50

VGG-16

Inception

EfficientNet


# Input file size
Generally the input file size (ResNet and VGG-16) is 224 x 224, but for Inception and EfficientNet, the input file size is 299 x 299.
We don't want to restrain the input file size to a specific value, so we will use the original image size as the output file size of the depth estimation model.



1,270,000 images

3 img/sec

375 x 500
500 x 375
500 x 500

Output dim.: 250 x 250


- try to use batch mode to speed up the marigol depth est. process


# Preprocessing 

- Resize the images to 224x224 (time took: 3 seconds for 1300 images, avg.: 413.30it/s)
- Depth estimation of the resized images (output size: original dimensions)
   - With batch size 2 is approx 25 min

- 1300 images converted in ~ 16:04 = 964 sec (1.37 iterations/sec)
- we may need to just convert the 50.000 validation images and not the whole testing dataset. Because we are only trying to evaluate the model performance, and the performance is evaluated on the validation dataset.
- 50,000 images of the validation set can be easily converted with the same speed in the equivalent of 37,313 seconds (10.3 hours), so we will not convert the whole dataset.


```terminal
❯ nvidia-smi
Wed Apr 16 22:32:43 2025       
+-----------------------------------------------------------------------------------------+
| NVIDIA-SMI 550.54.14              Driver Version: 550.54.14      CUDA Version: 12.4     |
|-----------------------------------------+------------------------+----------------------+
| GPU  Name                 Persistence-M | Bus-Id          Disp.A | Volatile Uncorr. ECC |
| Fan  Temp   Perf          Pwr:Usage/Cap |           Memory-Usage | GPU-Util  Compute M. |
|                                         |                        |               MIG M. |
|=========================================+========================+======================|
|   0  NVIDIA GeForce RTX 3070 Ti     On  |   00000000:53:00.0  On |                  N/A |
| 85%   80C    P2            260W /  310W |    6178MiB /   8192MiB |     98%      Default |
|                                         |                        |                  N/A |
+-----------------------------------------+------------------------+----------------------+
                                                                                         
+-----------------------------------------------------------------------------------------+
| Processes:                                                                              |
|  GPU   GI   CI        PID   Type   Process name                              GPU Memory |
|        ID   ID                                                               Usage      |
|=========================================================================================|
|    0   N/A  N/A      2524      G   /usr/lib/xorg/Xorg                            209MiB |
|    0   N/A  N/A      2881      G   /usr/bin/gnome-shell                           85MiB |
|    0   N/A  N/A      3372      G   /usr/bin/akonadi_archivemail_agent              3MiB |
|    0   N/A  N/A      3390      G   /usr/bin/akonadi_mailfilter_agent               3MiB |
|    0   N/A  N/A      3401      G   /usr/bin/akonadi_sendlater_agent                3MiB |
|    0   N/A  N/A      3402      G   /usr/bin/akonadi_unifiedmailbox_agent           3MiB |
|    0   N/A  N/A     30848      G   ...erProcess --variations-seed-version        172MiB |
|    0   N/A  N/A     32436      G   /usr/lib/firefox-esr/firefox-esr               18MiB |
|    0   N/A  N/A    260304      C   ...2425/packages/core/.venv/bin/python       5608MiB |
+-----------------------------------------------------------------------------------------+
```