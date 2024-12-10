# VisualCS

**Fine-tuning Language Models for Computer Science Concept Visualization Using ManimCE**

This repository contains the implementation and experimental results of VisualCS, a fine-tuned GPT-4o-mini model that generates ManimCE code to create animations of computer science concepts.

## Project Structure

The project contains three main experimental versions:

### Base Model (Zero-Shot Prompting)
- Documentation: `gpt-4o-mini-base/basic_prompting.md`
- Generated Animation: `gpt-4o-mini-base/media/videos/manim_basic_prompting/1080p60/MergeSortVisualization.mp4`

### Fine-Tuned Model v1 (Minimal Training)
- Documentation: `gpt-4o-mini-ft-v1/fine_tune_v1.md`
- Generated Animation: `gpt-4o-mini-ft-v1/media/videos/manim_fine_tuning/1080p60/MergeSortExample.mp4`

### Fine-Tuned Model v2 (Extended Training)
- Documentation: `gpt-4o-mini-ft-v2/fine_tune_v2.md`
- Note: No animation available for v2 due to unsuccessful generation

## Training Data

Training data for each version can be found in:
```
/trainingData/v0/  - Base validation data
/trainingData/v1/  - Version 1 training data
/trainingData/v2/  - Version 2 training data
```

## Getting Started

For detailed information about each version:
1. Review the corresponding markdown file for implementation details and results
2. Check the media folder for generated animations (base and v1 versions)
3. Examine the training data in the respective version folders

For a comprehensive understanding of the project, please refer to the paper.