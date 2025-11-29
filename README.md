# 📈 NiftySense — SAX & Machine Learning Market Pattern Prediction Model
### 📊 Project Overview

**This repository presents a complete quantitative time-series pattern recognition model designed to analyze 10 years of Nifty50 data across multiple timeframes using Symbolic Aggregate approXimation (SAX).
The goal is to convert raw OHLCV data into symbolic patterns and apply machine-learning techniques to uncover recurring behaviors in the Indian equity markets.**

**The project demonstrates the power of SAX for noise reduction, shape-based pattern identification, and unsupervised clustering, providing a strong foundation for predictive analytics, trading signal generation, and market structure analysis.**

### ✨ Key Features

- SAX-Based Pattern Extraction: Implements full SAX workflow including Z-Normalization, PAA, breakpoints & symbolic encoding.
- Multi-Timeframe Analysis: Supports 1m, 5m, 15m, and 1D granularities for richer trend recognition.
- 10-Year Nifty50 Pipeline: Automated data ingestion and preprocessing using yfinance.
- Pattern Mining: Detects recurring SAX words, n-gram sequences, and frequent symbolic patterns.
- Machine Learning Clustering: Groups similar patterns using KMeans for behavioral segmentation.
- Noise Reduction: Achieves ~30% smoother, cleaner time-series representation.
- Pythonic Implementation: Uses industry-standard numerical and ML libraries.

### 🏗️ Architecture Diagram
```bash
NIFTY50 DATA (10 Years)
          ↓
nifty_50_data.py      → Fetch OHLCV data (yfinance)
          ↓
SAX_Implementation.py → Z-Norm, PAA, Breakpoints, SAX words
          ↓
pattern_engine.py     → n-grams, frequency maps, repeating patterns
          ↓
clustering.py         → KMeans clustering of SAX vectors
          ↓
main.py               → Final combined output & reports
```

### ⚙️ Technology Stack
```bash
- Technology	Purpose
- Python	Core implementation language
- NumPy	Numerical operations & vectorization
- Pandas	Data manipulation, time-series handling
- SciPy (norm)	Breakpoint generation for SAX
- scikit-learn	KMeans clustering
- yfinance	Nifty50 OHLCV data ingestion
```

### ⚙️ Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/GururajIngavale/SAX-ML-Market-Pattern-Forecaster.git
```

### 2️⃣ Install Dependencies
#### Required packages:
```bash
numpy
pandas
scipy
scikit-learn
yfinance
```

### ▶️ Run the Full Engine
```bash
python nifty_50_data.py
python SAX_Implementation.py
```

## ⭐ Contribution

**Feel free to fork, submit issues, or propose improvements!**
