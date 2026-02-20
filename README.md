# 🌉 Bridge Monitoring Streaming Pipeline  
### Declarative Pipeline • Lakeflow • Medallion Architecture

---

## 🇬🇧 English Version

## 📌 Overview
This project implements a **real‑time bridge monitoring system** using a **Declarative Pipeline** built with **Lakeflow** and the **Medallion Architecture** (Bronze → Silver → Gold).  
The pipeline ingests streaming sensor data (temperature, tilt, vibration), processes it through structured transformation layers, and produces enriched metrics for monitoring structural health.

The repository includes:
- Python scripts for each transformation layer  
- SQL queries for materialized views  
- A Databricks Lakeflow streaming pipeline  
- A visual pipeline diagram  

---

## 🏗️ Architecture

### 🔹 **Declarative Pipeline (Lakeflow)**
The pipeline is defined declaratively:  
- You describe **what** each table should contain  
- Lakeflow handles **how** to compute it  
- Automatic orchestration, dependency resolution, and incremental updates

### 🥉 Bronze Layer — Raw Streaming Data
Files:
- `00_data_generator.py`  
- `01_bronze_processing.py`  

Responsibilities:
- Ingest raw sensor streams (temperature, tilt, vibration)  
- Store unprocessed data in Bronze tables  
- Preserve original schema and timestamps  

### 🥈 Silver Layer — Cleaned & Standardized Data
File:
- `02_silver_processing.py`  

Responsibilities:
- Clean and standardize sensor data  
- Normalize schemas  
- Remove corrupt or incomplete records  
- Prepare data for metric computation  

### 🥇 Gold Layer — Enriched Metrics
File:
- `03_gold_processing.py`  

Responsibilities:
- Compute aggregated bridge metrics  
- Join with metadata  
- Produce analytics‑ready tables for dashboards and alerts  

---

## 🔄 Lakeflow Streaming Pipeline
The Databricks pipeline processes the following tables in real time:

| Table Name          | Description                          |
|---------------------|--------------------------------------|
| `bridge_temperature` | Temperature sensor stream            |
| `bridge_tilt`        | Tilt sensor stream                   |
| `bridge_vibration`   | Vibration sensor stream              |
| `bridge_metadata`    | Static metadata (bridge info)        |
| `bridge_metrics`     | Final enriched metrics (Gold layer)  |

Each table is automatically refreshed and incrementally updated.

---

## 🧰 Technologies Used
- **Databricks Lakeflow** (Declarative Pipelines)  
- **Python** (ETL scripts)  
- **SQL** (Materialized views & queries)  
- **Medallion Architecture**  
- **Streaming data processing**  
- **Real‑time sensor ingestion**  

---

## 🎯 Objectives
- Build a fully declarative, maintainable streaming pipeline  
- Monitor bridge health using real‑time sensor data  
- Apply Medallion Architecture best practices  
- Produce enriched metrics for dashboards and alerting systems  

---


---

---

# 🇫🇷 Version Française

## 📌 Aperçu
Ce projet met en place un **système de surveillance de pont en temps réel** grâce à un **pipeline déclaratif** utilisant **Lakeflow** et l’**architecture Medallion** (Bronze → Silver → Gold).  
Le pipeline ingère des flux de capteurs (température, inclinaison, vibration), les transforme en couches structurées et produit des métriques enrichies pour surveiller l’état structurel du pont.

Le dépôt contient :
- Des scripts Python pour chaque couche  
- Des requêtes SQL  
- Un pipeline Lakeflow en streaming  
- Un schéma visuel du pipeline  

---

## 🏗️ Architecture

### 🔹 **Pipeline Déclaratif (Lakeflow)**
Le pipeline est défini de manière déclarative :  
- Vous décrivez **ce que** chaque table doit contenir  
- Lakeflow gère **comment** la calculer  
- Orchestration automatique et mises à jour incrémentales

### 🥉 Couche Bronze — Données Brutes en Streaming
Fichiers :
- `00_data_generator.py`  
- `01_bronze_processing.py`  

Rôle :
- Ingérer les flux bruts des capteurs  
- Stocker les données sans transformation  
- Préserver le schéma original  

### 🥈 Couche Silver — Données Nettoyées
Fichier :
- `02_silver_processing.py`  

Rôle :
- Nettoyer et standardiser les données  
- Normaliser les schémas  
- Retirer les enregistrements corrompus  
- Préparer les données pour les métriques  

### 🥇 Couche Gold — Données Enrichies
Fichier :
- `03_gold_processing.py`  

Rôle :
- Calculer les métriques agrégées  
- Joindre les données avec les métadonnées  
- Produire des tables prêtes pour la BI et les alertes  

---

## 🔄 Pipeline Lakeflow en Streaming
Le pipeline traite en continu les tables suivantes :

| Nom de Table          | Description                           |
|-----------------------|----------------------------------------|
| `bridge_temperature`  | Flux de température                    |
| `bridge_tilt`         | Flux d’inclinaison                     |
| `bridge_vibration`    | Flux de vibration                      |
| `bridge_metadata`     | Métadonnées statiques                  |
| `bridge_metrics`      | Métriques enrichies (couche Gold)      |

Chaque table est mise à jour automatiquement et de manière incrémentale.

---

## 🧰 Technologies Utilisées
- **Databricks Lakeflow**  
- **Python**  
- **SQL**  
- **Architecture Medallion**  
- **Traitement de données en streaming**  
- **Ingestion de capteurs en temps réel**  

---

## 🎯 Objectifs
- Construire un pipeline déclaratif et maintenable  
- Surveiller l’état d’un pont en temps réel  
- Appliquer les bonnes pratiques de l’architecture Medallion  
- Produire des métriques enrichies pour la BI et les alertes  

---

## 📁 Structure du Dépôt
