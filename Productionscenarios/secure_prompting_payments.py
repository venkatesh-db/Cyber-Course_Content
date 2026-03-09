import logging
import re

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Case Study: Secure Prompting for Payments
# Scenario: Ensuring secure handling of sensitive payment data.

# Example payment data
payment_data = {
    "card_number": "4111111111111111",  # PAN (Primary Account Number)
    "expiry_date": "12/26",
    "cvv": "123",
    "amount": 100.50,
    "token": "tok_1234567890abcdef"
}

# Function to sanitize sensitive data
def sanitize_payment_data(data):
    sanitized_data = data.copy()

    # Mask PAN (only show last 4 digits)
    if "card_number" in sanitized_data:
        sanitized_data["card_number"] = re.sub(r"\d(?=\d{4})", "*", sanitized_data["card_number"])

    # Remove CVV
    if "cvv" in sanitized_data:
        sanitized_data.pop("cvv")

    # Truncate token
    if "token" in sanitized_data:
        sanitized_data["token"] = sanitized_data["token"][:8] + "..."

    return sanitized_data

# Function to securely log payment data
def log_payment_data(data):
    sanitized_data = sanitize_payment_data(data)
    logging.info(f"Processed payment data: {sanitized_data}")

log_payment_data(payment_data)

# Offline LLM Usage Strategy
# Example: Using a local LLM (e.g., Llama or Mistral) for secure processing

def process_with_offline_llm(prompt):
    # Simulated offline LLM processing
    logging.info("Processing prompt with offline LLM...")
    response = f"Simulated response for prompt: {prompt[:50]}..."
    return response

# Example prompt
prompt = "Process payment for card number 4111111111111111 with token tok_1234567890abcdef."

# Sanitize prompt before sending to LLM
sanitized_prompt = sanitize_payment_data({"card_number": "4111111111111111", "token": "tok_1234567890abcdef"})
response = process_with_offline_llm(f"Process payment for card ending in {sanitized_prompt['card_number']} with token {sanitized_prompt['token']}.")

logging.info(f"LLM Response: {response}")