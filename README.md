# Human Beta-Globin (HBB) DNA Sequence Analyzer

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Environment](https://img.shields.io/badge/Environment-Linux%20%2F%20WSL%20Ubuntu-orange?logo=ubuntu&logoColor=white)
![Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library%20Only-brightgreen)
![Domain](https://img.shields.io/badge/Domain-Bioinformatics-purple)

A lightweight, dependency-free Python pipeline for parsing FASTA nucleotide sequences, quantifying base composition (A, T, G, C), calculating GC/AT content, and converting the coding nucleotide sequence into its corresponding mRNA transcript—demonstrated on the human hemoglobin subunit beta (*HBB*) gene.

---

## Biological Context

The ***HBB*** gene (located on human chromosome 11) encodes the **beta-globin** polypeptide subunit of adult hemoglobin (HbA). Hemoglobin is responsible for oxygen transport in red blood cells, and point mutations in *HBB* are directly associated with clinically significant hemoglobinopathies, including **sickle-cell disease** and **beta-thalassemia**.

Analyzing GC content and nucleotide composition provides foundational insights into sequence stability, gene structure, and coding region characteristics.

---

## Data Source

* **Database:** NCBI RefSeq (Nucleotide)
* **Accession ID:** `NM_000518.5`
* **Description:** *Homo sapiens* hemoglobin subunit beta (*HBB*), mRNA (cDNA representation in FASTA format)
* **Sequence Length:** 628 bp

---

## Project Structure

```text
Human-Globin-DNA-Analyzer/
├── data/
│   └── hbb_dna.fasta         # Input FASTA sequence (NCBI NM_000518.5)
├── scripts/
│   └── hbb_dna_analyzer.py   # Core parsing, GC/AT analysis, and transcription script
├── results/
│   └── report.txt            # Auto-generated sequence analysis report
└── README.md                 # Project documentation
```

---

## Features

* **Pure Python FASTA Parsing:** Reads raw `.fasta` files while automatically stripping metadata header lines (`>`) and newline characters—no external bioinformatics libraries required.
* **Nucleotide Quantification:** Computes total sequence length and individual base counts for Adenine (`A`), Thymine (`T`), Guanine (`G`), and Cytosine (`C`).
* **GC & AT Content Calculation:** Computes GC% and AT% formatted to two decimal places.
* **RNA Conversion:** Converts thymine (`T`) bases in the coding sequence to uracil (`U`) to generate the mRNA transcript.
* **Automated Reporting:** Exports a structured summary directly to `results/report.txt`.

---

## Getting Started

### Prerequisites

* Python 3.x
* Linux / WSL (Ubuntu) or any standard terminal environment

### Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Rakshit-Bioinfo/Human-Globin-DNA-Analyzer.git  
             https://github.com/Rakshit-Bioinfo/Human-Globin-DNA-Analyzer.git
   cd Human-Globin-DNA-Analyzer
   ```

2. **Run the analysis script:**
   ```bash
   python3 scripts/hbb_dna_analyzer.py
   ```

3. **View the generated report:**
   ```bash
   cat results/report.txt
   ```

---

## Results Summary (`NM_000518.5`)

| Metric | Value |
| :--- | :---: |
| **Total Sequence Length** | 628 bp |
| **Guanine (G) Count** | 165 |
| **Cytosine (C) Count** | 157 |
| **Adenine (A) Count** | 139 |
| **Thymine (T) Count** | 167 |
| **GC Content** | **51.27%** |
| **AT Content** | **48.73%** |

### Sample Output (`results/report.txt`)

```text
 ---Human Beta-Globin (HBB) Content Analyzer---
 total length of sequence: 628
 Total G count:165
 Total C count:157
 Total A count:139
 Total T count:167
GC percentage: 51.27%
AT percentage: 48.73%
RNA Sequence: ACAUUUGCUUCUGACACAACUGUGUUCACUAGCAACCUCAAACAGACACCAUGGUGCAUCUGACUCCUGAGGAGAA...
```

---

## Planned Enhancements

* **CLI Support:** Accept custom FASTA file paths via `argparse` to analyze any gene sequence dynamically.
* **ORF & Translation Module:** Locate the `AUG` start codon and translate the *HBB* mRNA into its 147-amino-acid beta-globin protein sequence.
* **Variant Detection:** Add a module to detect the classic sickle-cell point mutation (`GAG` → `GUG`, Glu6Val).
* **Visualization:** Generate nucleotide distribution bar charts using `matplotlib`.

---

## Author

**Rakshit Sinha**  
B.Sc. Bioinformatics | Chhatrapati Shivaji Maharaj University, Navi Mumbai  
GitHub: [@Rakshit-Bioinfo](https://github.com/Rakshit-Bioinfo)