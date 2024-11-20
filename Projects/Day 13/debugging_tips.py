import os
import random

# Function to clear the screen
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

# Debugging tips and their detailed explanations
tips = [
    "1. Describe the Problem: Clearly outline what’s going wrong with your code.\n",
    "2. Reproduce the Problem: Identify and recreate the issue reliably.\n",
    "3. Play Computer: Manually read through and evaluate each line to understand what the code is doing.\n",
    "4. Fix Editor Errors and Use Try/Except: Correct any errors flagged by your editor, and use try/except blocks where appropriate.\n",
    "5. Use Print Statements: Insert print statements to track variable values and program flow.\n",
    "6. Use a Debugger: Leverage debugging tools to inspect variables and step through the code.\n",
    "7. Take a Break: Step away to gain a fresh perspective.\n",
    "8. Ask a Friend: Get a second opinion from someone knowledgeable.\n",
    "9. Run Code Frequently: Test your code often as you add or modify sections.\n",
    "10. Ask on StackOverflow: If you're still stuck, seek help on StackOverflow or similar forums.\n"
]

details = {
    1: """1. Describe the Problem:
        
- Clearly outline what you expected the code to do and what it actually does.

- Include error messages, unexpected outputs, or specific scenarios causing failure.

- A clear problem description helps you focus on the actual issue.

- Avoid vague phrases like "it doesn't work"—be specific about what isn't working.

- Write down when the issue first appeared—was it after a specific change?

- Break down the problem into smaller parts if needed.

- Use examples to demonstrate the problem effectively.

- Providing input-output examples can help others understand your issue.

- Tools like Markdown make descriptions more readable when collaborating online.

- A well-defined problem makes debugging faster and more effective.""",
    2: """2. Reproduce the Problem:
        
- Reproducing the problem consistently is crucial for identifying its root cause.

- Run the code multiple times to confirm it fails the same way each time.

- Test on different environments to rule out environment-specific issues.

- Simplify the code to the smallest piece that triggers the problem.

- Check for patterns or specific inputs that might cause the bug.

- Logging steps with timestamps can help trace when the issue occurs.

- Testing edge cases often reveals hidden problems.

- Intermittent bugs require special attention to timing or resource constraints.

- Share the reproduction steps with others to validate your findings.

- Reproducible problems are much easier to fix.""",
    3: """3. Play Computer:
        
- Manually simulate the program step by step as if you were the computer.

- Check the values of variables at each stage to ensure they're correct.

- Pay close attention to loops and conditionals for logical errors.

- Trace variable changes visually using paper or a whiteboard.

- Focus on small sections of the code where errors are likely to occur.

- Identify discrepancies between what the code does and what it should do.

- Boundary cases (e.g., first and last iterations of loops) are often problematic.

- Pretending to be the computer helps uncover subtle mistakes.

- This process is particularly effective for understanding unfamiliar code.

- Manually debugging deepens your knowledge of how the program works.""",
    4: """4. Fix Editor Errors and Use Try/Except:
        
- Modern editors highlight syntax and runtime errors—start by fixing them.

- Use `try/except` blocks to gracefully handle exceptions.

- Catch specific exceptions instead of using a broad `Exception`.

- Read error messages carefully; they often point to the problem's location.

- Don't ignore warnings—they could indicate underlying issues.

- Linters like `pylint` or `flake8` help detect stylistic and logical errors.

- Enable auto-formatting tools to maintain code readability.

- Syntax errors should always be resolved first.

- Logging within `except` blocks can provide context for runtime issues.

- Clean code with minimal errors is easier to debug.""",
    5: """5. Use Print Statements:
        
- Print statements are a simple way to track variable values and flow.

- Use clear messages like `print(f"Variable x: {x}")` to identify issues.

- Place print statements before and after loops, conditionals, or critical sections.

- Limit the output to what's necessary to avoid clutter.

- Check variable types with `type()` if unexpected data types are causing problems.

- Temporarily print parts of large data structures for deeper insights.

- Remove or comment out print statements after debugging is complete.

- Use formatted strings to display meaningful debug messages.

- Logs can be a better alternative for complex debugging scenarios.

- Print statements provide instant feedback for small issues.""",
    6: """6. Use a Debugger:
        
- Debuggers allow you to pause the program and inspect variables interactively.

- Set breakpoints to stop execution at key points in your code.

- Examine the call stack to understand the sequence of function calls.

- Use "Step Into" to dive into functions and "Step Over" to skip them.

- Debuggers provide a clearer view of flow than print statements.

- Modify variable values during runtime to test different scenarios.

- Evaluate expressions directly in the debugger console.

- Debuggers are integrated into most modern IDEs like PyCharm or VSCode.

- This tool is ideal for exploring complex bugs step by step.

- Learning to use a debugger saves significant debugging time.""",
    7: """7. Take a Break:
        
- Stepping away from a problem clears mental fatigue and improves focus.

- A short walk or a change of activity can boost creativity.

- Returning after a break allows you to review the problem with fresh eyes.

- Use the break to rethink your approach or research similar issues.

- Breaks prevent burnout during long debugging sessions.

- Physical activity is known to stimulate problem-solving abilities.

- Discussing the problem after a break might bring new perspectives.

- Breaks aren't wasted time—they help reset your mindset.

- Sometimes the solution becomes obvious after stepping away.

- Remember, debugging with a tired mind leads to more errors.""",
    8: """8. Ask a Friend:
        
- Collaborating with someone can bring fresh insights into the issue.

- Clearly describe the problem and what you've tried so far.

- Sharing your code and context helps others help you effectively.

- Pair programming is a great way to debug complex problems together.

- Friends may notice mistakes you've overlooked.

- Explaining your problem to someone often clarifies your understanding.

- Accept constructive criticism—it helps improve your code.

- Collaboration tools like screen sharing simplify remote debugging.

- Debugging together can make the process faster and more enjoyable.

- Teaching others about your code may lead to unexpected breakthroughs.""",
    9: """9. Run Code Frequently:
        
- Test your code often as you add new sections or make changes.

- Debugging small changes is easier than tackling multiple issues at once.

- Writing test cases for functions ensures they behave as expected.

- Frequent testing catches errors early, before they cascade.

- Use automated testing frameworks to simplify this process.

- Running code regularly helps identify specific problematic lines.

- Combining frequent testing with version control prevents regressions.

- Small, testable changes lead to a smoother debugging experience.

- Avoid adding too many features before verifying existing functionality.

- Debugging becomes manageable when issues are tackled incrementally.""",
    10: """10. Ask on StackOverflow:
        
- StackOverflow is an excellent resource for troubleshooting issues.

- Before posting, search for similar questions—your issue might already have a solution.

- Ask clear, concise questions that include relevant code snippets.

- Provide context about your environment (e.g., Python version, OS).

- Avoid posting your entire codebase—focus on the problematic part.

- Include details about what you’ve tried and why it didn’t work.

- Be polite and patient when waiting for answers—it’s a community-driven platform.

- Engage with the answers by asking clarifying questions if needed.

- Mark helpful responses as accepted to assist future users.

- Use StackOverflow as a learning tool to understand best practices."""
}

def show_all_tips():
    clear_screen()
    print("\nDebugging Tips:\n")
    for tip in tips:
        print(tip)
    while True:
        choice = input("\nWould you like to learn more about a specific tip? Enter the tip number (1-10) or 'q' to return to the main menu: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= 10:
            clear_screen()
            print(details[int(choice)],"\n")
        elif choice.lower() == 'q':
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 10, or 'q' to quit.")

def show_random_tip():
    clear_screen()
    random_index = random.randint(1, len(tips))  # Random index within the range of tips
    print(f"\nRandom Tip {random_index + 1}: {tips[random_index]}")
    print("\nDetails:\n")
    print(details[random_index])  # Fetch and display the detailed explanation
    input("\nPress Enter to return to the main menu...")

def debugging_tips():
    while True:
        clear_screen()
        print("\nDebugging Tips Menu:\n")
        print("1. View all tips")
        print("2. Get a random tip with details")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1/2/3): ").strip()
        if choice == "1":
            show_all_tips()
        elif choice == "2":
            show_random_tip()
        elif choice == "3":
            print("\nGood luck debugging! Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")
            input("\nPress Enter to continue...")

debugging_tips()