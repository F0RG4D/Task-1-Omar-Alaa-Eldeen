def rule_based_chatbot():
    print("System Initialized: DecodeLabs Rule-Based Guardrail")
    print("(Type 'exit' to execute kill command)\n")

    # KNOWLEDGE BASE: Dictionary with 5+ intents[cite: 1]
    # Replaces the O(n) if-elif ladder with an O(1) Hash Map[cite: 1]
    knowledge_base = {
        'hello': 'Hi there!',
        'hi': 'Hi there!',
        'status': 'All systems operational. The logic engine is running.',
        'help': 'I am a deterministic system. Ask me about my status, creator, or mission.',
        'creator': 'I was built following the DecodeLabs IPO blueprint.',
        'mission': 'To serve as a deterministic guardrail before probabilistic LLM integration.',
        'bye': 'Goodbye!'
    }

    # EXIT STRATEGY: Clean break commands[cite: 1]
    exit_commands = {'exit', 'quit', 'stop', 'bye'}

    # THE HEARTBEAT: Continuous 'while' cycle[cite: 1]
    while True:
        
        # PHASE 1: INPUT & SANITIZATION[cite: 1]
        raw_input = input("You: ")
        clean_input = raw_input.lower().strip()

        # Check for the kill command to break the infinite cycle[cite: 1]
        if clean_input in exit_commands:
            print("System: Terminating cycle. Goodbye.")
            break

        # INTENT MATCHING & FALLBACK: The .get() Method[cite: 1]
        # Atomic operation combining instant lookup and a default fallback[cite: 1]
        reply = knowledge_base.get(clean_input, 'I do not understand.')
        
        # PHASE 3: OUTPUT[cite: 1]
        print(f"System: {reply}")

if __name__ == "__main__":
    rule_based_chatbot()