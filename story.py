

def guessConstellation(imageURL):
    from inference_sdk import InferenceHTTPClient
    from PIL import Image
    CLIENT = InferenceHTTPClient(
        api_url="https://detect.roboflow.com",
        api_key="ghzpyenPcNlDg1p1yWq9"
    )

    image = Image.open(imageURL)
    resizedImage = image.resize((640, 640))
    resizedPath = f'{imageURL}-resized.jpeg'
    resizedImage.save(resizedPath)

    result = CLIENT.infer(resizedPath, model_id="departing.earth-dqxez/5")

    return result['top']

def makeStory(guess):
    from groq import Groq
    client = Groq(api_key="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")
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Imagine you are a kid with a fantastical imagination. You look up into the night sky and see a universe of stars. Looking up, you see a cluster of stars that looks like a {guess}. Generate a magical, and mythological backstory behind the constellation and what the meaning of it is. Make sure to include {guess} and only generate the story, no other words. Make the story fit within 600 characters with no incomplete sentences.",
        }
    ], 
    model="llama3-8b-8192",
    )

    story = chat_completion.choices[0].message.content

    print(story)

    return story



    
