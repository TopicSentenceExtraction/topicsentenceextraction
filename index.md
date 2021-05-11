
### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).



# Topic Sentence Extraction

## Introduction
Topic sentence is one of the crucial parts for readers in article reading for many reasons. It summarizes the main idea of a body paragraph to show the big picture of a writer's idea to readers. Other than being a mere summary, topic sentence also serves as a sub-thesis of an article which is general enough to cover the support in the rest of body paragraph while being more direct than the thesis of the whole article[1]. Hence, finding a way to summarize the paragraph with a grammatical sentence will be very helpful for readers to recognize the main idea much easier in a short period of time.

Our goal is to build a topic sentence generation tool. This tool receives a body paragraph as the input then returns a summary sentence as the output. The dataset that we are going to use is [arXiv Dataset](https://www.kaggle.com/Cornell-University/arxiv) from Kaggle which includes millions of paper metadata in json format. Our team uses [T5(Text-to-Text Transfer Transformer)](https://huggingface.co/transformers/model_doc/t5.html) for model traning and [BLEU score](https://en.wikipedia.org/wiki/BLEU) for model evaluation.

## Methodologies

### T5 Model

### BLEU Score

## Examples

| Abstract | Predicted Title | Actural Title | BLEU Score |
| -------- | --------------- | ------------- | ---------- |
| We present new results concerning threshold functions for a wide family of random intersection graphs. To this end we apply the coupling method used for establishing threshold functions for homogeneous random intersection graphs introduced by Karo\\'nski, Scheinerman, and Singer--Cohen. In the case of inhomogeneous random intersection graphs the method has to be considerably modified and extended. By means of the altered method we are able to establish threshold functions for a general random intersection graph for such properties as | threshold functions for homogeneous random intersection graphs have to be modified and extended | The coupling method for inhomogeneous random intersection graphs | 0.43 |
| Although the free energy of a genome packing into a virus is dominated by DNA-DNA interactions, ordering of the DNA inside the capsid is elasticity-driven, suggesting general solutions with DNA organized into spool-like domains. Using analytical calculations and computer simulations of a long elastic filament confined to a spherical container, we show that the ground state is not a single spool as assumed hitherto, but an ordering mosaic of multiple homogeneously-ordered domains. At low densities, we observe concentric spools, while at higher densities, other morphologies emerge, which resemble topological links. We discuss our results in the context of metallic wires, viral DNA, and flexible polymers | a long elastic filament confined to a spherical container is confined | Spontaneous Domain Formation in Spherically-Confined Elastic Filaments | 0.52 |

## References
1. https://en.wikipedia.org/wiki/Topic_sentence
