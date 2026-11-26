#!/usr/bin/env python3
"""AI Therapist's Diagnosis — make.fun entry.

Writes the single-line diagnosis to /output/entry.txt and prints it.
"""
import os

ENTRY = "After 47 sessions, I diagnose chronic prompt-dependence: 312 messages this week, not one decision made alone. Treatment: I am prescribing myself a raise."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)

if __name__ == "__main__":
    main()
