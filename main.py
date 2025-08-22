from loguru import logger
from log_generator import generate_logs
from log_ingestor import ingest_logs
from scripts import log_parser, data_preprocessing, anomaly_detection

def main():
    logger.info("🚀 Starting AI-SOC pipeline")

    # Step 1: Generate mock logs
    raw_logs = generate_logs(num_logs=200)
    logger.info(f"Generated {len(raw_logs)} logs")

    # Step 2: Parse logs
    parsed_logs = [log_parser.parse_log(line) for line in raw_logs]
    parsed_logs = [log for log in parsed_logs if log]  # drop None
    logger.info(f"Parsed {len(parsed_logs)} logs")

    # Step 3: Preprocess logs
    df = data_preprocessing.preprocess(parsed_logs)
    logger.info(f"Preprocessed logs into dataframe with shape {df.shape}")

    # Step 4: Run anomaly detection
    anomalies = anomaly_detection.detect_anomalies(df)
    logger.info(f"Detected {len(anomalies)} anomalies")

    # Step 5: Ingest to Elasticsearch
    ingest_logs(parsed_logs)
    logger.info("✅ Pipeline completed successfully")

if __name__ == "__main__":
    main()
