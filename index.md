
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

## Dataset Sample
```javascript
{
  "id": "0704.0001",
  "submitter": "Pavel Nadolsky",
  "authors": "C. Bal\\'azs, E. L. Berger, P. M. Nadolsky, C.-P. Yuan",
  "title": "Calculation of prompt diphoton production cross sections at Tevatron and\n  LHC energies",
  "comments": "37 pages, 15 figures; published version",
  "journal-ref": "Phys.Rev.D76:013009,2007",
  "doi": "10.1103/PhysRevD.76.013009",
  "report-no": "ANL-HEP-PR-07-12",
  "categories": "hep-ph",
  "license": null,
  "abstract": "  A fully differential calculation in perturbative quantum chromodynamics is\npresented for the production of massive photon pairs at hadron colliders. All\nnext-to-leading order perturbative contributions from quark-antiquark,\ngluon-(anti)quark, and gluon-gluon subprocesses are included, as well as\nall-orders resummation of initial-state gluon radiation valid at\nnext-to-next-to-leading logarithmic accuracy. The region of phase space is\nspecified in which the calculation is most reliable. Good agreement is\ndemonstrated with data from the Fermilab Tevatron, and predictions are made for\nmore detailed tests with CDF and DO data. Predictions are shown for\ndistributions of diphoton pairs produced at the energy of the Large Hadron\nCollider (LHC). Distributions of the diphoton pairs from the decay of a Higgs\nboson are contrasted with those produced from QCD processes at the LHC, showing\nthat enhanced sensitivity to the signal can be obtained with judicious\nselection of events.\n",
  "versions": [
    {
      "version": "v1",
      "created": "Mon, 2 Apr 2007 19:18:42 GMT"
    },
    {
      "version": "v2",
      "created": "Tue, 24 Jul 2007 20:10:27 GMT"
    }
  ],
  "update_date": "2008-11-26",
  "authors_parsed": [
    [
      "Balázs",
      "C.",
      ""
    ],
    [
      "Berger",
      "E. L.",
      ""
    ],
    [
      "Nadolsky",
      "P. M.",
      ""
    ],
    [
      "Yuan",
      "C. -P.",
      ""
    ]
  ]
}
```

### T5 Model

### BLEU Score

## Examples

| Abstract | Predicted Title | Actural Title | BLEU Score |
| -------- | --------------- | ------------- | ---------- |
| We present new results concerning threshold functions for a wide family of random intersection graphs. To this end we apply the coupling method used for establishing threshold functions for homogeneous random intersection graphs introduced by Karo\\'nski, Scheinerman, and Singer--Cohen. In the case of inhomogeneous random intersection graphs the method has to be considerably modified and extended. By means of the altered method we are able to establish threshold functions for a general random intersection graph for such properties as | threshold functions for homogeneous random intersection graphs have to be modified and extended | The coupling method for inhomogeneous random intersection graphs | 0.43 |
| Although the free energy of a genome packing into a virus is dominated by DNA-DNA interactions, ordering of the DNA inside the capsid is elasticity-driven, suggesting general solutions with DNA organized into spool-like domains. Using analytical calculations and computer simulations of a long elastic filament confined to a spherical container, we show that the ground state is not a single spool as assumed hitherto, but an ordering mosaic of multiple homogeneously-ordered domains. At low densities, we observe concentric spools, while at higher densities, other morphologies emerge, which resemble topological links. We discuss our results in the context of metallic wires, viral DNA, and flexible polymers | a long elastic filament confined to a spherical container is confined | Spontaneous Domain Formation in Spherically-Confined Elastic Filaments | 0.52 |
| Learning in multi-agent scenarios is a fruitful research direction, but current approaches still show scalability problems in multiple games with general reward settings and different opponent types. The Multi-Agent Reinforcement Learning in Malm\\O competition is a new challenge that proposes research in this domain using multiple 3D games. The goal of this contest is to foster research in general agents that can learn across different games and opponent types, proposing a challenge as a milestone in the direction of Artificial General Intelligence | the multi-agent Reinforcement Learning in MalmO competition proposes research in | The Multi-Agent Reinforcement Learning in Malm\\O Competition | 0.5 |
| We propose a simple and efficient scheme based on adaptive finite elements over conforming quadtree meshes for collapse plastic analysis of structures. Our main interest in kinematic limit analysis is concerned with both purely cohesive-frictional and cohesive materials. It is shown that the most computational efficiency for collapse plastic problems is to employ an adaptive mesh strategy on quadtree meshes. However, a major difficulty in finite element formulations is the appearance of hanging nodes during adaptive process. This can be resolved by a definition of conforming quadtree meshes in the context of polygonal elements. Piecewise-linear shape functions enhanced with generalized bubble functions in barycentric coordinates are used to approximate the velocity field. Numerical results prove the reliability and benefit of the present approach | kinematic limit analysis is based on adaptive finite elements over conforming quadtre | An adaptive strategy based on conforming quadtree meshes for kinematic limit analysis | 0.71 |
| In this paper we propose a mathematical model for the onset and progression of Alzheimer's disease based on transport and diffusion equations. We regard brain neurons as a continuous medium, and structure them by their degree of malfunctioning. Two different mechanisms are assumed to be relevant for the temporal evolution of the disease: i) diffusion and agglomeration of soluble polymers of amyloid, produced by damaged neurons; ii) neuron-to-neuron prion-like transmission. We model these two processes by a system of Smoluchowski equations for the amyloid concentration, coupled to a kinetic-type transport equation for the distribution function of the degree of malfunctioning of neurons. The second equation contains an integral term describing the random onset of the disease as a jump process localised in particularly sensitive areas of the brain. Our numerical simulations are in good qualitative agreement with clinical images of the disease distribution in the brain which vary from early to advanced stages | we propose a mathematical model for the onset and progression of Alzheimer's disease | Alzheimer's disease: a mathematical model for onset and progression | 0.79 |

## References
1. [Wikipedia: Topic Sentence](https://en.wikipedia.org/wiki/Topic_sentence)
