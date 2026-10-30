import urllib.request
import json     
import time


# Load the secret URL from the .env vault file
with open('.env', 'r') as f:
    for line in f:
        if line.startswith('SLACK_WEBHOOK_URL='):
            SLACK_WEBHOOK_URL = line.split('=', 1)[1].strip()
def simulate_pipeline_failure():
    print("🔄 [DataForge Engine] Starting mock payroll data ingestion...")
    time.sleep(1)
    
    print("⚠️ [DataForge Engine] Simulating upstream API timeout (HTTP 504)...")
    time.sleep(1)
    
    payload = {
        "text": " *DATAFORGE ALERT: Pipeline Failure Detected*\n"
                "• *Source:* Mock Payroll API\n"
                "• *Error:* HTTP 504 Gateway Timeout\n"
                "• *Action:* Record quarantined. Retry scheduled.\n"
                "• *Status:* Engineering team notified. Zero data loss."
    }
    
    print(" [DataForge Engine] Firing Slack webhook alert...")
    
    # Convert the message to JSON format
    json_data = json.dumps(payload).encode('utf-8')
    
    # Create the request
    req = urllib.request.Request(
        SLACK_WEBHOOK_URL,
        data=json_data,
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        # Send the request
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("✅ [DataForge Engine] Alert delivered successfully. Pipeline secure.")
        else:
            print(f" [DataForge Engine] Slack alert failed with code: {response.getcode()}")
    except Exception as e:
        print(f"❌ [DataForge Engine] Error: {e}")

if __name__ == "__main__":
    simulate_pipeline_failure()