# Making markets and making bank

## 1. Files Overview
### 1.1. Given files
+ datamodel.py: type definitions for IMC objects
+ trader.py: only "Trader.run()" skeleton is given. All extra trading code must be in this file and invoked by "run()" method
### 1.2. Helper files
+ sample_trade.py: sample test data 
+ main.py: simple local testing with test data. Invoke with "python3 main.py <test_case>"
+ process_data.py: parsing data from log files into csv. Only retrieve lines with that contain "keyword". Invoke with "python3 process_data.py <folder_path> <log_file_name> <output_file_name> <keyword>".
    Example: python3 process_data.py data/tutorial/ dump.log out.csv TRADE