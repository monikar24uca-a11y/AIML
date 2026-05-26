from openai import OpenAI

# Create client
client = OpenAI(
    api_key="YOUR_API_KEY"
)

print("AI Assistant Started")
print("Type 'exit' to stop\n")

while True:

    user_input = input("You: ")

    # Exit condition
    if user_input.lower() == "exit":
        print("Chat ended")
        break

    # API request
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a smart AI assistant."
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    # Display response
    ai_reply = response.choices[0].message.content

    print("AI:", ai_reply)