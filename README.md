# BRES + Lightcast Data Analysis Project: West of England Industry Insights Pack

**Goal:** Build a high-perfromance Python workflow that automatically produces analysis and interactive visuals of key West of England industries (using BRES 2024 and Lightcast job posting data). The final output will mirror the format and insights of the exisitng 'Industries Inisght Pack' that has previously been in a slide deck format. This project should leave code that can easily be lightly edited to reproduce insight packs yearly going forward.

**stack:** Python, Polars, Plotly, python-pptx
**Deadline Focus:** December 2025, following from 28th October BRES 2024 data being released

---

## Phase 1 - Setup & Foundations
*Goal: Get environment, tools and foundational knowledge ready for Polars + Plotly.*

### Tasks and Checklist
| Week | Task | Status |
| :--- | :--- | :---: |
| Week 1 | Install Python, VS Code and set up Git + GitHub. | Done |
| Week 1 | Create Project project folder: 'bres-analysis/' with subfolders ('data/', 'scripts/', 'output/', etc.). | Done |
| Week 1 | Install core libraries: 'pip install polar plotly jupyterlap openpyxl python-pptx' | Done |
| Week 2 | Polars Practice: In a Jupyter Notebook, practice importing a sample CSV/Excel file. | DOne |
| Week 2 | Use Polars syntax for filtering, grouping, and aggregating data. | Done |
| Week 2 | Plotly Practice: Create a simple interactive Plotly Express chart (e.g., a bar chart or line plot). | To Do |

### Expected Output
* A functional Python development environment with the core libraries installed. 
* A test Jupyter Notebook demonstarting basic Polars data wrangling and a simple interactive Plotly chart. 

## Phase 2 - Data Acquistions & Exploration (Late Oct-Early Nov)
* Goal: Load and explore the real BRES 2024 data and merge it with Lightcast data.*

### Tasks & Checklist
| Week | Task | Status |
| :--- | :--- | :--- |
| **Week 3** | **Data Download:** Download BRES 2024 data (from Nomis or ONS, depending on which leaves more flexibility for automating process once complete) and save raw files in 'data/raw'. | To Do |
| **Week 3** | **Cleaning Script:** Begin 'scripts/clean_bres.py'. Use **Polars** to read the file, rename key columns (for consistency), filter the data to the West of England region, and inspect data types. | To Do |
| **Week 3** | **Geographic mapping:** Document the geographical codes (or names) needed for the West of England CA and its unitary authorities (+ N Somerset). | To Do |
| **Week 4** | **Data Join:** Import Lightcast job posting data and write a Polars script to join it with cleaned BRES data (need to be explored further, LLMs recommend using SIC codes, but might not be a possible route with job posting data). | To Do |
| **Week 4** | **Replicate Chart:** Use the combined dataset to recreate a simple chart from the Insight Pack (e.g, "Number of jobs by area") using **Plotly Express**. | To Do |
| **Week 4** | **Export test:** Export the Plotly chart as both interactive HTML file and a static PNG file. | To Do |

### Expected Outcome
* Cleaned and documented Polars dataframe from BRES 2024 data (to be reviewed if taking API approach)
* Combined BRES + Lightcast dataset. 
* The first successfully replivated, interactive insight chart using Plotly. 

---

## Phase 3 - Modular Analysis & Resuseable Functions (Mid November)
*Goal: Create reusable Polars functions to generate industry summaries and Plotly functions to generate standard charts.*


### Tasks & Checklist 
| Week | Task | Status |
| :--- | :--- | :--- |
| **Week 5** | **Analysis Utilities:** Create 'scripts/analysis\_utils.py'. | To Do |
| **Week 5** | Write a function to *filter by industry (SIC code)* and return a summary Polars DataFrame ready for plotting. | To Do |
| **Week 6** | **Plotting Functions:** Create Plotly functions to automate the key chart types for *all* industries: <br> 1. Full-time vs Part-time Split Bar Chart <br> 2. Employment Trend Over Time Line Chart (Regional vs. National) <br> 3. Top 20 Sub-Industries Bar Chart (using SIC codes) | To Do |
| **Week 6** | Run the analysis and function for 3-4 sectors (potentially growth sectors). | To Do |

### Expected Output
* A modular Python file ('analysis_utils.py') with reusable Polars functions. 
* A folder ('output/charts/') containing a set of reproducible, interactive Plotly charts for 3-4 key industries.

---

## Phase 4 - Presentation & Automation (Late November/early December)

### Tasks & Checklist

| Week | Task | Status |
| :--- | :--- | :--- |
| **Week 7** | **Presentation Automation:** Use 'python-pptx' to build a slide deck. | To Do |
| **Week 7** | Programmatically insert exported charts/tables into the PowerPoint slides, following agreed structure of the Insight Pack. | To Do |
| **Week 7** | Generate a text summary (Markdown or Jupyter Notebook) of the key headlines for each industry. | To Do |
| **Week 8** | **Final Review:** Review output with colleagues. | To Do |
| **Week 8** | **Documentation:** Update this 'README.md' and add comments to code for clarity and future maintenance. | To Do |
| **Week 8+** | Begin exploring Plotly Dash or Streamlit or other route to publish further interactive work and/or dashboard on *quarto* or other publishable programme. | To Do |

### Expected Output 
* A prototype automated PowerPoint deck with refreshed BRES-Lightcast visuals.
* A final, working, and documented analysis pipeline (scripts/function). 

---

## Core Tech Stack

| Purpose | Tool / Library |
| :--- | :--- |
| **Data Manipulation** | **Polars** (`import polars as pl`) |
| **Data Visualization** | **Plotly** (`plotly.express` for quick plots, `plotly.graph_objects` for fine control) |
| **Excel I/O** | `openpyxl` (used by Polars for reading/writing Excel) |
| **PowerPoint Automation** | **python-pptx** |
| **Interactive Environment**| Jupyter Notebooks / JupyterLab |
| **Version Control** | Git + GitHub |

## Stretch Goals (after completion) 
* **API function:** Move from downloaded data programme to one based on APIs to allow for easier process of updating year-on-year
* **Interactive Dashboard:** Build a simple online dashbaord sumamrisng data using Plotly Dash or Streamlit
* **Benchmarking** Add data from other Combined Authorities (potentially doing this already to some extent) to provide a national comparative context. 
* **Automated refresh:** Implement a simple Python scheduler to run the entire analysis pipeline yearly when BRES data is updated (potentialyl needing API work as crucial to this)