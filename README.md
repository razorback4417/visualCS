# VisualCS: Fine-tuning Language Models for Computer Science Concept Visualization Using ManimCE

**UCLA COMM 188C Final Project**

*Theo Luu*
Computer Science
University of California, Los Angeles
luut@ucla.edu

## Project Proposal

### Research Question

How can we fine-tune LLMs to effectively create visual explanations of computer science concepts?

### Project Overview

I am developing VisualCS, a fine-tuned GPT-4o-mini model designed to create visual explanations of computer science concepts. The aim is to develop engaging animated walkthroughs of programming concepts, assisting students in understanding complex course material.

### Main Goal / Scientific Question

The primary investigation is whether fine-tuning GPT-4o-mini on ManimCE code generation improves CS concept visualizations compared to its base version. Evaluation will use adapted Holistic Evaluation of Text-to-Image Model (HEIM) metrics and educational effectiveness criteria inspired by Summer of Math Exposition (SoME).

### Model Selection Rationale

**GPT-4o-mini:** Chosen for its cost-efficiency and high performance, making it ideal for real-time educational interactions.

**ManimCE:** Preferred over ManimGL for its stability, robust documentation, and API support, as recommended by Grant Sanderson.

### NLP Task

Instruction-to-code generation:

- **Input:** Natural language descriptions of CS concept visualizations
- **Output:** Executable ManimCE Python code generating corresponding educational animations

### Data

- **Dataset:** `manim-codegen` from Hugging Face
- **Size:** 1,620 query-answer pairs
- **Format:** Natural language queries paired with ManimCE code solutions
- **Preprocessing:** Standardizing query formats and ensuring code consistency for fine-tuning

### Baselines

The un-fine-tuned GPT-4o-mini model will serve as the primary baseline. Performance on visualization generation tasks will be compared, focusing on code quality and educational impact.

### Evaluation

A two-pronged evaluation approach will be applied:

1. **Adapted HEIM Metrics:**
   - **Alignment:** How well the generated code matches the requested visualization
   - **Quality:** Technical correctness and efficiency of the code
   - **Originality:** Novel visualization approaches
   - **Reasoning:** Logical flow and structure
   - **Knowledge:** Accuracy in CS concept representation
   - **Efficiency:** Performance and resource usage of animations

2. **SoME Educational Content Criteria:**
   - **Motivation:** Engagement of learners
   - **Clarity:** Effectiveness in communicating concepts
   - **Novelty:** Uniqueness of visualization approach
   - **Memorability:** Lasting understanding impact

Each metric will be rated on a 1-5 numerical scale for quantitative comparison between base and fine-tuned models.

## References

1. Rajpurkar, P., Jia, R., & Liang, P. (2018). Know What You Don't Know: Unanswerable Questions for SQuAD. *Association for Computational Linguistics (ACL)*.

2. Lee, T., et al. (2023). Holistic Evaluation of Text-to-Image Models. *arXiv preprint arXiv:2311.04287*. https://arxiv.org/pdf/2311.04287

3. 3Blue1Brown. (2022). What Makes a Great Math Explanation? | SoME2 Results. https://www.youtube.com/watch?v=cDofhN-RJqg

4. Menick, J., et al. (2024). GPT-4o Mini: Advancing Cost-Efficient Intelligence. OpenAI. https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/

5. The Manim Community Developers. (2024). Manim -- Mathematical Animation Framework (v0.18.1). https://www.manim.community/

6. generaleoley. (2024). manim-codegen. Hugging Face. https://huggingface.co/datasets/generaleoley/manim-codegen