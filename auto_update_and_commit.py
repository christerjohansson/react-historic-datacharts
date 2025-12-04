import subprocess
import sys
from datetime import datetime
from pathlib import Path

def run_command(command, cwd=None, use_shell=True):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(
            command,
            shell=use_shell,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout, result.stderr, result.returncode
    except subprocess.CalledProcessError as e:
        return e.stdout, e.stderr, e.returncode

def main():
    # Get the project root directory
    project_root = Path(__file__).parent
    
    print("=" * 60)
    print("Auto Update & Commit Stock Prices")
    print("=" * 60)
    print(f"Project: {project_root}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print()
    
    # Step 1: Run the stock price updater
    print("[1/4] Running stock price updater...")
    stdout, stderr, returncode = run_command(
        [sys.executable, "update_stock_prices.py"],
        cwd=project_root,
        use_shell=False
    )
    
    if returncode != 0:
        print(f"❌ Error running update_stock_prices.py:")
        print(stderr)
        return 1
    
    print("✅ Stock prices updated successfully")
    print()
    
    # Step 2: Stage changes
    print("[2/4] Staging changes...")
    stdout, stderr, returncode = run_command("git add app/data/stock_prices.json", cwd=project_root)
    
    if returncode != 0:
        print(f"❌ Error staging changes:")
        print(stderr)
        return 1
    
    print("✅ Changes staged")
    print()
    
    # Step 3: Check if there are changes to commit
    print("[3/4] Checking for changes...")
    stdout, stderr, returncode = run_command("git diff --cached --quiet", cwd=project_root)
    
    if returncode == 0:
        print("ℹ️  No changes to commit")
        return 0
    
    print("✅ Changes detected")
    print()
    
    # Step 4: Commit changes
    print("[4/4] Committing changes...")
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    commit_message = f"Update stock prices - {timestamp}"
    
    stdout, stderr, returncode = run_command(
        f'git commit -m "{commit_message}"',
        cwd=project_root
    )
    
    if returncode != 0:
        print(f"❌ Error committing changes:")
        print(stderr)
        return 1
    
    print(f"✅ Committed: {commit_message}")
    print()
    
    # Show commit info
    stdout, stderr, _ = run_command("git log -1 --oneline", cwd=project_root)
    print("Latest commit:")
    print(f"  {stdout.strip()}")
    print()
    
    print("=" * 60)
    print("✨ All done!")
    print("=" * 60)
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
