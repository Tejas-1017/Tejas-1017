import os
import subprocess

GITHUB_USERNAME = "Tejas-1017"

repos = [
    "Tejas-1017", # Special repository for GitHub Profile README
    "ai-powered-ppe-detection-yolo",
    "genai-rag-knowledge-engine",
    "realtime-driver-drowsiness-ai",
    "edge-ai-object-detection-esp32",
    "autonomous-edge-vision-rover",
    "smart-industrial-machine-health",
    "ble-smart-lock-system",
    "assistive-robotics-parkinsons",
    "multiscope-health-monitor"
]

def main():
    print(f"=== AUTOMATED PUSH TO GITHUB ACCOUNT: {GITHUB_USERNAME} ===")
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Profile README repository setup
    profile_dir = os.path.join(base_dir, GITHUB_USERNAME)
    os.makedirs(profile_dir, exist_ok=True)
    readme_src = os.path.join(base_dir, "GITHUB_PROFILE_README.md")
    readme_dst = os.path.join(profile_dir, "README.md")
    
    with open(readme_src, "r", encoding="utf-8") as f:
        content = f.read()
    with open(readme_dst, "w", encoding="utf-8") as f:
        f.write(content)

    subprocess.run(["git", "init"], cwd=profile_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["git", "add", "."], cwd=profile_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["git", "commit", "-m", "Initial commit: Award-winning GitHub profile README"], cwd=profile_dir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    for repo in repos:
        repo_path = os.path.join(base_dir, repo)
        if not os.path.exists(repo_path):
            print(f"[SKIP] Directory {repo} not found.")
            continue

        remote_url = f"git@github.com:{GITHUB_USERNAME}/{repo}.git"
        print(f"\n[PROCESSING] {repo}")
        
        subprocess.run(["git", "branch", "-M", "main"], cwd=repo_path)
        subprocess.run(["git", "remote", "remove", "origin"], cwd=repo_path, stderr=subprocess.DEVNULL)
        subprocess.run(["git", "remote", "add", "origin", remote_url], cwd=repo_path)

        print(f"[INFO] Pushing to {remote_url} via SSH...")
        res = subprocess.run(["git", "push", "-u", "origin", "main"], cwd=repo_path, capture_output=True, text=True)
        if res.returncode == 0:
            print(f"[SUCCESS] Pushed {repo} to GitHub!")
        else:
            print(f"[NOTE] Remote repository '{repo}' not found on GitHub yet. Create an empty repo '{repo}' on https://github.com/new, then run this script.")

if __name__ == "__main__":
    main()
