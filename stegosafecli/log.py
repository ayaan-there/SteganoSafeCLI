"""
Logging operations for StegoSafeCLI.
"""
import datetime

def log_operation(action, input_path, output_path, mode):
    with open('stegosafe.log', 'a', encoding='utf-8') as f:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(f'{timestamp} | {action} | {input_path} | {output_path or "-"} | {mode}\n')
