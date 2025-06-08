
- **Classification Accuracy**
- **Domain Adaptation Metrics** (e.g., Fréchet Distance)
- **Robustness Metrics** (e.g., performance under noisy inputs)
- **Computational Efficiency** (e.g., inference time on depth data)
### 1.  Classification Accuracy

- **Why it’s good**: It measures how often the model predicts the correct class.
- **How it helps**: It’s the most direct way to tell if the model is learning to classify depth images properly.
- **What to watch for**: It doesn’t tell you _why_ the model fails or if it generalizes well to other domains.

---

### 2. Domain Adaptation Metrics
(e.g., Fréchet Distance)

- **Why it’s good**: Depth images from different sensors or environments may vary. These metrics tell you how well a model trained in one domain works in another.
- **How it helps**: Fréchet Distance, for instance, compares feature distributions. If the source and target domains are close, the model should generalize better.
- **What to watch for**: Low distance doesn’t always mean high accuracy—it just shows feature alignment.

---

### 3. Robustness Metrics
(e.g., performance under noisy inputs)

- **Why it’s good**: Depth sensors are often noisy (e.g., Kinect in low light). A model that breaks down with small noise is unreliable.
- **How it helps**: Testing on corrupted depth maps (e.g., with Gaussian noise, missing regions) shows how stable the model is in real-world use.
- **What to watch for**: Robustness is hard to tune without hurting accuracy on clean data.

---

### 4. Computational Efficiency
(e.g., inference time on depth data)

- **Why it’s good**: Depth classification may run on limited hardware (e.g., robots, AR devices). Speed matters.
- **How it helps**: Measuring inference time or memory usage tells you if the model is practical in real-world settings.
- **What to watch for**: Efficient models may sacrifice some accuracy, so there’s always a trade-off.