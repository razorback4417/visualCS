# VisualCS

**Fine-tuning Language Models for Computer Science Concept Visualization Using Manim**

This repository contains the implementation and experimental results of VisualCS, a fine-tuned GPT-4o-mini model that generates [Manim](https://github.com/ManimCommunity/manim) code to create visual explanations of computer science concepts.

## Project Structure

The project contains three experimental versions:

### Base Model (Zero-Shot Prompting)
- Documentation: [`gpt-4o-mini-base/basic_prompting.md`](https://github.com/razorback4417/visualCS/blob/main/gpt-4o-mini-base/basic_prompting.md)
- Generated Animation: [`gpt-4o-mini-base/media/.../MergeSortVisualization.mp4`](https://github.com/razorback4417/visualCS/blob/main/gpt-4o-mini-base/media/videos/manim_basic_prompting/1080p60/MergeSortVisualization.mp4)

### Fine-Tuned Model v1
- Documentation: [`gpt-4o-mini-ft-v1/fine_tune_v1.md`](https://github.com/razorback4417/visualCS/blob/main/gpt-4o-mini-ft-v1/fine_tune_v1.md)
- Generated Animation: [`gpt-4o-mini-ft-v1/media/.../MergeSortExample.mp4`](https://github.com/razorback4417/visualCS/blob/main/gpt-4o-mini-ft-v1/media/videos/manim_fine_tuning/1080p60/MergeSortExample.mp4)

### Fine-Tuned Model v2
- Documentation: [`gpt-4o-mini-ft-v2/fine_tune_v2.md`](https://github.com/razorback4417/visualCS/blob/main/gpt-4o-mini-ft-v2/fine_tune_v2.md)
- Note: No animation available for v2 due to unsuccessful generation. [2 additional examples](https://github.com/razorback4417/visualCS/blob/main/gpt-4o-mini-ft-v2/other_responses.md)

## Training Data

Training data for each version can be found in:
```
/trainingData/v0/  - Base validation data
/trainingData/v1/  - Version 1 training data
/trainingData/v2/  - Version 2 training data
```