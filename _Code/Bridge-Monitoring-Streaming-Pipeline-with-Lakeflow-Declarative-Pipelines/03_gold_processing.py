# Databricks notebook source
# MAGIC %md
# MAGIC # Gold: 10-minute windowed metrics combining silver aggregates

# COMMAND ----------

import dlt
from pyspark.sql.functions import col, window, max, avg, round

# 1. DEFINE THE GOLD TABLE IN THE DLT PIPELINE
@dlt.table(
    name="03_gold.bridge_metrics",
    comment="10-min avg temperature, max vibration & max tilt per bridge with window start/end"
)
def bridge_metrics():


    # 2. READ & WATERMARK: LOAD STREAMING DATA FROM SILVER TABLES.
    # .WITHWATERMARK TELLS SPARK TO WAIT UP TO 2 MINUTES FOR LATE-ARRIVING DATA.
    # THIS PREVENTS THE SYSTEM FROM "CLOSING" A WINDOW TOO EARLY.


    temp = dlt.read_stream("02_silver.bridge_temperature").withWatermark("event_time", "2 minutes")
    vib = dlt.read_stream("02_silver.bridge_vibration").withWatermark("event_time", "2 minutes")
    tilt = dlt.read_stream("02_silver.bridge_tilt").withWatermark("event_time", "2 minutes")

    # 3. AGGREGATE TEMPERATURE: CALCULATE AVERAGE TEMP EVERY 10 MINUTES PER BRIDGE.

    temp_agg = (
      temp
        .groupBy(window("event_time", "10 minutes"), col("bridge_id"), col("name"), col("location"))
        .agg(avg("temperature").alias("avg_temperature"))
        .select("bridge_id", "name", "location", col("window.start").alias("window_start"), col("window.end").alias("window_end"), "avg_temperature")
    )



    # 4. AGGREGATE VIBRATION: CALCULATE MAX VIBRATION EVERY 10 MINUTES.
    vib_agg = (
      vib
        .groupBy(window("event_time", "10 minutes"), col("bridge_id"))
        .agg(max("vibration").alias("max_vibration"))
        .select("bridge_id", col("window.start").alias("window_start"), col("window.end").alias("window_end"), "max_vibration")
    )




    # 5. AGGREGATE TILT: CALCULATE MAX TILT ANGLE EVERY 10 MINUTES.
    tilt_agg = (
      tilt
        .groupBy(window("event_time", "10 minutes"), col("bridge_id"))
        .agg(max("tilt_angle").alias("max_tilt_angle"))
        .select("bridge_id", col("window.start").alias("window_start"), col("window.end").alias("window_end"), "max_tilt_angle")
    )



    # 6. JOIN & OUTPUT: MERGE ALL THREE METRICS BASED ON THE BRIDGE ID AND THE SPECIFIC 10-MINUTE WINDOW.
    return (
      temp_agg.alias("t")
        .join(vib_agg.alias("v"), on=["bridge_id", "window_start", "window_end"], how="inner")
        .join(tilt_agg.alias("l"), on=["bridge_id", "window_start", "window_end"], how="inner")
        .select(
          "bridge_id", "name", "location", "window_start", "window_end",
          round(col("avg_temperature"), 2).alias("avg_temperature"), # ROUND FOR READABILITY
          "max_vibration", "max_tilt_angle"
        )
    )
