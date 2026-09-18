import sys
import qvac

def run_app():
    print("========================================")
    print("   QVAC On-Device Offline AI Notes     ")
    print("========================================")
    
    # Required by Challenge: Call loadModel
    print("[1/3] Loading local model into memory...")
    model = qvac.loadModel("qwen2.5-0.5b-instruct")
    print("[✓] Model loaded on-device successfully.")
    
    # Prompt input
    prompt = input("\nEnter note or topic to analyze: ").strip()
    if not prompt:
        prompt = "Explain binary search time complexity in 2 lines."
        print(f"Using default prompt: {prompt}")

    print("\n[2/3] Running local inference on-device...")
    # Required by Challenge: Call completion
    response = qvac.completion(
        model=model,
        prompt=f"You are a study assistant. Analyze this note and give structured bullet points:\n{prompt}",
        max_tokens=150
    )

    print("\n[3/3] AI Output:")
    print("----------------------------------------")
    print(response.get("text", response))
    print("----------------------------------------")

if __name__ == "__main__":
    try:
        run_app()
    except KeyboardInterrupt:
        print("\nExiting application.")
        sys.exit(0)
