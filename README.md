# Semantic Spatiotemporal Mutual Exclusivity Simulator

![Python](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Overview

This project provides a Python tool to analyze semantic keyword relationships based on their spatiotemporal occurrences.  
It detects pairs of keywords that are **impossible** to co-occur within a specified spatiotemporal distance threshold, effectively ruling out incompatible keyword combinations.

The core concept combines semantic mutual exclusivity with spatial and temporal proximity, enabling advanced keyword analysis in domains where space and time matter.

## Features

- Interactive text interface to input keywords and their spatial (x, y, z) and temporal (t) coordinates.  
- Automatically cross-references all keywords pairwise using combinatorics.  
- Classifies keyword pairs as **possible** (can co-occur) or **impossible** (mutually exclusive based on threshold distance).  
- Flexible parameters to weight temporal distance and define proximity thresholds.

## Getting Started

### Prerequisites

- Python 3.7 or higher  
- [NumPy](https://numpy.org/) library

Install dependencies using pip:

