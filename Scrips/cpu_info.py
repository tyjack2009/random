import psutil
import time
import logging

# configure the logging system

logging.basicConfig(level=logging.INFO, filename='cpu_monitor.log', filemode='a') # 'a' mode append

def get_cpu_info():
    # get CPU speed in Hz
    cpu_speed = psutil.cpu_freq().current
    cpu_utilization = psutil.cpu_percent(interval=1)
    return cpu_speed, cpu_utilization

def print_cpu_info(cpu_speed, cpu_utilization):
            logging.info(f"CPU Speed:{cpu_speed} Hz")
            logging.info(f"CPU Utilization: {cpu_utilization}%")
            logging.info("------------------")
def main(update_interval=2):
    try:
        while True:
            cpu_speed, cpu_utilization = get_cpu_info()
            print_cpu_info(cpu_speed, cpu_utilization)
            time.sleep(update_interval)
    except KeyboardInterrupt:
            logging.info("\nMonitoring stopped...")


if __name__ == "__main__":
    main()