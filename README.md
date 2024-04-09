# Gemini_Bot Generative AI Python Client

This Python script demonstrates how to use the Palm Generative AI client to interact with a language model API. The client allows you to generate text based on prompts provided to it. This README provides instructions on how to set up and use the client effectively.

## Installation

To use the Palm Generative AI Python client, you must have Python installed on your system. You can install the client via pip:

```bash
pip install google-generativeai
```

## Usage

1. Import the required modules:

    ```python
    import google.generativeai as palm
    import signal
    ```

2. Define a signal handler to gracefully exit the program when Ctrl+C is pressed:

    ```python
    def handle_interrupt(sig, frame):
        """Gracefully exits the program on Ctrl+C press."""
        print("exiting...")
        exit(0)

    signal.signal(signal.SIGINT, handle_interrupt) # Register the signal handler
    ```

3. Set up your API key:

    ```python
    API_KEY = "YOUR_API_KEY"
    palm.configure(api_key=API_KEY)
    ```

    Replace `"YOUR_API_KEY"` with your actual google.generativeai Generative AI API key.

4. Prompt the user to input their message:

    ```python
    prompt = str(input("Enter your prompt:"))
    ```

5. Make a request to the google.generativeai Generative AI API to generate a response based on the provided prompt:

    ```python
    response = palm.chat(messages=prompt, temperature=0.2, context="Speak like a AI assistance")
    ```

6. Print the generated response:

    ```python
    for message in response.messages:
        print(message['author'], message['content'])
    ```

## Notes

- The `temperature` parameter controls the randomness of the generated responses. Lower values produce more deterministic responses, while higher values produce more diverse responses.
- The `context` parameter can be used to provide additional context to the language model, influencing the generated responses.

## Example

Here's a commented-out example that can be used to process and print each line of the generated response separately:

```python
# for message in response.messages:
#           for i in message['content'].split('\n'):
#                    if count != 0:
#                        print(i)
#                        speak(i)
#                    count += 1
```

Uncomment and modify this section as needed to customize the output format of the generated text.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

For any issues or inquiries, please [open an issue](https://github.com/Ro706/Gemini_Bot/issues) in the GitHub repository.
