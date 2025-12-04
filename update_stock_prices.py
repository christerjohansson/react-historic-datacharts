import json
import random
from pathlib import Path

def update_stock_prices(file_path):
    """
    Updates stock prices in the JSON file with random variations.
    
    - Updates closingPrice by a random value within ±10% of current value
    - Calculates new averagePrice based on the new closingPrice
    
    Args:
        file_path: Path to the stock_prices.json file
    """
    # Read the JSON file
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            stock_data = json.load(f)
        
        print(f"Loaded {len(stock_data)} stock entries from {file_path}")
        
        # Update each stock entry
        for entry in stock_data:
            symbol = entry.get('symbol', 'Unknown')
            year = entry.get('year', 'Unknown')
            old_closing = entry['closingPrice']
            old_average = entry['averagePrice']
            
            # Calculate new closingPrice within ±10% range
            min_price = old_closing * 0.9  # 90% of current value
            max_price = old_closing * 1.1  # 110% of current value
            new_closing = random.uniform(min_price, max_price)
            
            # Calculate new averagePrice based on new closingPrice
            # Using a simple approach: adjust the average proportionally to the closing price change
            price_change_ratio = new_closing / old_closing
            new_average = old_average * price_change_ratio
            
            # Update the entry
            entry['closingPrice'] = round(new_closing, 10)
            entry['averagePrice'] = round(new_average, 10)
            
            print(f"{symbol} ({year}): Closing ${old_closing:.2f} -> ${new_closing:.2f}, "
                  f"Average ${old_average:.2f} -> ${new_average:.2f}")
        
        # Write the updated data back to the file
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(stock_data, f, indent=4)
        
        print(f"\nSuccessfully updated {len(stock_data)} entries in {file_path}")
        
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {file_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Path to the stock prices JSON file
    json_file_path = Path(__file__).parent / "app" / "data" / "stock_prices.json"
    
    print("=" * 60)
    print("Stock Price Update Program")
    print("=" * 60)
    print(f"Target file: {json_file_path}")
    print("Action: Update closing prices with ±10% random variation")
    print("=" * 60)
    print()
    
    # Run the update
    update_stock_prices(json_file_path)
